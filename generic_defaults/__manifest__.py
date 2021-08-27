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
        'calendar',
        'contacts',
        'crm',
        'google_drive',
        'hr',
        'l10n_ar',
        'l10n_latam_base',
        'mrp',
        'note',
        'purchase',
        'sale_management',
        'sales_team',
        'stock_account',
        'stock',
# addons 3rd party
        'backend_theme_v14',
#        'base_territory',
        'disable_odoo_online',
##        'fieldservice_account',
##        'fieldservice_activity',
##        'fieldservice_recurring',
##        'fieldservice_timeline',
#        'fieldservice',
        'hide_powered_by_and_manage_db',
#        'login_user_detail',
        'mail_outbound_static',
        'partner_contact_in_several_companies',
#        'partner_phone_extension',
        'remove_odoo_enterprise',
        'report_xlsx',
        'rowno_in_tree',
        'web_environment_ribbon',
        'web_responsive',
        'web_timeline',
# addons NUMA básicos
        'numa_currency_bna',
        'numa_exceptions',
        'numa_pricelist',
        'numa_product_currency',
# addons NUMA licalización
        'numa_background_job',
        'numa_payment',
        'numa_country_extended', # ???
        'numa_l10n_ar_base',
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
        # Contabilidad para ODOO Community
        'base_accounting_kit', # Cybrosys Full Accounting Kit
        'dynamic_accounts_report', # Cybrosysy Dynamic Financial Reports
        'numa_physical_product',
        'numa_account_community',
        # Sin dependencias
        'numa_address_extended', # ???
#        'numa_product_serial_number', # da error api multi
        'numa_periodic_services',
        'numa_product_multi_category',
        'numa_product_variant',
        'numa_synch',
    ],
    'data': [
        'data/01-generic-defaults.xml',
        'data/02-cert-homo.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': '1',
}
