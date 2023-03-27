#Proyecto Programación



#Ingreso de datos para registrar al usuario
print ("Bienvenidx a ENTREGAS MEX, para registrarse como usuario de nuestro servicio, por favor ingrese los siguientes datos:")
correocomercio= input("Ingrese el correo electrónico del comercio: ") #Almacena el correo del comercio
telefonocomercio= int(input("Ingrese el número de teléfono del comercio: ")) #Almacena el número de teléfono del comercio
dueñocomercio= input("Ingrese el nombre de la persona dueña del comercio: ") #Almacena el nombre de la persona dueña del comercio
ubicacioncomercio= input("Ingrese la ubicación del comercio: ") #Almacena la ubicación del comercio

#Ingreso de datos para registrar una factura electrónica
print ("Hola de nuevo, por favor ingrese los datos para su factura electronica")
tipoDeCedula= input ("Ingrese el tipo de cedula:")
numeroDeCedula= input ("Ingrese su numero de cedula:") #almacena el numero de cedula para la facturacion nombreRegistrado= input ("Ingrese el nombre con el que se registro:") #almacena el nombre con el que fue registrado telefono= input ('Ingrese el numero de telefono para su facturacion:") #almacena el telefono para la facturacion correo= input ("Ingrese el correo para su facturacion:") #almacena el correo respectivo para la facturacion
provincia= input ("Provincia:") #almacena la provincia para la facturacion 
canton= input ("Canton: ") #almacena el canton para la facturacion
distrito= input ("Distrito:") #almacena el distrito para la facturacion 



#Ingreso de datos para creación de paquetes
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
    