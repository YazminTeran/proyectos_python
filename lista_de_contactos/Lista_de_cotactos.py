lista_contactos = [
    {
        "nombre_contacto": "Pepito",
        "apellido_contacto": "Perez",
        "telefono_contacto": "3158357923"
    },
    {
        "nombre_contacto": "Maria",
        "apellido_contacto": "Lopez",
        "telefono_contacto": "3146509821"
    },
    {
        "nombre_contacto": "Carlos",
        "apellido_contacto": "Gomez",
        "telefono_contacto": "3101234567"
    },
    {
        "nombre_contacto": "Ana",
        "apellido_contacto": "Martinez",
        "telefono_contacto": "3129876543"
    },
    {
        "nombre_contacto": "Juan",
        "apellido_contacto": "Rodriguez",
        "telefono_contacto": "3174443388"
    },
    {
        "nombre_contacto": "Sofia",
        "apellido_contacto": "Fernandez",
        "telefono_contacto": "3007654321"
    },
    {
        "nombre_contacto": "Miguel",
        "apellido_contacto": "Diaz",
        "telefono_contacto": "3195551234"
    },
    {
        "nombre_contacto": "Luis",
        "apellido_contacto": "Hernandez",
        "telefono_contacto": "3109876543"
    }
]


def buscar_contacto(pTelefono):

    for contactos in lista_contactos:
        if pTelefono == contactos["telefono_contacto"]:
            return contactos["nombre_contacto"],contactos["telefono_contacto"]


def llamar_contacto(pTelefono):
    
    contacto_encontrado = buscar_contacto(pTelefono)

    print(f"llamando alcontacto, {contacto_encontrado}")

llamar_contacto("3109876543")