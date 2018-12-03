# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.agw.pygauge as PG

import formEAY.funcEAY.func_huellas as func_huellas

COLOR_BARRA = wx.Colour(66, 160, 255)
COLOR_BARRA_90 = wx.RED
COLOR_BARRA_65 = wx.Colour(233, 124, 88)

###########################################################################
## Class Resultados
###########################################################################

class Resultados(wx.Frame):

    def __init__(self, parent, a, l, w, sqtl):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Resultados", pos=wx.DefaultPosition,
                          size=wx.Size(484, 490), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(484, 490), wx.Size(484, 490))

        self.a=a
        self.l=l
        self.w=w
        self.sqtl=sqtl

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel4.SetBackgroundColour(wx.Colour(208, 208, 208))

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel5.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Resultados", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        bSizer20.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer20.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer19.Add(bSizer20, 0, wx.EXPAND, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Arco (A):", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer21.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.lbl_a = wx.StaticText(self.m_panel5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_a.Wrap(-1)
        self.lbl_a.SetFont(wx.Font(13, 70, 90, 92, False, wx.EmptyString))
        self.lbl_a.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer21.Add(self.lbl_a, 0, wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Presilla (L):", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)
        self.m_staticText101.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer21.Add(self.m_staticText101, 0, wx.ALL, 5)

        self.lbl_l = wx.StaticText(self.m_panel5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_l.Wrap(-1)
        self.lbl_l.SetFont(wx.Font(13, 70, 90, 92, False, wx.EmptyString))
        self.lbl_l.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer21.Add(self.lbl_l, 0, wx.ALL, 5)

        self.m_staticText102 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Verticilo (W):", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText102.Wrap(-1)
        self.m_staticText102.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer21.Add(self.m_staticText102, 0, wx.ALL, 5)

        self.lbl_w = wx.StaticText(self.m_panel5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_w.Wrap(-1)
        self.lbl_w.SetFont(wx.Font(13, 70, 90, 92, False, wx.EmptyString))
        self.lbl_w.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer21.Add(self.lbl_w, 0, wx.ALL, 5)

        self.m_staticText1021 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"SQTL:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1021.Wrap(-1)
        self.m_staticText1021.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer21.Add(self.m_staticText1021, 0, wx.ALL, 5)

        self.lbl_sqtl = wx.StaticText(self.m_panel5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_sqtl.Wrap(-1)
        self.lbl_sqtl.SetFont(wx.Font(14, 70, 90, 92, False, wx.EmptyString))
        self.lbl_sqtl.SetForegroundColour(wx.Colour(0, 0, 255))

        bSizer21.Add(self.lbl_sqtl, 0, wx.ALL, 5)

        bSizer19.Add(bSizer21, 1, wx.EXPAND, 5)

        self.m_panel5.SetSizer(bSizer19)
        self.m_panel5.Layout()
        bSizer19.Fit(self.m_panel5)
        bSizer16.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        bSizer15.Add(bSizer16, 0, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel6.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        bSizer24 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText103 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Formula Digital:", wx.DefaultPosition,
                                             wx.Size(135, -1), wx.ALIGN_RIGHT)
        self.m_staticText103.Wrap(-1)
        self.m_staticText103.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer24.Add(self.m_staticText103, 0, wx.ALL, 5)

        self.lbl_formula = wx.StaticText(self.m_panel6, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_formula.Wrap(-1)
        self.lbl_formula.SetFont(wx.Font(13, 70, 90, 92, False, wx.EmptyString))
        self.lbl_formula.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer24.Add(self.lbl_formula, 0, wx.ALL, 5)

        bSizer25.Add(bSizer24, 0, wx.EXPAND, 5)

        bSizer241 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1031 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Sistema Energetico:", wx.DefaultPosition,
                                              wx.Size(135, -1), wx.ALIGN_RIGHT)
        self.m_staticText1031.Wrap(-1)
        self.m_staticText1031.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))

        bSizer241.Add(self.m_staticText1031, 0, wx.ALL, 5)

        self.lbl_sistema_energetico = wx.StaticText(self.m_panel6, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize,
                                                    0)
        self.lbl_sistema_energetico.Wrap(-1)
        self.lbl_sistema_energetico.SetFont(wx.Font(13, 70, 90, 92, False, wx.EmptyString))
        self.lbl_sistema_energetico.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer241.Add(self.lbl_sistema_energetico, 0, wx.ALL, 5)

        bSizer25.Add(bSizer241, 0, wx.EXPAND, 5)

        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.etq_f = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Fuerza:", wx.DefaultPosition, wx.Size(90, -1),
                                   wx.ALIGN_RIGHT)
        self.etq_f.Wrap(-1)
        self.etq_f.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer33.Add(self.etq_f, 0, wx.ALL, 5)

        self.gauge_f = PG.PyGauge(self.m_panel6, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_f.SetValue(0)
        #self.gauge_f.SetDrawValue(draw=True, drawPercent=False, font=None, colour=wx.BLACK, formatString=None)
        self.gauge_f.SetBarColor(colour=COLOR_BARRA)
        self.gauge_f.SetMinSize(wx.Size(200, 20))

        bSizer33.Add(self.gauge_f, 0, wx.ALL, 5)

        bSizer32.Add(bSizer33, 0, wx.EXPAND, 5)

        bSizer331 = wx.BoxSizer(wx.HORIZONTAL)

        self.etq_p = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Potencia:", wx.DefaultPosition, wx.Size(90, -1),
                                   wx.ALIGN_RIGHT)
        self.etq_p.Wrap(-1)
        self.etq_p.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer331.Add(self.etq_p, 0, wx.ALL, 5)

        self.gauge_p = PG.PyGauge(self.m_panel6, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_p.SetValue(0)
        self.gauge_p.SetBarColor(colour=COLOR_BARRA)
        self.gauge_p.SetMinSize(wx.Size(200, 20))

        bSizer331.Add(self.gauge_p, 0, wx.ALL, 5)

        bSizer32.Add(bSizer331, 0, wx.EXPAND, 5)

        bSizer332 = wx.BoxSizer(wx.HORIZONTAL)

        self.etq_v = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Velocidad:", wx.DefaultPosition, wx.Size(90, -1),
                                   wx.ALIGN_RIGHT)
        self.etq_v.Wrap(-1)
        self.etq_v.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer332.Add(self.etq_v, 0, wx.ALL, 5)

        self.gauge_v = PG.PyGauge(self.m_panel6, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_v.SetValue(0)
        self.gauge_v.SetBarColor(colour=COLOR_BARRA)
        self.gauge_v.SetMinSize(wx.Size(200, 20))

        bSizer332.Add(self.gauge_v, 0, wx.ALL, 5)

        bSizer32.Add(bSizer332, 0, wx.EXPAND, 5)

        bSizer333 = wx.BoxSizer(wx.HORIZONTAL)

        self.etq_c = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Coordinación:", wx.DefaultPosition, wx.Size(90, -1),
                                   wx.ALIGN_RIGHT)
        self.etq_c.Wrap(-1)
        self.etq_c.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer333.Add(self.etq_c, 0, wx.ALL, 5)

        self.gauge_c = PG.PyGauge(self.m_panel6, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_c.SetValue(0)
        self.gauge_c.SetBarColor(colour=COLOR_BARRA)
        self.gauge_c.SetMinSize(wx.Size(200, 20))

        bSizer333.Add(self.gauge_c, 0, wx.ALL, 5)

        bSizer32.Add(bSizer333, 0, wx.EXPAND, 5)

        bSizer334 = wx.BoxSizer(wx.HORIZONTAL)

        self.etq_r = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Resistencia:", wx.DefaultPosition, wx.Size(90, -1),
                                   wx.ALIGN_RIGHT)
        self.etq_r.Wrap(-1)
        self.etq_r.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer334.Add(self.etq_r, 0, wx.ALL, 5)

        self.gauge_r = PG.PyGauge(self.m_panel6, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge_r.SetValue(0)
        self.gauge_r.SetBarColor(colour=COLOR_BARRA)
        self.gauge_r.SetMinSize(wx.Size(200, 20))

        bSizer334.Add(self.gauge_r, 0, wx.ALL, 5)

        bSizer32.Add(bSizer334, 0, wx.EXPAND, 5)

        bSizer25.Add(bSizer32, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        self.txt_detalle = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 130),
                                       wx.TE_MULTILINE)
        self.txt_detalle.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        self.txt_detalle.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer31.Add(self.txt_detalle, 0, wx.ALL | wx.EXPAND, 5)

        bSizer25.Add(bSizer31, 0, wx.EXPAND, 5)

        self.m_panel6.SetSizer(bSizer25)
        self.m_panel6.Layout()
        bSizer25.Fit(self.m_panel6)
        bSizer17.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        bSizer15.Add(bSizer17, 1, wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer15)
        self.m_panel4.Layout()
        bSizer15.Fit(self.m_panel4)
        bSizer14.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer14)

### INICIALIZAR VALORESS EAY
        self.cargar_datos()

        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def cargar_datos(self):

        if self.a == 10:
            self.sqtl=0

        self.lbl_a.SetLabel(str(self.a))
        self.lbl_l.SetLabel(str(self.l))
        self.lbl_w.SetLabel(str(self.w))
        self.lbl_sqtl.SetLabel(str(self.sqtl))

        fuerza, potencia, velocidad, coordinacion, resistencia, formula, energia, tendencia, componente, nivel = func_huellas.get_detalle_firma_para_laudo(self.a, self.l, self.w, self.sqtl)

        detalle_nivel = func_huellas.get_detalle_por_nivel(nivel, energia)

        self.lbl_formula.SetLabel(formula)
        self.lbl_sistema_energetico.SetLabel(energia)



        if fuerza >= 85:
            self.gauge_f.SetBarColor(colour=COLOR_BARRA_90)
        if potencia >= 85:
            self.gauge_p.SetBarColor(colour=COLOR_BARRA_90)
        if velocidad >= 85:
            self.gauge_v.SetBarColor(colour=COLOR_BARRA_90)
        if coordinacion >= 85:
            self.gauge_c.SetBarColor(colour=COLOR_BARRA_90)
        if resistencia >= 85:
            self.gauge_r.SetBarColor(colour=COLOR_BARRA_90)


        if fuerza >= 65 and  fuerza < 85:
            self.gauge_f.SetBarColor(colour=COLOR_BARRA_65)
        if potencia >= 65 and  potencia < 85:
            self.gauge_p.SetBarColor(colour=COLOR_BARRA_65)
        if velocidad >= 65 and  velocidad < 85:
            self.gauge_v.SetBarColor(colour=COLOR_BARRA_65)
        if coordinacion >= 65 and  coordinacion < 85:
            self.gauge_c.SetBarColor(colour=COLOR_BARRA_65)
        if resistencia >= 65 and  resistencia < 85:
            self.gauge_r.SetBarColor(colour=COLOR_BARRA_65)

        self.gauge_f.SetValue(fuerza)
        self.gauge_p.SetValue(potencia)
        self.gauge_v.SetValue(velocidad)
        self.gauge_c.SetValue(coordinacion)
        self.gauge_r.SetValue(resistencia)

        self.txt_detalle.SetValue(detalle_nivel)



