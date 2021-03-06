# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "eInvoice",
    "version" : "2.0",
    "author" : "Econube - pablo.cabezas@econube.cl, jose.pinto@econube.cl",
    "website" : "www.econube.cl",
    "category" : "Econube",
    "description": """
    --Facturacion Electronica--
    *Para Firmado e envio de documentos tener instalado libreria facturisa con las siguientes rutas:
            base : /home/openerp/lfubu14_64 \n
            folios: /home/openerp/caf/  \n
            certificados : /home/openerp/certificados/ \n      
    **directorio de firmas
        /home/openerp/lfubu14_64/out/dte_otros
        /home/openerp/lfubu14_64/out/dte_sii
        /home/openerp/lfubu14_64/out/resp_sii
        /home/openerp/lfubu14_64/out/dte_setprueba

    *Todas las rutas deben tener los permisos para el usuario openerp \n 
    
    *Para recepcion de correos configurar un usuario con dominio econube(primero configurar correo) ejemplo:
            usuario sii correo : True \n
            email:dte@econube.cl  \n
            alias:dte@econube.cl \n                
            servidor con parametros: \n
            servidor : just150.justhost.com \n
            puerto:995 \n
            ssl/tls : True \n
            usuario : dte@econube.cl \n
            pass : dte2015 \n
            accion del srvidor : \n  
               Nombre accion: mail_enter \n
               objeto : Mensaje \n
               tipo accion : python \n     
               condicion : True \n
               secuencia :1 \n
               codigo python : self.mail_enter(cr, uid, object, context) \n
               
        Solucion Error:
            Se debe a un error en libxmlsec , por lo que se debe descargar la version que trae utopic (ubuntu 14.10),
            poniendo al final de /etc/apt/sources.list lo siguiente:
            
            deb http://us.archive.ubuntu.com/ubuntu wily main universe
            
            Despues ejecutar
            
            aptitude update
            aptitude install xmlsec1
        
                    """,
    "depends" : ['base','account','base_vat','product','stock','l10n_cl_toponyms'],
	"data": [
            'workflow/workflow.xml',            
            'views/menu_facturacion_dte.xml',
            'views/default_account_dte.xml',            
            'views/account_invoice_folios.xml',                
            'views/account_config_firma.xml',
            'views/account_journal_code.xml',
            'views/account_invoice_emitidos.xml',
            'views/account_invoice_dte.xml',
            'views/view_company.xml',
            'views/product_product_view.xml',
            'views/cpcs_view.xml',
            'views/cron_monitor_documentos.xml',
            'views/res_users_view.xml',
            'views/account_invoice.xml',
            'views/stock_picking_view.xml',
            'views/wizard_buscar_correo.xml',            
	        'views/librossii.xml',
            'views/accounts_views.xml',
    ],
    "update_xml" : [],
    "installable": True,
	"active": False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:#