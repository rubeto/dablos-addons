# -*- coding: utf-8 -*-

{
    'name': "Generic defaults",
    'version': '14.0.1.0.0',
    'summary': """
        - Carga módulos básicos
        - Establece varios parámetros default automáticamente
    """,
    'description': """
    """,
    'category': 'Uncategorized',
    'author': "",
    'website': "",
    'depends': [
# addons ODOO
        'account',
        'base',
        'base_automation',
        'calendar',
        'contacts',
        'crm',
        'google_drive',
        'hr',
        'l10n_ar',
        'l10n_latam_base',
        'mrp',
        'note',
        'project',
        'purchase',
        'sale_management',
        'sales_team',
        'stock_account',
        'stock',
# addons 3rd party
        'backend_theme_v14',
#        'base_territory',
        'delivery_carrier_partner',
        'disable_odoo_online',
##        'fieldservice_account',
##        'fieldservice_activity',
##        'fieldservice_recurring',
##        'fieldservice_timeline',
#        'fieldservice',
        'hide_powered_by_and_manage_db',
#        'login_user_detail',
        'mail_outbound_static',
        'mail_restrict_follower_selection',
#        'mail_tracking',
        'partner_contact_in_several_companies',
#        'partner_phone_extension',
        'purchase_order_line_price_history',
        'remove_odoo_enterprise',
        'report_xlsx',
        'rowno_in_tree',
        'sale_commission',
        'sale_order_line_price_history',
#        'sale_stock_mto_as_mts_orderpoint',
        'stock_available',
        'stock_mts_mto_rule',
#        'stock_picking_purchase_order_link',
#        'stock_picking_sale_order_link',
        'web_environment_ribbon',
        'web_responsive',
        'web_timeline',
        'base_remote',
        'base_report_to_printer',
#        'remote_report_to_printer',
        'base_user_role',
        'base_user_role_company',
# addons NUMA básicos
        'numa_currency_bna',
        'numa_exceptions',
        'numa_pricelist',
        'numa_product_currency',
# addons NUMA licalización
        'numa_account_community',
        'numa_account_extended',
        'numa_background_job',
        'numa_country_extended',
        'numa_l10n_ar_base',
        'numa_payment',
        # AFIP web services
        'numa_l10n_ar_afipws',
        'numa_l10n_ar_afipws_wscdc',
        'numa_l10n_ar_afipws_padron',
        # AFIP factura electrónica
        'numa_l10n_ar_afipws_fe',
        'numa_l10n_ar_afipws_fex',
        # Agentes de retención
        'numa_l10n_ar_agip', # CABA
        'numa_l10n_ar_arba', # Buenos Aires
        'numa_l10n_ar_ater', # Entre Ríos
        'numa_l10n_ar_atm_misiones', # Misiones
        # Contabilidad para ODOO Community
        'base_accounting_kit', # Cybrosys Full Accounting Kit
        'dynamic_accounts_report', # Cybrosysy Dynamic Financial Reports
        'numa_physical_product',
        # Sin dependencias
        'numa_address_extended',
        'numa_invoice_from_delivery_order_physical_product',
        'numa_invoice_from_delivery_order',
        'numa_l10n_ar_bank_statement_import',
        'numa_periodic_services',
        'numa_product_multi_category',
#        'numa_product_serial_number',
        'numa_product_variant',
        'numa_synch',
    ],
    'data': [
        'data/01-generic-defaults.xml',
        'data/02-cert-homo.xml',
        'data/afip.tipos.documentos.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': '1',
    'pre_init_hook': 'generic_pre_init_hook',
}
