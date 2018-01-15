# Keep up your hard work, and Go Bears!
# Let is do this

# Autor: Santos Lopez Tzoy

# ciclo infinito, se repite sino se cumplen los numeros del rango esperado
while True:
    try:
        # variable donde vamos almacenar lo que se ingresa
        height = int(input(u"Height: "))
        if height>=1 and height<24:
            print("Very good!!!\n")
            break # nos salimos del ciclo cuando se cumplen los numeros esperados
    except:
        #si lo que se ingresa no es numero imprimimos este mensaje
        print("ERROR!!! ")
