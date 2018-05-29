#!/usr/bin/python
# -*- coding: UTF-8 -*-

import serial.tools.list_ports
import wx
import threading
import mysquare
from mythreading import stop_thread



def readData(self):
    print('-> start')
    self.ser = serial.Serial(self.m_cbCOM.GetValue(), 19200, timeout=1)
    while 1:
        x = self.ser.read()
        self.m_txtData.AppendText("data:" + str(x, encoding="utf-8") + "\n")

class GetDataFrame(mysquare.GetData):

    def __init__(self, parent):
        mysquare.GetData.__init__(self, parent)
        plist = list(serial.tools.list_ports.comports())
        comlist = []
        for i in range(0,len(plist)):
            print(plist[i][0])
            comlist.append(plist[i][0])
        self.m_cbCOM.SetItems(comlist)
        if len(plist) <= 0:
            print("没有发现端口!")
        else:
            self.m_cbCOM.SetValue(comlist[0])
        #默认端口配置
        self.m_cbCOM.SetValue("COM1")


    def m_btnPORTOnButtonClick(self, event):  # 定义事件处理函数
        if self.m_btnPORT.GetLabelText() == "打开端口":
            wx.MessageBox('打开端口', '提示', wx.OK | wx.ICON_INFORMATION)
            self.t = threading.Thread(target=readData, args=(self,))
            self.t.start()
            self.m_btnPORT.SetLabelText("关闭端口")

        else:
            wx.MessageBox('关闭端口', '提示', wx.OK | wx.ICON_INFORMATION)
            stop_thread(self.t)
            self.ser.close()
            self.m_btnPORT.SetLabelText("打开端口")
        #num = int(self.m_textCtrl1.GetValue())
        #self.m_textCtrl2.SetValue(str(num * num))
        return True

app = wx.App(False)
frame = GetDataFrame(None)
frame.Show(True)
app.MainLoop()




#ser = serial.Serial("COM4", 9600, timeout=60)



#while 1:
    #char = ser.read()
    #print(char)

