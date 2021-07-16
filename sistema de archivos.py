import os
import tkinter
from tkinter import filedialog


def selecciona_ruta():
    raiz= tkinter.Tk()
    raiz.title("Explorando archivos.")
    raiz.iconify() # Oculto la ventana
    
    ruta=filedialog.askopenfilename() #Obtengo la ruta seleccionada
    raiz.destroy() #Queda pendiente           
    return ruta

def metodo(mi_ruta):
   # mi_ruta=open(mi_ruta2,"r", encoding="utf-8")
    
    while True:
        print("\n-OPCIONES DISPONIBLES- \n1.-Insertar \n2.-Modificar \n3.-Eliminar \n4.-Localizar y mostrar un registro\n5.-Calcular promedio de edades\n6.-Ver un ASCCI ART\n7.-Salir")
        opcion=int(input("Selccione una opción: "))
        
    #opción 1    
        if opcion==1:
            
            contador=0

            #mi_archivo=mi_ruta
            mi_archivo=open(mi_ruta)
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()
            
            for j in range(len(mi_lista)):
                if mi_lista[j][0:4]==("Id: "):
                    contador+=1
            

            #if contador<10:            
            #print(archivo.read())
            #ruta= "C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt"
            #archivo=open(ruta, 'r')
            #ite=0
            
            if os.stat(mi_ruta).st_size == 0: #Determino si esta vacío mi .txt                           
                    
                    ruta0= 'C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt'
                    archivo0=open(mi_ruta, 'w')

                    id_alumno=input("Ingrese id del alumno: ")
                    archivo0.write("Id: "+id_alumno+"\n")

                    nombre= input("Ingrese nombre del alumno: ")
                    archivo0.write("Nombre: "+nombre+"\n")

                    paterno= input("Ingrese apellido paterno del alumno: ")
                    archivo0.write("Apellido paterno: "+paterno+"\n")

                    materno=input("Ingrese apellido materno del alumno: ")
                    archivo0.write("Apellido materno: "+materno+"\n")

                    edad= input("Ingrese edad del alumno: ")
                    archivo0.write("Edad: "+edad)

                    print("Alumno registrado correctamente")
                    #archivo.close()
                    archivo0.close()

            elif  os.stat(mi_ruta).st_size != 0:
                    #ruta2= 'C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt'
                    archivo2=open(mi_ruta, 'a')
                    ite=0
                    

                    id_alumno=input("Ingrese id del alumno: ")
                    #print(mi_lista)
                    for j in range(len(mi_lista)):
                        if mi_lista[j]==("Id: "+id_alumno+"\n"):                        
                            ite+=1                                            
                    
                    if ite==0:                   
                        archivo2.write("\n\nId: "+id_alumno+"\n")

                        nombre= input("Ingrese nombre del alumno: ")
                        archivo2.write("Nombre: "+nombre+"\n")

                        paterno= input("Ingrese apellido paterno del alumno: ")
                        archivo2.write("Apellido paterno: "+paterno+"\n")

                        materno=input("Ingrese apellido materno del alumno: ")
                        archivo2.write("Apellido materno: "+materno+"\n")

                        edad= input("Ingrese edad del alumno: ")
                        archivo2.write("Edad: "+edad)
                        
                        print("Alumno registrado correctamente")
                    else:
                        print("Id ya registrada")                 
                    
                    #archivo.close()
                    archivo2.close()
            elif contador>=10:
                print("Se supero el número máximo de alumnos registrados (10)")        
    
     
    #Opción 2
        if opcion==2:
            mi_archivo=open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista                t
            mi_archivo.close()        
            ite=0
            cuen=0
            c=0

            busca_id=input("Ingrese el ID por BUSCAR: ")
            
            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):                     
                    print("Sí  encontro ID") 
                    c+=1
                    nueva_id= input("Ingrese NUEVA ID: ")                
                    for j in range(len(mi_lista)):
                        if mi_lista[j]==("Id: "+nueva_id+"\n"):                        
                            ite+=1 
                        if mi_lista[j][0:4]=="Id: ":
                            cuen+=1

                    if ite!=1: 
                        nuevo_nombre= input("Ingrese NUEVO Nombre: ")
                        nuevo_paterno= input("Ingrese NUEVA Apellido Paterno: ")
                        nuevo_materno= input("Ingrese NUEVA Apellido Materno: ")
                        nueva_edad= input("Ingrese NUEVA Edad: ")

                        mi_lista[i]="Id: "+nueva_id+"\n"
                        mi_lista[i+1]="Nombre: "+nuevo_nombre+"\n"
                        mi_lista[i+2]="Apellido paterno: "+nuevo_paterno+"\n"
                        mi_lista[i+3]="Apellido materno: "+nuevo_materno+"\n"
                        mi_lista[i+4]="Edad: "+nueva_edad+"\n"
                        print("Archivo modificado satisfactoriamente")
                        
                        mi_archivo = open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt", "w")
                        new_file_contents="".join(mi_lista)
                        
                        mi_archivo.write(new_file_contents)
                        mi_archivo.close

                        #Hasta aquí
                        readable_file = open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
                        read_file = readable_file.read()                                                
                        mi_archivo.close() 
                        
                    elif ite==1:
                        print("Id ya registrado")                
                                                    
            if cuen==c:
                print("No se encontro alumno con esa Id")            
                mi_archivo.close()        

    #Opción 3          
        if opcion==3:
            mi_archivo=open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()        
            
            cuen=0
            c=0    

            for j in range(len(mi_lista)):                    
                if mi_lista[j][0:4]=="Id: ":
                    cuen+=1
            
            busca_id=input("Ingrese el ID por ELIMINAR: ")            
            
            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):
                    c+=1                     
                    print("Sí  encontro ID")                                
                    mi_lista[i-1]=""
                    mi_lista[i]=""
                    mi_lista[i+1]=""
                    mi_lista[i+2]=""
                    mi_lista[i+3]=""
                    mi_lista[i+4]=""                
                                    
                    mi_archivo = open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt", "w")
                    new_file_contents="".join(mi_lista)
                    
                    mi_archivo.write(new_file_contents)
                    mi_archivo.close

                    #Hasta aquí
                    readable_file = open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
                    read_file = readable_file.read()                
                    print(mi_lista)

                    print("Archivo eliminado satisfactoriamente")
                    mi_archivo.close()
                    
                
            if cuen!=c:
                print("No se encontro alumno con esa Id")
                mi_archivo.close()                
        
    #Opción 4
        if opcion==4:
            mi_archivo=open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
            mi_lista= mi_archivo.readlines() #Archivo convertido en lista
            mi_archivo.close()
            print(mi_lista)
            ubicacion=0
            
            busca_id=input("Ingrese el ID por BUSCAR: ")            
            
            for i in range(len(mi_lista)):
                if mi_lista[i]==("Id: "+busca_id+"\n") or mi_lista[i]==("Id: "+busca_id):                     
                    print("Sí  encontro ID")

                    print(mi_lista[i])
                    print(mi_lista[i+1])
                    print(mi_lista[i+2])
                    print(mi_lista[i+3])
                    print(mi_lista[i+4])                                 
                    
                    #Hasta aquí
                    readable_file = open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
                    read_file = readable_file.read()                                
                    mi_archivo.close()                            
                #else:
                #   print("No se encontro alumno con esa Id")
                #ubicacion+=1
                #mi_archivo.close()  

    #Opción 5
        if opcion==5:
            ruta='C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt'
            archivo=open(ruta, 'r+')
            con=0

            #Archivo vacío        
            if os.stat("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt").st_size == 0:
                print("El archivo esta vacío, no se pueden modificar datos")
            
            #Archivo diferente de vacío
            else:            
                mi_archivo=open("C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt")
                mi_lista= mi_archivo.readlines() #Archivo convertido en lista                t
                mi_archivo.close()
                print(mi_lista)            
                #ruta= 'C:/Users/Jordan/Documents/ITP/4to/Sistemas Operartivos/Unidad 5/miarchivo.txt'
                #archivo=open(ruta, 'w')
                                        
                edad=0
                div=0
                for i in range(len(mi_lista)):
                    if mi_lista[i][0:6]==("Edad: "):
                        div+=1
                        edad+=float(mi_lista[i][5:8])
                
                #print(mi_lista[4][5:])            
                promedio=+edad/div
                print("El promedio de edades es: {}". format(promedio))
                archivo.close()                       
        
    #Opción 6
        if opcion==6:        
            print("")
            print("         _nnnn_                      ")
            print("        dGGGGMMb     ,"""""""""""""".")
            print("       @p~qp~~qMb    | Linux Rules! |")
            print("       M|@||@) M|   _;..............'")
            print("       @,----.JM| -'")
            print("      JS^\__/  qKL")
            print("     dZP        qKRb")
            print("    dZP          qKKb")
            print("   fZP            SMMb")
            print("   HZM            MMMM")
            print("   FqM            MMMM")
            print(" __|  .        |\dS qML")
            print(" |    `.       |    \Zq")
            print("_)      \.___.,|     . ")
            print("\____   )MMMMMM|   .'")
            print("     `-'       `--' hjm")
 
    #Opción 7
        if opcion==7:
            break                             
    
la_ruta=selecciona_ruta()
metodo(la_ruta)

