# """
# name: Dablos defaults
# version: 14.0.1.0.0
# Establece varios parámetros default automáticamente
# """

{
    "name": "Dablos Defaults",
    "version": "14.0.1.0.0",
    "summary": """
        Establece varios parámetros default automáticamente
    """,
    "description": """
    """,
    "category": "Uncategorized",
    "author": "Ruben Fortunato",
    "website": "",
    "depends": [
        "generic_defaults",
        # addons DABLOS
        "dablos_product"
    ],
    "data": [
        "data/01-set-dablos.xml",
        # "data/02-cert-dablos.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": "1",
}
