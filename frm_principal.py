# -*- coding: utf-8 -*-
###########################################################################

## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os

import subprocess

import formEAY.constantesCAC.configCAC as configCAC


import formEAY.constantesCAC.imgCAC as imgCAC
#import formEAY.dbaseCAC.dbEaysecurt as  dbEaysecurt

import formEAY.formularios.forms_varios.frm_validarPassword as frm_validarPassword

import formEAY.formularios.forms_cliente.frm_cartaDermatoglifica as frm_cartaDermatoglifica
import formEAY.formularios.forms_huellas.frm_graficar_radares_multiselect as frm_graficar_radares_multiselect

import formEAY.formularios.forms_varios.frm_configuracion as frm_configuracion

IMAGEN_WALLPAPER=imgCAC.Img_formularios.WALLPAPER_CAC

###########################################################################
## Class Principal
###########################################################################

class Principal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DermaSoft V.2.0", pos = wx.DefaultPosition, size = wx.Size( 788,765 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		#wx.SetS  ( wx.minS, wx.DefaultSize )
		self.contador_id_imagenes_detalle_huellas = 8000

		bSizer_panel_accesos_directos = wx.BoxSizer(wx.VERTICAL)

		self.panel_accesos_directos = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.panel_accesos_directos.SetBackgroundColour(wx.Colour(0, 0, 0))

		bSizer4 = wx.BoxSizer(wx.VERTICAL)

		bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer5 = wx.BoxSizer(wx.VERTICAL)

		self.btn_cartaDermatoglifica = wx.Button(self.panel_accesos_directos, wx.ID_ANY, u"Carta Dermatoglifica", wx.DefaultPosition,
									  wx.DefaultSize, 0)
		self.btn_cartaDermatoglifica.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.btn_cartaDermatoglifica.SetForegroundColour(wx.Colour(0, 0, 0))
		self.btn_cartaDermatoglifica.SetBackgroundColour(wx.Colour(255, 255, 0))

		bSizer5.Add(self.btn_cartaDermatoglifica, 0, wx.ALL, 5)


		bSizer3.Add(bSizer5, 1, wx.EXPAND, 5)

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)


		self.btn_deporte = wx.Button(self.panel_accesos_directos, wx.ID_ANY, u"Deporte", wx.DefaultPosition,
									 wx.DefaultSize, 0)
		self.btn_deporte.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.btn_deporte.SetForegroundColour(wx.Colour(0, 0, 0))
		self.btn_deporte.SetBackgroundColour(wx.Colour(255, 173, 9))

		bSizer6.Add(self.btn_deporte, 0, wx.ALL, 5)


		self.btn_captar_huella_normal = wx.Button(self.panel_accesos_directos, wx.ID_ANY, u"Captar Huella", wx.DefaultPosition, wx.DefaultSize, 0)
		self.btn_captar_huella_normal.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.btn_captar_huella_normal.SetForegroundColour(wx.Colour(0, 0, 0))
		self.btn_captar_huella_normal.SetBackgroundColour(wx.Colour(0, 255, 0))

		bSizer6.Add(self.btn_captar_huella_normal, 0, wx.ALL, 5)




		self.btn_confifguracion = wx.Button(self.panel_accesos_directos, wx.ID_ANY, u"Configuración",
											wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.btn_confifguracion.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.btn_confifguracion.SetForegroundColour(wx.Colour(0, 0, 0))
		self.btn_confifguracion.SetBackgroundColour(wx.Colour(128, 255, 255))

		bSizer6.Add(self.btn_confifguracion, 0, wx.ALL, 5)

		bSizer3.Add(bSizer6, 0, wx.EXPAND, 5)

		bSizer4.Add(bSizer3, 0, wx.EXPAND, 5)

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		self.m_bitmap4 = wx.StaticBitmap(self.panel_accesos_directos, wx.ID_ANY,
										 wx.Bitmap(IMAGEN_WALLPAPER,
												   wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.m_bitmap4, 0, wx.ALL, 5)

		bSizer4.Add(bSizer2, 1, wx.EXPAND, 5)

		self.panel_accesos_directos.SetSizer(bSizer4)
		self.panel_accesos_directos.Layout()
		bSizer4.Fit(self.panel_accesos_directos)
		bSizer_panel_accesos_directos.Add(self.panel_accesos_directos, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer_panel_accesos_directos)
		self.Layout()

		self.Centre( wx.BOTH )

		self.Maximize()

		# Connect Events
		self.btn_cartaDermatoglifica.Bind(wx.EVT_BUTTON, self.btn_cartaDermatoglificaOnButtonClick)
		self.btn_captar_huella_normal.Bind(wx.EVT_BUTTON, self.btn_captar_huella_normalOnButtonClick)
		self.btn_confifguracion.Bind(wx.EVT_BUTTON, self.btn_confifguracionOnButtonClick)
		self.btn_deporte.Bind(wx.EVT_BUTTON, self.btn_deporteOnButtonClick)


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class

	def btn_cartaDermatoglificaOnButtonClick( self, event ):

		# frame_validar=frm_validarPassword.ValidarPassword(self, 'Ventas Generales')
		# frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		# frame_validar.Center()
		# frame_validar.Show()

		self.contador_id_imagenes_detalle_huellas += 3000

		frame_cartaDermatoglifica=frm_cartaDermatoglifica.CartaDermatoglifica(self, 0,self.contador_id_imagenes_detalle_huellas)
		frame_cartaDermatoglifica.Center()
		frame_cartaDermatoglifica.Show()
		event.Skip()

	def btn_captar_huella_normalOnButtonClick(self, event):
		dir_captahuella_normal =  configCAC.configuracion('CaptaHuellas', 'normal')

		try:
			subprocess.call(dir_captahuella_normal)
		except:
			wx.MessageBox(u'DermaSoft no detecta el CaptaHuella instalado. Comunicate a Whatsapp: +57-301 227 97 53', u'Atención...', wx.OK | wx.ICON_INFORMATION)
		event.Skip()

	def btn_confifguracionOnButtonClick(self, event):

		# frame_validar=frm_validarPassword.ValidarPassword(self, 'Ventas Generales')
		# frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		# frame_validar.Center()
		# frame_validar.Show()

		frame_configuracion = frm_configuracion.Configuracion(self)
		frame_configuracion.Center()
		frame_configuracion.Show()
		event.Skip()

	def btn_deporteOnButtonClick(self, event):
		#frame_analisis_por_deporte = frm_graficar_radar_filho_por_deporte.Graficar_radar(self, '00.graficas_deporte')
		frame_analisis_por_deporte = frm_graficar_radares_multiselect.Graficar_radar(self, '00.graficas_deporte')
		frame_analisis_por_deporte.Center()
		frame_analisis_por_deporte.Show()
		event.Skip()


	def mnu_salirOnMenuSelection( self, event ):
		event.Skip()

	def mnu_listadoProductosOnMenuSelection( self, event ):
		import formEAY.formularios.forms_inventario.frm_listadoProductos as frm_listadoProductos
		frame_listadoProductos=frm_listadoProductos.ListadoProductos(None, 1,1,1)
		frame_listadoProductos.Center()
		frame_listadoProductos.Show()
		event.Skip()


	def mnu_ventasXDiaOnMenuSelection( self, event ):
		import formEAY.formularios.forms_varios.frm_validarPassword as frm_validarPassword
		frame_validar=frm_validarPassword.ValidarPassword(self, 'Ventas por dia')
		frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		frame_validar.Center()
		frame_validar.Show()
		event.Skip()

	def mnu_historialVentasOnMenuSelection( self, event ):
		frame_validar = frm_validarPassword.ValidarPassword(self, 'Historial Ventas')
		frame_validar.SetWindowStyle(style=wx.STAY_ON_TOP)
		frame_validar.Center()
		frame_validar.Show()
		event.Skip()

	def mnu_carteraPendienteOnMenuSelection( self, event ):
		event.Skip()


	def mnu_reciboCajaOnMenuSelection( self, event ):
		import formEAY.formularios.forms_caja.frm_reciboCaja as frm_reciboCaja
		frame_reciboCaja=frm_reciboCaja.ReciboCaja(None)
		frame_reciboCaja.Center()
		frame_reciboCaja.Show()
		event.Skip()

	def mnu_entradaDineroOnMenuSelection( self, event ):
		import formEAY.formularios.forms_empleado.frm_seleccionarEmpleado as frm_seleccionarEmpleado
		frame_seleccionarEmpleado=frm_seleccionarEmpleado.SeleccionarEmpleado(None)
		frame_seleccionarEmpleado.Center()
		frame_seleccionarEmpleado.Show()
		event.Skip()

	def mnu_salidaDineroOnMenuSelection( self, event ):
		event.Skip()

	def mnu_cuadreCajaMenorOnMenuSelection( self, event ):
		event.Skip()

	def mnu_notaCreditoOnMenuSelection( self, event ):
		import formEAY.formularios.forms_caja.frm_notaCredito as frm_notaCredito
		frame_notaCredito=frm_notaCredito.NotaCredito(None)
		frame_notaCredito.Center()
		frame_notaCredito.Show()
		event.Skip()

	def mnu_notaDebitoOnMenuSelection( self, event ):
		event.Skip()

	def mnu_abonoClienteOnMenuSelection( self, event ):
		import formEAY.formularios.forms_cuentas.frm_abonoCuentaCliente as frm_abonoCuentaCliente
		frame_abonocliente=frm_abonoCuentaCliente.AbonosCuentaClientes(self)
		frame_abonocliente.Center()
		frame_abonocliente.Show()
		event.Skip()


	def mnu_ventaGeneralOnMenuSelection( self, event ):
		import formEAY.formularios.forms_venta.frm_venderProducto as frm_venderProducto
		# frame_validar=frm_validarPassword.ValidarPassword(self, 'Ventas Generales')
		# frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		# frame_validar.Center()
		# frame_validar.Show()

		frame_ventaGeneral=frm_venderProducto.VenderProducto(None, 2)
		frame_ventaGeneral.Center()
		frame_ventaGeneral.SetPosition((10, 60))
		frame_ventaGeneral.Show()

		event.Skip()

	def mnu_trabajosDelDiaOnMenuSelection(self, event):
		frame_validar=frm_validarPassword.ValidarPassword(self, 'Trabajos del dia')
		frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		frame_validar.Center()
		frame_validar.Show()


		# frame_trabajosDelDia = frm_trabajosDelDia.TrabajosDelDia(self)
		# frame_trabajosDelDia.Center()
		# frame_trabajosDelDia.Show()
		event.Skip()


	def mnu_nominaGrupalOnMenuSelection(self, event):
		import formEAY.formularios.forms_nomina.frm_nominaGrupal as frm_nominaGrupal
		frame_nominaGrupal = frm_nominaGrupal.NominaGrupal(self)
		frame_nominaGrupal.Center()
		frame_nominaGrupal.Show()
		event.Skip()

	def mnu_historialNominaOnMenuSelection(self, event):
		event.Skip()

	def mnu_resumenNominaOnMenuSelection(self, event):
		event.Skip()

	def mnu_miNominaOnMenuSelection(self, event):
		import formEAY.formularios.forms_nomina.frm_miNomina as frm_miNomina
		frame_miNomina = frm_miNomina.MiNomina(self)
		frame_miNomina.Center()
		frame_miNomina.Show()
		event.Skip()

	def mnu_nominaSemanalOnMenuSelection(self, event):
		event.Skip()

	def mnu_nominaMensualOnMenuSelection(self, event):
		event.Skip()

	def mnu_prestamosEmpleadosOnMenuSelection(self, event):
		import formEAY.formularios.forms_nomina.frm_prestamosEmpleado as frm_prestamosEmpleado
		frame_prestamosEmpleado = frm_prestamosEmpleado.PrestamosEmpleado(self)
		frame_prestamosEmpleado.Center()
		frame_prestamosEmpleado.Show()
		event.Skip()

	def mnu_abonosEmpleadosOnMenuSelection(self, event):
		import formEAY.formularios.forms_nomina.frm_abonosPrestamosEmpleados as frm_abonosPrestamosEmpleados
		frame_abonosPrestamosEmpleado = frm_abonosPrestamosEmpleados.AbonosPrestamosEmpleado(self)
		frame_abonosPrestamosEmpleado.Center()
		frame_abonosPrestamosEmpleado.Show()
		event.Skip()



	def mnu_nuevoProductoOnMenuSelection( self, event ):
		import formEAY.formularios.forms_producto.frm_nuevoProducto as  frm_nuevoProducto
		frame_nuevoProducto=frm_nuevoProducto.NuevoProducto(self,'Nuevo Producto', 2)
		frame_nuevoProducto.Center()
		frame_nuevoProducto.Show()
		event.Skip()

	def mnu_deshabilitarProductoOnMenuSelection( self, event ):
		frame_validar=frm_validarPassword.ValidarPassword(self, 'Deshabilitar Productos')
		frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		frame_validar.Center()
		frame_validar.Show()
		event.Skip()


	def mnu_habilitarProductoOnMenuSelection( self, event ):
		frame_validar=frm_validarPassword.ValidarPassword(self, 'Habilitar Productos')
		frame_validar.SetWindowStyle( style=wx.STAY_ON_TOP )
		frame_validar.Center()
		frame_validar.Show()
		event.Skip()


	def mnu_tipoProductoOnMenuSelection( self, event ):
		import formEAY.formularios.forms_producto.frm_gestionarTipoProducto as frm_gestionarTipoProducto
		frame_gestionarTipoProducto=frm_gestionarTipoProducto.GestionarTipoProducto(self)
		frame_gestionarTipoProducto.Center()
		frame_gestionarTipoProducto.Show()
		event.Skip()

	def mnu_categoriaProductoOnMenuSelection( self, event ):
		import formEAY.formularios.forms_producto.frm_gestionarCategoria as  frm_gestionarCategoria
		frame_gestionarCategoria=frm_gestionarCategoria.GestionarCategoria(self)
		frame_gestionarCategoria.Center()
		frame_gestionarCategoria.Show()
		event.Skip()

	def mnu_entradaMercanciaOnMenuSelection( self, event ):
		import formEAY.formularios.forms_inventario.frm_entradaMercancia as frm_entradaMercancia
		frame_entradaMercancia=frm_entradaMercancia.EntradaMercancia(self)
		frame_entradaMercancia.Center()
		frame_entradaMercancia.Show()
		event.Skip()

	def mnu_movimientoDeStockOnMenuSelection( self, event ):
		import formEAY.formularios.forms_inventario.frm_movimientoDeStock as frm_movimientoDeStock
		frame_movimientoDeStock=frm_movimientoDeStock.MovimientoDeStock(None)
		frame_movimientoDeStock.Center()
		frame_movimientoDeStock.Show()
		event.Skip()

	def mnu_devolucionPorVentaOnMenuSelection( self, event ):
		import formEAY.formularios.forms_producto.frm_modificacionesDirectas as frm_modificacionesDirectas
		#temporalmente para frm_modificacionesDirectas
		frame_modificacionesDirectas=frm_modificacionesDirectas.ModificacionesDirectas(None)
		#frame_modificacionesDirectas.SetWindowStyle( style=wx.STAY_ON_TOP )
		frame_modificacionesDirectas.Center()
		frame_modificacionesDirectas.Show()
		event.Skip()

	# def mnu_devolucionPorcomprasOnMenuSelection( self, event ):
	# 	event.Skip()

	def mnu_acercaDeOnMenuSelection( self, event ):
		event.Skip()

	def mnu_nueva_fraganciaOnMenuSelection(self, event):
		event.Skip()

	def mnu_stock_fraganciasOnMenuSelection(self, event):
		import formEAY.formularios.forms_perfumes.frm_stock_fragancias as frm_stock_fragancias
		frame_stock_fragancias = frm_stock_fragancias.Stock_fragancias(self)
		frame_stock_fragancias.Center()
		frame_stock_fragancias.Show()
		event.Skip()

	def btn_deshabilitarProductoOnButtonClick( self, event ):
		event.Skip()


	def func_rtaValidarUsuario(self, nombreFormulario, id_usuario):

		if nombreFormulario == 'Historial Ventas':
			import formEAY.formularios.forms_reportes.frm_historial_ventas as frm_historial_ventas
			frame_historial_ventas = frm_historial_ventas.Historial_de_ventas(self)
			frame_historial_ventas.Center()
			frame_historial_ventas.Show()

		if nombreFormulario == 'Dash':
			import formEAY.formularios.forms_varios.frm_dash_menu as frm_dash_menu
			frame_dash_menu = frm_dash_menu.Dash_menu(self)
			frame_dash_menu.Center()
			frame_dash_menu.Show()






if __name__ == '__main__':
	app=wx.App()

	frame_principal=Principal(None)
	frame_principal.Center()
	frame_principal.Show()

	app.MainLoop()
