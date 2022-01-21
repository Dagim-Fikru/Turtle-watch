# In this simple project i tried to make an ethiopian analog clock by using the d/t method I read from d/t sources!!
import turtle
import time

scrn = turtle.Screen()
scrn.bgcolor('#B1B2B7')
scrn.setup(width=900, height=700)
scrn.tracer(0)

draw = turtle.Turtle()
draw.speed(0)
draw.hideturtle()
draw.pensize(5)


def draw_hands(hr, sec, mnt, draw):
    # Let's first draw the circle of our clock!!
    draw.penup()
    draw.goto(0, -200)
    draw.setheading(-360)
    draw.pendown()
    draw.color('Black')
    draw.circle(200)
    # make a hanger to our watch!!
    draw.penup()
    draw.goto(0, 200)
    draw.right(-90)
    draw.pendown()
    draw.color("brown")
    draw.forward(80)

    hanger = turtle.Turtle()
    hanger.penup()
    hanger.goto(0, 290)
    hanger.shape("circle")
    hanger.shapesize(stretch_wid=1, stretch_len=1)

    # now let's draw the small lines that represent the hours 1 to 12!!

    draw.penup()
    draw.goto(0, 0)
    draw.setheading(90)
    for i in range(12):
        draw.forward(190)
        draw.color("black")
        draw.pendown()
        draw.forward(10)
        draw.penup()
        draw.goto(0, 0)
        draw.right(30)

    # now let's write 4 numbers on clock such as 12,3,6 and 9 in this case i used geez(Ethiopian number)

    draw.goto(-15, 143)
    draw.write("፲፪", font=("Helvetica", 30, 'bold'))
    draw.goto(168, -15)
    draw.write("፫", font=("Helvetica", 30, 'bold'))
    draw.goto(-10, -185)
    draw.write("፮", font=("Helvetica", 30, 'bold'))
    draw.goto(-185, -15)
    draw.write("፱", font=("Helvetica", 30, 'bold'))

    # I want to add some dicoration in the center of the clock it means "it is my dam"!

    draw.color("green")
    draw.goto(-30, 0)
    draw.write("ግድቡ", font=("Times", 20, 'bold'))
    draw.color("Yellow")
    draw.goto(-17, -30)
    draw.write("የኔ", font=("Times", 20, 'bold'))
    draw.color("Red")
    draw.goto(-27, -55)
    draw.write("ነው።", font=("Times", 20, 'bold'))

    center_circle = turtle.Turtle()
    center_circle.shape("circle")
    center_circle.color("brown")
    center_circle.shapesize(stretch_wid=0.5, stretch_len=0.5)

    # now lets draw the hands that represent minute,hour and second!!

    draw.goto(0, 0)
    draw.setheading(90)
    draw.color("#06455C")
    draw.pensize(3)
    angle = (sec / 60) * 360
    draw.right(angle)
    draw.pendown()
    draw.forward(165)

    draw.goto(0, 0)
    draw.setheading(90)
    draw.pensize(6)
    draw.color("#1B0452")
    angle = (hr / 12) * 360
    draw.right(angle)
    draw.pendown()
    draw.forward(60)

    draw.goto(0, 0)
    draw.setheading(90)
    draw.color("black")
    draw.pensize(5)
    angle = (mnt / 60) * 360
    draw.right(angle)
    draw.pendown()
    draw.forward(100)


# to let our clock update with current time we will do this;
while True:
    sec = int(time.strftime("%S"))
    mnt = int(time.strftime("%M"))
    hr = int(time.strftime("%I"))

    draw_hands(hr, sec, mnt, draw)

    scrn.update()

    time.sleep(1)

    draw.clear()

scrn.mainloop()
