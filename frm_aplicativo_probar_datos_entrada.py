# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import formEAY.utilCAC.ClasesValidatorEAY as cvEAY
import formEAY.constantesCAC.imgCAC as imgCAC
import frm_resultadoAplicativo  as frm_resultadoAplicativo

IMAGEN_LOGOCAC=imgCAC.Img_formularios.LOGOCAC

###########################################################################
## Class MainAplicativo
###########################################################################

class MainAplicativo(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Aplicativo Probar Datos", pos=wx.DefaultPosition,
                          size=wx.Size(500, 374), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 374), wx.Size(500, 374))

        bSizer56 = wx.BoxSizer(wx.VERTICAL)

        bSizer57 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel14 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel14.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer59 = wx.BoxSizer(wx.VERTICAL)

        bSizer60 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap12 = wx.StaticBitmap(self.m_panel14, wx.ID_ANY,
                                          wx.Bitmap(IMAGEN_LOGOCAC,
                                                    wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer60.Add(self.m_bitmap12, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer59.Add(bSizer60, 1, wx.EXPAND, 5)

        bSizer61 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel16 = wx.Panel(self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel16.SetBackgroundColour(wx.Colour(224, 224, 224))

        bSizer62 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer72 = wx.BoxSizer(wx.VERTICAL)

        bSizer63 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText37 = wx.StaticText(self.m_panel16, wx.ID_ANY, u"Arcos (A):", wx.DefaultPosition,
                                            wx.Size(120, -1), wx.ALIGN_RIGHT)
        self.m_staticText37.Wrap(-1)
        self.m_staticText37.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText37.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer63.Add(self.m_staticText37, 0, wx.ALL, 5)

        self.txt_a = wx.TextCtrl(self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_PROCESS_ENTER)
        self.txt_a.SetMaxLength(2)
        self.txt_a.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        bSizer63.Add(self.txt_a, 0, wx.ALL, 5)

        bSizer72.Add(bSizer63, 0, wx.EXPAND, 5)

        bSizer631 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText371 = wx.StaticText(self.m_panel16, wx.ID_ANY, u"Presillas (L):", wx.DefaultPosition,
                                             wx.Size(120, -1), wx.ALIGN_RIGHT)
        self.m_staticText371.Wrap(-1)
        self.m_staticText371.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText371.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer631.Add(self.m_staticText371, 0, wx.ALL, 5)

        self.txt_l = wx.TextCtrl(self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_PROCESS_ENTER)
        self.txt_l.SetMaxLength(2)
        self.txt_l.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        bSizer631.Add(self.txt_l, 0, wx.ALL, 5)

        bSizer72.Add(bSizer631, 0, wx.EXPAND, 5)

        bSizer632 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText372 = wx.StaticText(self.m_panel16, wx.ID_ANY, u"Verticilos (W):", wx.DefaultPosition,
                                             wx.Size(120, -1), wx.ALIGN_RIGHT)
        self.m_staticText372.Wrap(-1)
        self.m_staticText372.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText372.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer632.Add(self.m_staticText372, 0, wx.ALL, 5)

        self.txt_w = wx.TextCtrl(self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_PROCESS_ENTER)
        self.txt_w.SetMaxLength(2)
        self.txt_w.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        bSizer632.Add(self.txt_w, 0, wx.ALL, 5)

        bSizer72.Add(bSizer632, 1, wx.EXPAND, 5)

        bSizer6321 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3721 = wx.StaticText(self.m_panel16, wx.ID_ANY, u"SQTL:", wx.DefaultPosition, wx.Size(120, -1),
                                              wx.ALIGN_RIGHT)
        self.m_staticText3721.Wrap(-1)
        self.m_staticText3721.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText3721.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer6321.Add(self.m_staticText3721, 0, wx.ALL, 5)

        self.txt_sqtl = wx.TextCtrl(self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_PROCESS_ENTER)
        self.txt_sqtl.SetMaxLength(3)
        self.txt_sqtl.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        bSizer6321.Add(self.txt_sqtl, 0, wx.ALL, 5)

        bSizer72.Add(bSizer6321, 1, wx.EXPAND, 5)

        bSizer62.Add(bSizer72, 1, wx.EXPAND, 5)

        bSizer73 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel17 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel17.SetBackgroundColour(wx.Colour(208, 208, 208))

        bSizer78 = wx.BoxSizer(wx.VERTICAL)

        self.btn_evaluar = wx.Button(self.m_panel17, wx.ID_ANY, u"Evaluar", wx.DefaultPosition, wx.Size(120, -1),
                                     0 | wx.NO_BORDER)
        self.btn_evaluar.SetBackgroundColour(wx.Colour(128, 255, 128))

        bSizer78.Add(self.btn_evaluar, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel17.SetSizer(bSizer78)
        self.m_panel17.Layout()
        bSizer78.Fit(self.m_panel17)
        bSizer73.Add(self.m_panel17, 1, wx.EXPAND | wx.ALL, 5)

        bSizer62.Add(bSizer73, 1, wx.EXPAND, 5)

        self.m_panel16.SetSizer(bSizer62)
        self.m_panel16.Layout()
        bSizer62.Fit(self.m_panel16)
        bSizer61.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)

        bSizer59.Add(bSizer61, 0, wx.EXPAND, 5)

        self.m_panel14.SetSizer(bSizer59)
        self.m_panel14.Layout()
        bSizer59.Fit(self.m_panel14)
        bSizer57.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        bSizer56.Add(bSizer57, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer56)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_evaluar.Bind(wx.EVT_BUTTON, self.btn_evaluarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_evaluarOnButtonClick(self, event):
        a=self.txt_a.GetValue()
        l=self.txt_l.GetValue()
        w=self.txt_w.GetValue()
        sqtl=self.txt_sqtl.GetValue()

        if a == '':
            a=0
        if l == '':
            l=0
        if w == '':
            w=0
        if sqtl == '':
            sqtl=0

        a = int(a)
        l = int(l)
        w = int(w)
        sqtl = int(sqtl)


        if (a+l+w) != 10:
            wx.MessageBox(u'La suma de A+L+W debe ser 10', u'Atención...',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if sqtl > 300:
            wx.MessageBox(u'SQTL demasiado alto', u'Atención...',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if l>0 or w>0:
            if sqtl ==0:
                wx.MessageBox(u'SQTL debe ser mayor que Cero', u'Atención...',
                              wx.OK | wx.ICON_INFORMATION)
                return 0


        frame_resultado = frm_resultadoAplicativo.Resultados(self, a, l, w,sqtl)
        frame_resultado.Center()
        frame_resultado.Show()

        event.Skip()


if __name__ == '__main__':
    app=wx.App()

    frame_principal = MainAplicativo(None)
    frame_principal.Center()
    frame_principal.Show()

    # rows = dbClientes.cargarLista_ids_atletas()
    #
    # for id in rows:
    #     id_atleta = id[0]
    #     actualizar_formulas_digitales_en_masa(id_atleta)
    #
    # print 'listo papa'



    app.MainLoop()
