#las listas son equivalentes a los arreglos en otros lenguajes de programacion

#las listas en python se pueden guardar diferentes tipos de valores

#el primer elemente empieza tiene posicion cero, el segundo es 1
print "Agregando datos a la lista"
listaCantantes = ["Ariana Grande","Selena Gomez","Katty Perry","Alissa Strekozova","Rihanna","Adam Levine"]
print listaCantantes,"\n"

print "Creando lista con diferentes tipos de datos"
#creamos una lista para almacenar el nombre y edad del estudiante
listaEstudiantes = ["Santos Lopez",23]
print listaEstudiantes,"\n"

print "Imprimiendo el valor del indice 5 de la lista"
#si queremos imprimir alguna posicion en especifica de la lista unicamente le mandamos la posicion de la lista
print(listaCantantes[5]),"\n"   #imprimimos el ultimo elemento de la lista - resultado> Adam Levine

print "Imprimiendo el primer valor de la lista"
print(listaEstudiantes[0]),"\n" #imprimimos  el primer elemento de la lista - resultado> Santos Lopez

print "Imprimiendo el segundo valor de la lista"
print(listaEstudiantes[1]),"\n" #imprimimos el segundo elemento de la lista - resultado> 23


print "Imprimos el primer elemento hasta el indice 2"
#imprimos el primer elemento hasta el indice 2, el numero tres queda excluido
print(listaCantantes[0:3]),"\n"

print "Imprimos el primer elemento hasta el indice 2 (Otra forma de usar el codigo)"
print(listaCantantes[:3]),"\n" #esto es equivalente la linea anterior

print "Imprimir lo que esta en el indice 2 hasta el ultimo elemento"
print(listaCantantes[2:]),"\n" #empieza a imprimir lo que esta en el segundo elemento de la lista hasta el ultimo

print "Agregamos el elemento Kristina Basham al final de la lista"
#Para agregar elementos al final de la lista
listaCantantes.append("Kristina Basham")
print(listaCantantes[:]),"\n" #imprimos todos los elementos de la lista

print "En el indice 2 incluimos el elemento Megan Maria"
#En el indice 2 incluye este elemento
listaCantantes.insert(2,"Megan Maria")
print (listaCantantes[:]),"\n"

print "Agregamos elementos a la lista original"
#agregamos estos elementos a la lista original
listaEstudiantes.extend(["Valentina","Flor","Nancy"])
print(listaEstudiantes[:]),"\n"


print "Averiguando si el indice de Santos Lopez existe"
#Si quiero averiguar el indice de cierto elemento, si existen dos elementos iguales me devuelve el primer elemento encontrado
print (listaEstudiantes.index("Santos Lopez")),"\n"

print "Averiguamos si el elemento Santos Lopez esta o no en la lista"
#Averiguar si un elemento esta o no en una lista
print ("Santos Lopez" in listaEstudiantes),"\n" #imprime verdadero o falso si esta la lista

print "Eliminando el nombre Adam Levine de la lista cantantes"
listaCantantes.remove("Adam Levine")
print(listaCantantes[:]),"\n"

print "Eliminando el numero 23 de la lista estudiantes "
listaEstudiantes.remove(23)
print(listaEstudiantes[:]),"\n"

print "Eliminando ultimo elemento de la lista utilizando funcion pop"
listaCantantes.pop()
print(listaCantantes[:]),"\n"

print "Creando listas"
#Sumando listas diferentes
amores = ["Pizza","Batidos","Frijoles"]
print(amores[:]),"Lista creada \n"
precios = [5,10,2]
print (precios[:]),"Lista creada\n"
precioComida =amores+precios
print("Lista unidas"),"\n"
print (precioComida[:]),"\n"

print "Repitiendo listas usando operador de multiplicacion"
print (amores * 3),"\n"
