#coding=utf-8
#This calc is used for calculate
#1.how long did the borrower get the money
#2.how much principal&interest should pay back
#3.how much the lender get
##notic:a.利息，计头不计尾。b.到期应还利息 计算时，借款期限需要换算为 年+月+天
##1.到期应还利息=本金*年利率*年+本金*年利率*月/12+本金*年利率*天/360
##2.应计利息=本金*年利率*实际借款天数/360
##3.罚息=（到期应还利息-应计利息）*提前还款违约金比例

import datetime


##-------------------------------参数初始化*Begin------------------------####
#startYear=2015
#startMonth=11
#startDay=17
#startDate=datetime.datetime(startYear,startMonth,startDay)  ##放款日期

#endYear=2015
#endMonth=12
#endDay=17
#endDate=datetime.datetime(endYear,endMonth,endDay)  ##还款日

#duration=1              ##  借款期限
#durationType=0          ##  0 表示月；1 表示天

#rateOfYear=0.075        #   年利率

#principal=3000000       ##  本金

#ratOfPunish=0.3         ##  提前还款违约比例

##-------------------------------参数初始化*End------------------------####
class amtCalc():

    def setStart(self,startYear,startMonth,startDay):
        self.startDate=datetime.datetime(startYear,startMonth,startDay)
        
    def setEnd(self,endYear,endMonth,endDay):
        self.endDate=datetime.datetime(endYear,endMonth,endDay)
        
    def daysOfMonth(self,dateYear):##获得每个月天数，按平年和闰年
                    daysOfMonth_p=[0,31,28,31,30,31,30,31,31,30,31,30,31]  #平年，array[i]表示i月的天数
                    daysOfMonth_r=[0,31,29,31,30,31,30,31,31,30,31,30,31]  #润年，array[i]表示i月的天数
                    if(dateYear%100==0 and dateYear%400==0):##闰年
                            return daysOfMonth_r
                    elif(0!=dateYear%100 and dateYear%4==0):##闰年
                            return daysOfMonth_r
                    else:
                            return daysOfMonth_p	

    def getEndDate(self,StartDate,Duration,DurationType):  ##获取还款日期

            EndDate=[0,0,0]##[年，月，日]
            
            if((1!=DurationType) and (0!=DurationType)):
                    print 'date type error'

            elif(0==DurationType):
                    EndDate[0]=(StartDate.year+(StartDate.month+Duration)/12)
                    EndDate[1]=(StartDate.month+Duration)%12
                    if(0==EndDate[1]):##当和为12整数倍时，1.月份为12月；2.年数需要减去当前满12加上的1年
                            EndDate[0]-=1
                            EndDate[1]=12
                    EndDate[2]=StartDate.day
                    DaysOfMonth=self.daysOfMonth(EndDate[0])
                    if(EndDate[2]>DaysOfMonth[EndDate[1]]):##如果借款日期大于到期月份的天数，则取到期月份的最后一天
                            EndDate[2]=DaysOfMonth[EndDate[1]]

            elif(1==DurationType):
                    EndDate[0]=(StartDate+datetime.timedelta(days=Duration)).year
                    EndDate[1]=(StartDate+datetime.timedelta(days=Duration)).month
                    EndDate[2]=(StartDate+datetime.timedelta(days=Duration)).day

            return EndDate

    def getYMD(self,StartDate,Duration,DurationType):

            interestDuration=[0,0,0]##总利息计算时，借款时间需要转换为 几个月零几天

            if(0==DurationType):
                    interestDuration[1]=Duration
            elif(1==DurationType):
                    EndDate=self.getEndDate(StartDate,Duration,DurationType)
                    if(EndDate[2]>=StartDate.day):
                            interestDuration[1]=(EndDate[0]-StartDate.year)*12+EndDate[1]-StartDate.month
                            interestDuration[2]=EndDate[2]-StartDate.day
                    else:
                            interestDuration[1]=(EndDate[0]-StartDate.year)*12+EndDate[1]-StartDate.month-1
                            tmp=[EndDate[0],EndDate[1],StartDate.day]
                            tmp[1]=EndDate[1]-1
                            if(0==tmp[1]):
                                    tmp[1]=12
                                    tmp[0]=EndDate[0]-1
                            DaysOfMonth=self.daysOfMonth(EndDate[0])
                            if(tmp[2]>DaysOfMonth[tmp[1]]):
                                    tmp[2]=DaysOfMonth[tmp[1]]
                            interestDuration[2]=(datetime.datetime(EndDate[0],EndDate[1],EndDate[2])-datetime.datetime(tmp[0],tmp[1],tmp[2])).days
            interestDuration[0]=interestDuration[1]/12
            interestDuration[1]=interestDuration[1]%12
            return interestDuration

    def interest(self,StartDate,EndDate,Duration,DurationType,principal,rateOfYear,ratOfPunish):
            interest=[0,0,0,0]##[总利息，应计利息，实际利息，提前还款违约金]
            ##到期还款
            if(EndDate==datetime.datetime(self.getEndDate(StartDate,Duration,DurationType)[0],self.getEndDate(StartDate,Duration,DurationType)[1],self.getEndDate(StartDate,Duration,DurationType)[2])):
                for i in [0,1,2]:
                    interest[i]=self.getYMD(StartDate,Duration,DurationType)[0]*rateOfYear*principal+self.getYMD(StartDate,Duration,DurationType)[1]*rateOfYear/12*principal+self.getYMD(StartDate,Duration,DurationType)[2]*rateOfYear/360*principal
                    interest[i]=round(interest[i],2)
                    #print interest[i]
            ##提前还款
            else:
                    ##总利息
                    interest[0]=round(self.getYMD(StartDate,Duration,DurationType)[0]*rateOfYear*principal+self.getYMD(StartDate,Duration,DurationType)[1]*rateOfYear/12*principal+self.getYMD(StartDate,Duration,DurationType)[2]*rateOfYear/360*principal,2)
                    ##应计利息
                    interest[1]=round((EndDate-StartDate).days*rateOfYear/360*principal,2)
                    ##提前还款违约金
                    interest[3]=round((interest[0]-interest[1])*ratOfPunish,2)
                    if(interest[3]>principal*rateOfYear/12):
                            interest[3]=round(principal*rateOfYear/12,2)
                    if(interest[3]<0):
                        interest[3]=0
                    ##实际利息
                    interest[2]=round(interest[1]+interest[3],2)
            
            
            return interest


#print 'start',startDate

#print 'end:',getEndDate(startDate,duration,durationType)

#print 'duration:',getYMD(startDate,duration,durationType)[0],u'年',getYMD(startDate,duration,durationType)[1],u'个月',getYMD(startDate,duration,durationType)[2],u'天'

#print '**************Interest**************'
#print u'到期利息：',interest(startDate,endDate,duration,durationType,principal,rateOfYear,ratOfPunish)[0],u'实际利息:',interest(startDate,endDate,duration,durationType,principal,rateOfYear,ratOfPunish)[2],u'本息和：',principal+interest(startDate,endDate,duration,durationType,principal,rateOfYear,ratOfPunish)[2]
#print u'应计利息:',interest(startDate,endDate,duration,durationType,principal,rateOfYear,ratOfPunish)[1],u'提前还款违约金:',interest(startDate,endDate,duration,durationType,principal,rateOfYear,ratOfPunish)[3]
