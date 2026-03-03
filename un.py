import turtle
import time
import random

pospos_retraso = 0.1
marcador = 0
max_marcador = 0

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de la Culebrita")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0) # Desactiva animaciones automáticas para fluidez

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# Segmentos del cuerpo
cuerpo = []

# Texto del marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Marcador: 0   Máximo: 0", align="center", font=("Courier", 20, "normal"))

# Funciones de movimiento
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Bucle principal
while True:
    ventana.update()

    # Colisión con bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        # Esconder segmentos
        for segmento in cuerpo:
            segmento.goto(1000, 1000)
        cuerpo.clear()
        marcador = 0
        texto.clear()
        texto.write(f"Marcador: {marcador}   Máximo: {max_marcador}", align="center", font=("Courier", 20, "normal"))

    # Colisión con comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("lightgreen")
        nuevo_segmento.penup()
        cuerpo.append(nuevo_segmento)

        marcador += 10
        if marcador > max_marcador:
            max_marcador = marcador
        texto.clear()
        texto.write(f"Marcador: {marcador}   Máximo: {max_marcador}", align="center", font=("Courier", 20, "normal"))

    # Mover el cuerpo (en orden inverso)
    total_segmentos = len(cuerpo)
    for i in range(total_segmentos -1, 0, -1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x, y)

    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)

    movimiento()

    # Colisión con el propio cuerpo
    for segmento in cuerpo:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            for s in cuerpo:
                s.goto(1000, 1000)
            cuerpo.clear()
            marcador = 0
            texto.clear()
            texto.write(f"Marcador: {marcador}   Máximo: {max_marcador}", align="center", font=("Courier", 20, "normal"))

    time.sleep(pospos_retraso)

ventana.mainloop()