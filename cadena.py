print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 30/03/2023")

 #Escribir un programa que pregunte el nombre del usuario en la consola y después 
 # de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.

nombre= input("Escriba su nombre:")
print("! Hola ", nombre, "¡")
print("! Hola "+ nombre + "¡")
print(f" ! Hola {nombre} ¡")
print(" ! Hola {}".format(nombre))