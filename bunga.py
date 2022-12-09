import turtle
a = turtle
x = 1
""""
while(True):
    x +=1
    if x > 3:
        x = 0
"""
a.bgcolor("black")
def flower():
    for i in range(100):
        for colors in ["red", "yellow", "blue"]:
            a.speed(100)
            a.color(colors)
            a.circle(190-i, 90)
            a.left(90)
            for c in ["orange" , "green"  , "purple" ]:
                a.color(c)
            a.circle(190-i, 90)
            a.left(10)
flower()
turtle.done()