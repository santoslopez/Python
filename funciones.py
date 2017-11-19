#las funciones se usan directamente para reutilizar codigo

#esta funcion no tiene parametros (o argumentos) y vamos a imprimir un texto
def imprimirTexto():
    print "Hola mundo" #la funcion print es una predefinido o sea ya viene en el lenguaje

#mandamos a llamar la funcion para que se ejecute
imprimirTexto()#ejecutamos la funcion


#funcion con parametros para imprimir indicar que numero es mayor, menor o igual
def numeros(primerNumero,segundoNumero):
    if primerNumero>segundoNumero:
        print "El primerNumero",primerNumero," es mayor al segundo ",segundoNumero
    elif segundoNumero>primerNumero:
        print "El segundo argumento ",segundoNumero," es mayor al primero ",primerNumero
    elif primerNumero==segundoNumero:
        print "El primer numero es ",primerNumero," y el segundo numero es",segundoNumero," son iguales"

numeros(1,2)#el segundo numero es mayor al primero
numeros(10,2)#el primer numero es mayor al segundo
numeros(100,100)#los numeros son iguales


#sumatoria de dos numeros
def operacionesAritmeticas(primerNumero,segundoNumero):
    print "La suma de ",primerNumero," (primer parametro) y ", segundoNumero, " (segundo parametro) es ",(primerNumero+segundoNumero)
    print "La resta de ",primerNumero," (primer parametro) y ", segundoNumero, " (segundo parametro) es ",(primerNumero-segundoNumero)
    print "La multiplicacion de ",primerNumero," (primer parametro) y ", segundoNumero, " (segundo parametro) es ",(primerNumero*segundoNumero)
    print "La division de ",primerNumero," (primer parametro) y ", segundoNumero, " (segundo parametro) es ",(primerNumero/segundoNumero)

operacionesAritmeticas(100,2)#realizamos las operaciones aritmeticas y imprimimos su resultado
