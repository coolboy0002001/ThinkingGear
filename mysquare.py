# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class GetData
###########################################################################

class GetData ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"获取数据", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_lblCOM = wx.StaticText( self, wx.ID_ANY, u"选择串口：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblCOM.Wrap( -1 )
		bSizer2.Add( self.m_lblCOM, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		m_cbCOMChoices = [ u"COM1", u"COM2" ]
		self.m_cbCOM = wx.ComboBox( self, wx.ID_ANY, u"COM1", wx.DefaultPosition, wx.DefaultSize, m_cbCOMChoices, 0 )
		bSizer2.Add( self.m_cbCOM, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_btnPORT = wx.Button( self, wx.ID_ANY, u"打开端口", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_btnPORT, 0, wx.ALL, 5 )
		
		self.m_txtData = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,280 ), wx.TE_MULTILINE )
		bSizer1.Add( self.m_txtData, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_btnPORT.Bind( wx.EVT_BUTTON, self.m_btnPORTOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_btnPORTOnButtonClick( self, event ):
		event.Skip()
	

