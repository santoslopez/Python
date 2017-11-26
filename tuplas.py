#es igual que una lista pero no se mueve agregar, eleminar y mover elementos, por eso son inmutables
#las tuplas no permiten busquedas, pero si permite verificar si un elemento esta en la tupla
#las tuplas son rapidas mayor optimizacion, formatean string, pueden usarse como claves en un diccionario


tuplaMujeres = ("Maria","Megan","Katty","Barbara","Kristina")
tuplaHombres = "David Beckham","Romeo Santos","Taylor Lautner" #es valido no poner los parentesis en las tuplas
tuplaSelecciones = ("Holanda",10,"Roben");

print ("Imprimiendo las tuplas creadas: \n");
#imprimimos los valores de las tuplas, las tres formas son equivalentes, falto print (tuplaSelecciones);
print tuplaMujeres
print tuplaHombres;
print (tuplaSelecciones)

print ("\nAccediendo a ciertas posiciones de las tuplas: \n");
print ("Ellos son pareja: "+tuplaMujeres[0] + " y "+tuplaHombres[2]);
print ("Ellos son pareja: "+tuplaMujeres[1] + " y "+tuplaHombres[0]);

print ("\nConvirtiendo tupla a lista - noten que la lista lleva llaves la tupla parentesis \n");
#convirtiendo tupla en lista
miLista = list(tuplaHombres);
print miLista


print "\nConvirtiendo lista a tupla:\n"
miTupla = tuple(miLista)
print miTupla

print "\nAveriguamos si cierto texto se encuentra en la tupla:\n";
print "Quiero saber si el nombre Maria se encuentra en la tupla","Maria" in tuplaMujeres
print "Quiero saber si la palabra amor se encuentra en la tupla","amor" in tuplaMujeres

#o queremos saber por ejemplo si el nombre maria cuantas veces se repite
print "\nPregutar cuantos elementos estan en la tupla:"
print "Cuantas veces el nombre Taylor Lautner esta en la tupla: ",miTupla.count("Taylor Lautner")


#averiguamos la longitud o cantidad elementos
print "Cuantos elementos hay en la tupla David Beckham","Romeo Santos","Taylor Lautner"
print (len(miTupla))

#creando tuplas unitarias
print "\nCreando tuplas unitarias"
tuplaUnitaria = ("Santos",)#es necesario poner la coma
print tuplaUnitaria,"\n"

#las tuplas sin parentesis se llama empaquetado de tuplas

#desempaquetado de tuplas
edad,mes,year = miTupla
print "\nDesempaquetado de tuplas - a cada variable declarado le asigna cada valor que esta dentro de la tupla"
print (edad)
print (year)
print (mes)
