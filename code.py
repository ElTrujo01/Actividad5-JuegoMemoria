# Por:  Jesus A. Trujillo de Anda   A00827538
#       Jorge Avalos                A01720730
#       Carlos Milano               A01383102
#       Carlos Gaeta López          A01611248
#       Alberto Guajardo            A00826548

#Herramientas computacionales: el arte de la programación (Gpo 6)

#Actividad 5. Juego de Memoria

#ULTIMA FECHA DE MODIFICACION: Jueves, 28 de octubre de 2021

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
writer = Turtle(visible=False) #llamada al metodo
tiles = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Ñ','!','?','+','-','&','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Ñ','!','?','+','-','&']
state = {'mark': None}
stateTaps = {'score': 0} #creacion del contador
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    clear()
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        stateTaps['score'] += 1 #suma de un tap al contador
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        stateTaps['score'] += 1 #suma de un tap al contador 

    hideturtle()
    tracer(False)
    writer.undo()
    writer.write(stateTaps['score']) #actualizacion del contador de taps

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 12, y) #centrar la escritura de la letra
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(450, 470, 390, 0)
hideturtle()
tracer(False)
writer.goto(200, 200) #coordenadas del contador de taps 
writer.color('black') #color del contador de taps
writer.write(stateTaps['score']) #despliegue
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

# 2021. Derechos reservados : Ninguna parte de esta obra puede ser reproducida o
# transmitida, mediante ningún sistema o método, electrónico o mecánico, sin conocimiento por escrito 
# de los autores. Tec de Monterrey.