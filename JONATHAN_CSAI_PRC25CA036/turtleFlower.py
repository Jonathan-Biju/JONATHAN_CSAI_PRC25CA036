import turtle

def draw_petal(t,radius,angle):
    for _ in range(2):
        t.circle(radius,angle)
        t.left(180-angle)

wn=turtle.Screen()
wn.bgcolor("black")
t=turtle.Turtle()
t.color("red")
t.speed(0)
petals=12

for _ in range(petals):
    draw_petal(t,radius=100,angle=60)
    t.left(360/petals)
t.hideturtle()
turtle.done()