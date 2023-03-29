cant1=float(input("ingrese el primer dato:"))
cant2=float(input("Ingrese el segundo dato:"))

valor= cant1== cant2
#OPCION1
print ("los numeros" +str(cant1)+ " y "+  str(cant2) + " son iguales " +  str(valor))
#OPCION 2
print("el numero ", cant1," y ", cant2, "son iguales ",valor)
#OPCION 3
print(f"los  numeros {cant1} y {cant2} son iguales  {valor}")
#OPCION 4
print("los numeros  {} y {} son iguales {} \n".format(cant1,cant2,valor))
#OPCION 4

valor= cant1!=cant2
#OPCION1
print("los numeros "+ str (cant1)+ " y "+ str(cant2) +"son distintos" + str(valor))
#OPCION2
print("los numeros ", cant1," y ",cant2, " son distintos " , valor)
#OPCION3
print(f"los numeros {cant1} y {cant2} son distintos {valor}")
#OPCION4
print("los numeros {} y{} son distintos  {} \n".format(cant1,cant2,valor))

valor=cant1 > cant2
#OPCION1
print("el numero "+str(cant1)+ " es mayor al " + str(cant2) + str(valor))
#OPCION2
print("el numero  " , cant1, "es mayor al  ",cant2 ,valor)
#OPCION3
print(f"el primero  {cant1}  es mayor al   {cant2} {valor}")
#OPCION4
print("el primero es   {} es mayor   {}  {} \n".format(cant1,cant2,valor))

valor=cant1 <= cant2
#OPCION1
print("el numero "+str(cant2)+ " es mayor o igual que " + str(cant1)+ " "+str(valor))
#OPCION2
print("el numero" , cant2, " es mayor o igual que ",cant1 , valor,)
#OPCION3
print(f"el numero {cant2}  es mayor o igual quw {cant1}  {valor}")
#OPCION4
print("el numero  {}  es mayor o igual que {}  {} \n".format(cant2,cant1,valor))
