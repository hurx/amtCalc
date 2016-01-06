#encoding=utf-8

import wx
import os
import amtCalc

class iFrame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(500,650))

        panel=wx.Panel(self,-1,size=(500,650))##panel为窗口容器
        panel.SetBackgroundColour('white')

        condition_box=wx.BoxSizer(wx.VERTICAL)##HORIZONTAL为水平
        
#************************放款日期***************************#
        condition_box.Add((-1,20))##添加空隙
        
        box1=wx.BoxSizer(wx.HORIZONTAL)##VERTICAL
        
        fkDate=wx.StaticText(panel,-1,u'    放款日期： ')
        box1.Add(fkDate,proportion=0,flag=wx.EXPAND,border=0)
        
        self.fkYear=wx.TextCtrl(panel,-1,'2015',size=(50,-1))
        box1.Add(self.fkYear,proportion=0,flag=wx.EXPAND,border=0)
        
        text_year=wx.StaticText(panel,-1,u' 年 ')
        box1.Add(text_year,proportion=0,flag=wx.EXPAND,border=0)
        
        self.fkMonth=wx.TextCtrl(panel,-1,'11',size=(50,-1))
        box1.Add(self.fkMonth,proportion=0,flag=wx.EXPAND,border=0)        

        text_month=wx.StaticText(panel,-1,u' 月 ')
        box1.Add(text_month,proportion=0,flag=wx.EXPAND,border=0)

        self.fkDay=wx.TextCtrl(panel,-1,'23',size=(50,-1))
        box1.Add(self.fkDay,proportion=0,flag=wx.EXPAND,border=0)        

        text_day=wx.StaticText(panel,-1,u' 日 ')
        box1.Add(text_day,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=0)
        
        condition_box.Add((-1,10))##添加空隙
        
#************************借款期限***************************#

        box2=wx.BoxSizer(wx.HORIZONTAL)

        duration=wx.StaticText(panel,-1,u'    借款期限： ')
        box2.Add(duration,proportion=0,flag=wx.EXPAND,border=0)
        
        self.durationValue=wx.TextCtrl(panel,-1,'100',size=(80,-1))
        box2.Add(self.durationValue,proportion=0,flag=wx.EXPAND,border=0)

        durationTypeList=[u' 月',u' 天']
        self.durationType=wx.Choice(panel,-1,(85,18),choices=durationTypeList)
        self.durationType.SetSelection(0)
        box2.Add(self.durationType,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box2,flag=wx.ALL,border=0)
        
        condition_box.Add((-1,10))##添加空隙
    

#************************借款金额***************************#
        box3=wx.BoxSizer(wx.HORIZONTAL)##VERTICAL
        
        pricipal=wx.StaticText(panel,-1,u'    借款金额： ')
        box3.Add(pricipal,proportion=0,flag=wx.EXPAND,border=0)
        
        self.principalValue=wx.TextCtrl(panel,-1,'2000000',size=(150,-1))
        box3.Add(self.principalValue,proportion=0,flag=wx.EXPAND,border=0)
        
        principalType=wx.StaticText(panel,-1,u' 元')
        box3.Add(principalType,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box3,flag=wx.ALL,border=0)
        
        condition_box.Add((-1,10))##添加空隙
        
#************************利率***************************#
        box4=wx.BoxSizer(wx.HORIZONTAL)##VERTICAL
        
        rate=wx.StaticText(panel,-1,u'    利      率： ')
        box4.Add(rate,proportion=0,flag=wx.EXPAND,border=0)
        
        self.rateValue=wx.TextCtrl(panel,-1,'8.4',size=(50,-1))
        box4.Add(self.rateValue,proportion=0,flag=wx.EXPAND,border=0)
        
        rateType=wx.StaticText(panel,-1,u' %')
        box4.Add(rateType,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box4,flag=wx.ALL,border=0)
        
        condition_box.Add((-1,10))##添加空隙
        
#************************提前还款违约比例***************************#
        box5=wx.BoxSizer(wx.HORIZONTAL)##VERTICAL
        
        punish=wx.StaticText(panel,-1,u'    违约比例： ')
        box5.Add(punish,proportion=0,flag=wx.EXPAND,border=0)
        
        self.punishValue=wx.TextCtrl(panel,-1,'30',size=(50,-1))
        box5.Add(self.punishValue,proportion=0,flag=wx.EXPAND,border=0)
        
        punishType=wx.StaticText(panel,-1,u' %  (注：提前还款违约金比例)')
        box5.Add(punishType,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box5,flag=wx.ALL,border=0)
        
        condition_box.Add((-1,10))##添加空隙

