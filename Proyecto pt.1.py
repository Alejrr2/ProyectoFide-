#Proyecto Programación
cantidaddeEnvios=0
montoacobrar=0
nombrecomercio=0
telefonocomercio=0
pagocontraentrega=0
nombredestinatario=0
telefonodestinatario=0
ceduladestinario=0
cantidadxTelefono=[]
cantidadxCedula=[]
guia=[]

#<<<REGISTRO DE USUARIO>>>

#Se crea el archivo
def crearArchivoUsuario():
    file=open("registroUsuario.txt","w")
    print("Bienvenidx a ENTREGAS MEX, para registrarse como usuario de nuestro servicio, por favor ingrese los siguientes datos:")
    file.close()
    
#Ingreso de datos para registrar al usuario
def registrarUsuario():
    global nombrecomercio
    global telefonocomercio
    correocomercio= input("Ingrese el correo electrónico del comercio: ") #Almacena el correo del comercio
    nombrecomercio= input("Ingrese el nombre del comercio: ")#Almacena el nombre del comercio
    telefonocomercio= input("Ingrese el número de teléfono del comercio: ") #Almacena el número de teléfono del comercio
    dueñocomercio= input("Ingrese el nombre de la persona dueña del comercio: ") #Almacena el nombre de la persona dueña del comercio
    ubicacioncomercio= input("Ingrese la ubicación del comercio: ") #Almacena la ubicación del comercio
    file=open("registroUsuario.txt","a")
    file.write(correocomercio)
    file.write("\n")
    file.write(nombrecomercio)
    file.write("\n")
    file.write(telefonocomercio)
    file.write("\n")
    file.write(dueñocomercio)
    file.write("\n")
    file.write(ubicacioncomercio)
    file.write("\n")
    print("\nEl ususario fue registrado correctamente!")
    file.close()

#Se muestra la información almacenada en el archivo
def mostrarInformacionUsuario():
    file=open("registroUsuario","r")
    mensaje=file.read()
    print(mensaje)
    file.close()

#<<<REGISTRO DE FACTURA ELECTRÓNICA>>>
    
#Se crea el archivo  
def crearArchivoFactura():
    file=open("registroUsuario.txt","w")
    print("Bienvenidx a ENTREGAS MEX, para crear una factura electronica, por favor ingrese los siguientes datos:")
    file.close()
    
#Ingreso de datos para registrar una factura electrónica
def registrarFactura():
    tipoDeCedula= input ("Ingrese el tipo de cedula: ")
    numeroDeCedula= input ("Ingrese el numero de cedula: ") #almacena el numero de cedula para la facturacion 
    nombreRegistrado= input ("Ingrese el nombre que desea imprimir en la factura: ") #almacena el nombre con el que fue registrado 
    telefono= input ("Ingrese un numero de telefono para su facturacion: ") #almacena el telefono para la facturacion 
    correo= input ("Ingrese un correo para su facturacion: ") #almacena el correo respectivo para la facturacion
    provincia= input ("Provincia destino:") #almacena la provincia para la facturacion 
    canton= input ("Canton destino: ") #almacena el canton para la facturacion 
    distrito= input ("Distrito destino: ") #almacena el distrito para la facturacion
    file=open("registroFacturaElectronica.txt","a")
    file.write(tipoDeCedula)
    file.write("\n")
    file.write(numeroDeCedula)
    file.write("\n")
    file.write(nombreRegistrado)
    file.write("\n")
    file.write(telefono)
    file.write("\n")
    file.write(correo)
    file.write("\n")
    file.write(provincia)
    file.write("\n")
    file.write(canton)
    file.write("\n")
    file.write(distrito)
    file.write("\n")
    print("\nLa factura fue registrada correctamente!")
    file.close()

#Se muestra la información almacenada en el archivo
def mostrarInformacionFactura():
    file=open("registroFacturaElectronica","r")
    mensaje=file.read()
    print(mensaje)
    file.close()

#<<<CREACIÓN DE PAQUETE>>>
    
#Se crea el archivo  
def crearArchivoPaquete():
    file=open("registroPaquete.txt","w")
    print("Bienvenidx a ENTREGAS MEX, para crear un paquete, por favor ingrese los siguientes datos:")
    file.close()
    
#Ingreso de datos para creación de paquetes solamente
def crearPaquete():
    global nombredestinatario
    global telefonodestinatario
    global montoacobrar
    global pagocontraentrega
    global cantidaddeEnvios
    global ceduladestinario
    
    nombredestinatario=input("Ingrese el nombre del destinario: ")
    telefonodestinatario= input("Ingrese el numero de telefono del destinario: ")
    cantidadxTelefono.append(telefonodestinatario)
    ceduladestinario= input("Ingrese el numero de cedula del destinario: ")
    cantidadxCedula.append(ceduladestinario)
    pesopaquete= input("Ingrese el peso en kilogramos del paquete: ")
    file=open("registroPaquete.txt","a")
    file.write(nombredestinatario)
    file.write("\n")
    file.write(telefonodestinatario)
    file.write("\n")
    file.write(ceduladestinario)
    file.write("\n")
    file.write(pesopaquete)
    file.write("\n")
    pagocontraentrega= int(input("Digite 1 si desea la opción de *Pago Contra Entrega* o 2 si desea continuar: "))
    if pagocontraentrega==1:
        montoacobrar=str(input("Ingrese el monto a cobrar a la hora de realizar la entrega: "))
        file.write(montoacobrar)
        file.write("\n")
        cantidaddeEnvios= cantidaddeEnvios+1
    elif pagocontraentrega==2:
        cantidaddeEnvios= cantidaddeEnvios+1
    print("\nEl paquete fue registrado correctamente!")
    file.write(str(cantidaddeEnvios))
    file.close()

