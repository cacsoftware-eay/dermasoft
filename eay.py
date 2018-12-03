#!/usr/bin/env python

# -*- coding: utf-8 -*-
###########################################################################
import wx

import frm_principal as pp
import formEAY.dbaseCAC.dbClientes as dbClientes


# def actualizar_formulas_digitales_en_masa(el_id_atleta):
#
#
#
#     dic_datos = dbClientes.cargar_atleta_id_datos_dermatoglifia(id_atleta)
#
#     rta = dbClientes.guardar_analisis_de_huellas(dic_datos, id_atleta)


if __name__ == '__main__':
    app=wx.App()

    frame_principal=pp.Principal(None)
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