#************************还款日期***************************#
        condition_box.Add((-1,40))##添加空隙
        
        box6=wx.BoxSizer(wx.HORIZONTAL)##VERTICAL
        
        hkDate=wx.StaticText(panel,-1,u'    还款日期： ')
        box6.Add(hkDate,proportion=0,flag=wx.EXPAND,border=0)
        
        self.hkYear=wx.TextCtrl(panel,-1,'2016',size=(50,-1))
        box6.Add(self.hkYear,proportion=0,flag=wx.EXPAND,border=0)
        
        hkYearType=wx.StaticText(panel,-1,u' 年 ')
        box6.Add(hkYearType,proportion=0,flag=wx.EXPAND,border=0)
        
        self.hkMonth=wx.TextCtrl(panel,-1,'3',size=(50,-1))
        box6.Add(self.hkMonth,proportion=0,flag=wx.EXPAND,border=0)        

        hkMonthType=wx.StaticText(panel,-1,u' 月 ')
        box6.Add(hkMonthType,proportion=0,flag=wx.EXPAND,border=0)

        self.hkDay=wx.TextCtrl(panel,-1,'2',size=(50,-1))
        box6.Add(self.hkDay,proportion=0,flag=wx.EXPAND,border=0)        

        hkDayType=wx.StaticText(panel,-1,u' 日 ')
        box6.Add(hkDayType,proportion=0,flag=wx.EXPAND,border=0)

        condition_box.Add(box6,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=0)
        
        condition_box.Add((-1,10))##添加空隙

#************************计算按键***************************#
        button=wx.Button(panel,-1,'Penging',size=(20,40))
        self.Bind(wx.EVT_BUTTON,self.calculate,button)
        condition_box.Add(button,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=0)
        
#************************结果输出***************************#
        self.result=wx.StaticText(panel,-1,u'')
        condition_box.Add(self.result,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=0)
        
 #**********************窗口初始化*************************#        
        self.SetSizer(condition_box)
        self.Centre()
        self.Show(True)


#************************按键事件***************************#
    def calculate(self,event):
        try:
            #获取界面上的参数
            self.iDict={
                'fkYear':self.fkYear.GetValue(),'fkMonth':self.fkMonth.GetValue(),'fkDay':self.fkDay.GetValue(),
                'durationValue':self.durationValue.GetValue(),'durationType':self.durationType.GetStringSelection(),
                'principalValue':self.principalValue.GetValue(),'rateValue':self.rateValue.GetValue(),
                'punishValue':self.punishValue.GetValue(),
                'hkYear':self.hkYear.GetValue(),'hkMonth':self.hkMonth.GetValue(),'hkDay':self.hkDay.GetValue()
                }
            #调用计算函数
            res=amtCalc.amtCalc()
            res.setStart(int(self.iDict['fkYear']),int(self.iDict['fkMonth']),int(self.iDict['fkDay']))
            res.setEnd(int(self.iDict['hkYear']),int(self.iDict['hkMonth']),int(self.iDict['hkDay']))
            #print res.startDate

            if(u'月'==self.iDict['durationType'].strip()):
                duYear=res.getYMD(res.startDate,int(self.iDict['durationValue']),0)[0]
                duMonth=res.getYMD(res.startDate,int(self.iDict['durationValue']),0)[1]
                duDay=res.getYMD(res.startDate,int(self.iDict['durationValue']),0)[2]

                #到期利息    
                intTotal=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[0]
                #应计利息
                intCur=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[1]
                #实际利息
                intPay=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[2]
                #本息和
                intPrin=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[2]+float(int(self.iDict['principalValue']))
                #提前还款违约金
                intPunish=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[3]

                #print res.startDate,res.endDate,int(self.iDict['durationValue']),0,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100
                #print intTotal,intCur,intPay,intPrin,intPunish
                #print duYear,duMonth,duDay
            elif(u'天'==self.iDict['durationType'].strip()):
                duYear=res.getYMD(res.startDate,int(self.iDict['durationValue']),1)[0]
                duMonth=res.getYMD(res.startDate,int(self.iDict['durationValue']),1)[1]
                duDay=res.getYMD(res.startDate,int(self.iDict['durationValue']),1)[2]
                #print duYear,duMonth,duDay
                #到期利息    
                intTotal=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[0]
                #应计利息
                intCur=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[1]
                #实际利息
                intPay=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[2]
                #本息和
                intPrin=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[2]+float(int(self.iDict['principalValue']))
                #提前还款违约金
                intPunish=res.interest(res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100)[3]

                #print res.startDate,res.endDate,int(self.iDict['durationValue']),1,float(self.iDict['principalValue']),float(self.iDict['rateValue'])/100,float(self.iDict['punishValue'])/100
                #print intTotal,intCur,intPay,intPrin,intPunish

            s='\n'+u'    到期利息(元)：'+str(intTotal)+'\n\n'\
               +u'    应计利息(元)：'+str(intCur)+'\n\n'\
               +u'    违 约  金(元)：'+str(intPunish)+'\n\n'\
               +u'    实际利息(元)：'+str(intPay)+'\n\n'\
               +u'    本 息  和(元)：'+str(intPrin)
            
            #print s
            self.result.SetLabel(s)

        except:
            dlg=wx.MessageDialog(None,u'请检查输入的参数','error massage',wx.YES_DEFAULT|wx.ICON_ERROR)
            if dlg.ShowModal()==wx.ID_YES:
                dlg.Destroy()

