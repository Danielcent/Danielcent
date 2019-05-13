#uso de numeros aleatorios
#guardamos en la carpeta del repositorio
#con la expresion .py
#uso de numeros aleatorios



#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)  #creamos una variable
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el numero generado
#ejercicio
#escribir una funcion sorteo()que reciba
#una lista de participantes, y elegir a uno
#de los participantes aleatoriamente, y
#retornar esa persona elegida
#desafio: no volver a retornar una persona
#   ya sorteada


from sorteo import randint
concursantes=["Daniel","Marcos","Jose","Matias","Horacio","Leo","Fran"]#creamos una lista
def personas(partisipan):
ficha=randint(0,len(concursantes))  #se aplica el numeron 0 a la lista de concursantes
ganador=concursantes[ficha]
return ganador
personas(concursantes)


#Soluciones
#importamos la funcion randint de libreria random
from random import randint
def sorteo-fin_de_anho(lista):# definimos una funcion
    #
    #
    cant=len(lista)-1
    indice=randint(0,cant)#
    ganador=lista[indice]
    return ganador
    print(ganador)  #esto no se ejecuta

participantes=["Juan","Lucas","Fede","Jose","Ramon","Junior","Marin"]
ganar=sorteo_fin_de_anho(participantes)
print(ganar)







