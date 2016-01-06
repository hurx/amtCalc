import amtGUI
import wx

if '__main__'==__name__:
    app=wx.App()
    result=amtGUI.iFrame(None,-1,'AmtCalc')
    app.MainLoop()
