# Blóm/stjarna eins og í gamla Logo-forritinu:
# teikna línu, beygja um X gráður, skipta um lit, endurtaka endalaust.
#
# Logo-útgáfan:   REPEAT 10000 [SETPC REPCOUNT FD 200 RT :X]

import turtle

X = 170          # beygjan í gráðum - prófaðu 144, 160, 175, 91, 121...
LENGD = 300      # FD 300
LITIR = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

skjar = turtle.Screen()
skjar.bgcolor("black")
skjar.title(f"Blóm - beygja {X}°")

s = turtle.Turtle()      # skjaldbakan sjálf
s.speed(0)               # hraðast
s.hideturtle()           # HT
s.width(2)

skref = 0
while LENGD > 0:
    s.pencolor(LITIR[skref % len(LITIR)])
    s.forward(LENGD)
    s.right(X)
    skref = skref + 1
    LENGD = LENGD - 1

turtle.done()