#Se muestra la información almacenada en el archivo
def mostrarInformacionPaquete():
    file=open("registroPaquete","r")
    mensaje=file.read()
    print(mensaje)
    file.close()
    

#<<<CREACIÓN GUÍAS>>>
import os
def crearArchivoGuias():
    file=open("registroGuias.txt","w")
    print("Bienvenidx a ENTREGAS MEX, para crear una guía, por favor ingrese los siguientes datos:")
    file.close()
        
def crearGuias():
    global guia
    
    print("Información de Guía")
    print("-Infromación de Comercio: \n","Nombre del Comercio: ",nombrecomercio,"\n","Telefono: ",telefonocomercio,"\n")
    print("-Información del Destinatario: \n","Nombre: ",nombredestinatario,"\n","Teléfono: ",telefonodestinatario)
    #Si requiere cobro
    file=open("registroGuias.txt","a")
    if pagocontraentrega==1:
        print("Su monto a pagar es de: ",montoacobrar)
        file.write(montoacobrar)
        file.write("\n")
    import random
    num = random.randint(0,10000)
    print("Su numero de tracking es",num,"\n\n")
    guia.append(num)
    

def mostrarInformacionGuias():
    file=open("registroGuias.txt","r")
    mensaje=file.read()
    print(mensaje)
    file.close()

#<<<CAMBIO DE ESTADO Y RASTREO>>>
    
def crearArchivoEstado():
    file=open("registroEstado.txt","w")
    print("Bienvenidx a ENTREGAS MEX, para cambiar el estado de un paquete, por favor ingrese los siguientes datos:")
    file.close()
        
def cambiarEstado():
    global estado
    global numTracking
    global status
    status=""
    #Cambio de estados del paquete
    file=open("registroEstado.txt","a")
    numTracking=input("Ingrese el número de tracking al que desea cambiar su estado: ")
    file.write(numTracking)
    file.write("\n")
    estado= int(input("Ingrese el nuevo estado del paquete"  
                       " 1=Creado" 
                       " 2=Recolectado" 
                       " 3=Entrega fallida" 
                       " 4=Entregado"))
    if estado==1:
        status="Creado"
        file.write(status)
        print("El estado del paquete",numTracking, "es: ",status)
        file.write("\n")
    elif estado==2:
        status="Recolectado"
        file.write(status)
        print("El estado del paquete",numTracking, "es: ",status)
        file.write("\n")
    elif estado==3:
        status="Entrega Fallida"
        file.write(status)
        print("El estado del paquete",numTracking, "es: ",status)
        file.write("\n")
    elif estado==4:
        status="Entregado"
        file.write(status)
        print("El estado del paquete",numTracking, "es: ",status)
        file.write("\n")

def mostrarInformacionEstadoRastreo():
    file=open("registroEstado.txt","r")
    trackingRastreo=input("Ingrese el número de tracking al que desea consultar su estado: ")
    trackingRastreo=numTracking
    print("",status)
    file.close()

#<<<MODULO DE ESTADÍSTICAS>>>
    
def moduloEstadistica():
    menuEstadistica=""
    menuEstadistica=int(input("Digite 1 si desea usar el Menu de Estadísticas o 2 si desea salir: "))
    while menuEstadistica==1:         
        menuEstadistica=int(input("Bienvenidx al menu de estadísticas, digite la opción a la que desea accesar: \n1-Cantidad de envíos.\n2-Lista de paquetes enviados.\n3- Monto de cobro.\n4- Cantidad de paquetes por número de teléfono.\n5-Cantidad de paquetes por número de cédula.\n"))
        if menuEstadistica==1:
            print("La cantidad de envios realizados es de: ",cantidaddeEnvios)
        if menuEstadistica==2:
            print("Lista de paqutes enviados: ",guia)
        if menuEstadistica==3:
            print("Su saldo pendiente es de ",montoacobrar)
        if menuEstadistica==4:
            telefonoEstadistica=input("Ingrese el número de teléfono al que desea consultar su cantidad de envíos: ")
            telefonoEstadistica=telefonodestinatario
            print("Cantidad de paquetes enviados al número ingresado: ")
            print("",cantidadxTelefono.count(telefonodestinatario))
        if menuEstadistica==5:
            cedulaEstadistica=input("Ingrese el número de cédula al que desea consultar su cantidad de envíos: ")
            cedulaEstadistica=ceduladestinario
            print("Cantidad de paquetes enviados a la cedula ingresada: ")
            print("",cantidadxCedula.count(ceduladestinario))
            
    

menuInicio=int(input("Digite 1 si desea usar el programa o 2 si desea salir: "))
while menuInicio==1:         
    menuPrincipal=int(input("Bienvenidx a ENTREGAS MEX, digite la opción a la que desea accesar: \n1-Registrar una cuenta de Usuario.\n2-Registrar una factura electrónica.\n3-Crear un paquete.\n4-Crear una guía.\n5-Cambiar el estado de un paquete.\n6-Rastrear un paquete.\n7-Mostrar Estadística\n"))
    if menuPrincipal==1:
        crearArchivoUsuario()
        registrarUsuario()
    if menuPrincipal==2:
        crearArchivoFactura()
        registrarFactura()
    if menuPrincipal==3:
        crearArchivoPaquete()
        crearPaquete()
    if menuPrincipal==4:
        crearArchivoGuias()
        crearGuias()
    if menuPrincipal==5:
        crearArchivoEstado()
        cambiarEstado()
    if menuPrincipal==6:
        mostrarInformacionEstadoRastreo()
    if menuPrincipal==7:
        moduloEstadistica()
