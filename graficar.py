import matplotlib.pyplot as plt

nombresMujeres = ('Maria Zlatkova','Kristina','Alejandra','.Eva')

#los nombres deben de tener un valor para que podamos hacer la grafica
cantidadPais = (100,300,500,533)

#para que la grafica se visualice mejor le vamos a dar un color
colores = ('crimson','orange','blue','red')


#resaltar un texto con respecto a los demas
otrosTextos = (0.1,0,0,0)


#quitar las barras de herramientas
plt.rcParams['toolbar'] = 'None'


#ultimo valor representa a lo que se guarda en el porcentaje
_, _, valoresPorcentaje = plt.pie(cantidadPais,colors=colores,labels=nombresMujeres,autopct='%1.1f%%',explode=otrosTextos,startangle=90)

for v in valoresPorcentaje:
	v.set_color('white')


#para que realmente sea un circulo
plt.axis('equal')


plt.title('Nombre de mujeres por pais')

#esto es para dibujar los nombres de las mujeres
#plt.legend(labels=nombresMujeres)


#guardar la grafica como imagen
plt.savefig('nombresMujeres.png')


plt.show()