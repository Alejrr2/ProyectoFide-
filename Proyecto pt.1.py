#Proyecto Programación
import random
montoacobrar=0

#Ingreso de datos para registrar al usuario
print ("Bienvenidx a ENTREGAS MEX, para registrarse como usuario de nuestro servicio, por favor ingrese los siguientes datos:")
correocomercio= input("Ingrese el correo electrónico del comercio: ") #Almacena el correo del comercio
nombrecomercio= input("Ingrese el nombre del comercio: ")#Almacena el nombre del comercio
telefonocomercio= input("Ingrese el número de teléfono del comercio: ") #Almacena el número de teléfono del comercio
dueñocomercio= input("Ingrese el nombre de la persona dueña del comercio: ") #Almacena el nombre de la persona dueña del comercio
ubicacioncomercio= input("Ingrese la ubicación del comercio: ") #Almacena la ubicación del comercio

#Ingreso de datos para registrar una factura electrónica y crear un paquete
facturaelectronica=int(input("Hola de nuevo, por favor ingrese 1 si desea generar una factura electrónica O 2 si desea continuar con el registro del paquete: "))
if facturaelectronica==1:
    tipoDeCedula= input ("Ingrese el tipo de cedula: ")
    numeroDeCedula= input ("Ingrese el numero de cedula: ") #almacena el numero de cedula para la facturacion 
    nombreRegistrado= input ("Ingrese el nombre que desea imprimir en la factura: ") #almacena el nombre con el que fue registrado 
    telefono= input ("Ingrese un numero de telefono para su facturacion: ") #almacena el telefono para la facturacion 
    correo= input ("Ingrese un correo para su facturacion: ") #almacena el correo respectivo para la facturacion
    provincia= input ("Provincia destino:") #almacena la provincia para la facturacion 
    canton= input ("Canton destino: ") #almacena el canton para la facturacion 
    distrito= input ("Distrito destino: ") #almacena el distrito para la facturacion 

    print ("Los siguientes datos son requeridos para la creación de los paquetes:")
    nombredestinatario=input("Ingrese el nombre del destinario: ")
    telefonodestinatario= input("Ingrese el numero de telefono del destinario: ")
    ceduladestinario= input("Ingrese el numero de cedula del destinario: ")
    pesopaquete= input("Ingrese el peso en kilogramos del paquete: ")
    pagocontraentrega= int(input("Digite 1 si desea la opción de *Pago Contra Entrega*: "))
    if pagocontraentrega==1:
        montoacobrar=int(input("Ingrese el monto a cobrar a la hora de realizar la entrega: "))

#Ingreso de datos para creación de paquetes solamente
if facturaelectronica==2:
    print ("Los siguientes datos son requeridos para la creación de los paquetes:")
    nombredestinatario=input("Ingrese el nombre del destinario: ")
    telefonodestinatario= input("Ingrese el numero de telefono del destinario: ")
    ceduladestinario= input("Ingrese el numero de cedula del destinario: ")
    pesopaquete= input("Ingrese el peso en kilogramos del paquete: ")
    pagocontraentrega= int(input("Digite 1 si desea la opción de *Pago Contra Entrega*: "))
    if pagocontraentrega==1:
        montoacobrar=int(input("Ingrese el monto a cobrar a la hora de realizar la entrega: "))                            

#Creación de Guías 
    tracking=0
    opcion=int(input("Ingrese 1 para desglosar la información de su guía: "))
    while opcion==1:
        print("Información de Guía")
        print("*Número de Guía:", tracking,"*")
        tracking=tracking+1
        print("-Infromación de Comercio: \n","Nombre del Comercio: ",nombrecomercio,"\n","Telefono: ",telefonocomercio,"\n")
        print("-Información del Destinatario: \n","Nombre: ",nombredestinatario,"\n","Teléfono: ",telefonodestinatario)
        #Si requiere cobro
        if pagocontraentrega==1:
            print("Su monto a pagar es de: ",montoacobrar)
        break

#Cambio de estados del paquete

estado= int(input("Ingrese el nuevo estado del paquete"  
                   " 1=Creado" 
                   " 2=Recolectado" 
                   " 3=Entrega fallida" 
                   " 4=Entregado"))
if estado==1:
    print("El estado del paquete es: Creado")
elif estado==2:
    print("El estado del paquete es: Recolectado")
elif estado==3:
    print("El estado del paquete es: Entrega fallida")
elif estado==4:
    print("El estado del paquete es: Entregado")
#Rastreo de los paquetes
numerodeguia=input("introduzca el numero de guia")
if numerodeguia != 88769017460863418:
    if estado != 0:
        print("¿desea realizar algun cambio en su estado de paquetes?")
        print("1. Si")
        print("2. No")
        opcion2=int(input("seleccione una opcion"))
        if opcion2 ==1:
            estado= int(input("Ingrese el nuevo estado del paquete"  
                   " 1=Creado" 
                   " 2=Recolectado" 
                   " 3=Entrega fallida" 
                   " 4=Entregado"))
            if estado==1:
                print("El estado del paquete es: Creado")
            elif estado==2:
                print("El estado del paquete es: Recolectado")
            elif estado==3:
                print("El estado del paquete es: Entrega fallida")
            elif estado==4:
                print("El estado del paquete es: Entregado")
        print("gracias por confirmar sus cambios")
        if opcion2==2:
            print("gracias por confirmar sus cambios")
