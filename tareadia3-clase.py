#crear una lista con nombre, apellido, correo y edad.
#donde al inicio me muestre las 4 cosas que quierop hacer, crear, actualizar, ver o eliminar
#y finalmente listar las personas del grupo que ya tengo ingresadas.

lista = []

continuar = True

while continuar:
    print("    Opciones Disponibles   ")
    print("1. Ver estudiantes")
    print("2.Crear")
    print("3. Modificar")
    print("4. Eliminar")
    print("5.Salir del sistema")    

    elegir_opcion = (input("Elige una de las opciones: "))

    if elegir_opcion == "1":
        print(lista)
          
    elif elegir_opcion == "2":
        nuevo_estudiante = {"nombre": input("nombre: "),"apellido": input("Apellido: "),"edad": int(input("Edad: ")), "correo": input("Correo: ")}
        lista.append(nuevo_estudiante)  
        
        
    elif elegir_opcion == "3":
        nombre_buscado = (input("Ingrese el nombre del estudiante a modificar: "))
        encontrado=0
        opcion = 0
        estudiante=0
        for estudiante in lista:
            if estudiante["nombre"] == nombre_buscado:
                encontrado = estudiante
                
        
        print("Que dato deseas cambiar")
        print("1. Nombre")
        print("2. Apellido")
        print("3.Edad")
        print("4.Correo")
        
        opcion=str(input("Elige una opcion: "))
        
        if opcion == "1":
            estudiante["nombre"]=input("nuevo nombre: ")
            
        elif opcion=="2":
            estudiante["apellido"] = input("Nuevo apellido: ") 
            
        elif opcion=="3":
            estudiante["edad"] = input("Nueva edad: ")
            
        elif opcion == "4":
            estudiante["correo"] = input("Nuevo correo: ")          
            
           
        
    elif elegir_opcion == "4":
        eliminar = (input("Ingresa el nombre del estudiante: "))
        lista.remove(eliminar) 
        
        
    elif elegir_opcion == "5":
        salir = input("Desea salir: S(si), N(no): ")
        if(salir=="S"):
            continuar=False
                   
        


print(lista)        
    
        

    
            
    
       