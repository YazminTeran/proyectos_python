# hacer una agenda que permita agregar un conacto, buscar un contacto
# eliminar un contacto y editar un contacto y salir

lista_contactos= []

# ****************************  funcionaldades*********************
def agregar_contacto(pNombre, pTelefono):
    # crear objeto
    objeto_contacto = {
        "nombre_contacto": pNombre,
        "telefono_contacto": pTelefono
    }

    lista_contactos.append(objeto_contacto)

#++++++++++++++++++++++++++++++++++++++++++++++++
def obtener_todos_contactos(lista_contactos):
    
    for contactos in lista_contactos:
        return contactos
    
    

#++++++++++++++++++++++++++++++++++++++++++++++++
def buscar_contactos():

    for pNombre in lista_contactos :
        return pNombre

#*****************************************************************************************








opcion_salir= 0
while opcion_salir != 6:
    print("1 - Agregar")
    print("2 - listar")
    print("3 - Buscar")
    print("4 - Eliminar")
    print("5 - Editar ")
    print("6 - Salir ")

    opcion_usuario=int(input("ingresar opcion: "))
    opcion_salir = opcion_usuario

    if opcion_usuario == 1 :
        print("*****opcion Agregar contacto ******")
        nombre_contacto = input("ingresar nombre contacto:  ")
        numero_contacto = int(input("ingresar numero contacto:  "))
        agregar_contacto(nombre_contacto, numero_contacto)
        
    
    if opcion_usuario == 2:
        print("*******opcion listar *******")
        lista = input(lista_contactos)
        obtener_todos_contactos(lista_contactos)
        
        
        


    if opcion_usuario == 3:
        print("******* Buscar contacto*******")
        buscar = input("ingresar nombre : ")
        print(f"el numero de {buscar}, es {numero_contacto}")
   











