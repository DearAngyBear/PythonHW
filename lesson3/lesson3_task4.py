from turtle import *
t = Turtle()
t.screen.setup(1000, 1000)
t.ht()
t.up()
t.goto (0,-10)
t.down()

t.fillcolor ("yellow")
t.begin_fill ()

t.goto (-20,0)
t.goto (-40,20)
t.goto (-50,15)
t.goto (-45,30)
t.goto (-50,25)
t.goto (-60,30)
t.goto (-60,20)
t.goto (-70,35)
t.goto (-60,40)
t.goto (-60,50)
t.goto (-30,60)
t.goto (10,40)
t.goto (20,60)
t.goto (30,55)
t.goto (35,40)
t.goto (60,-20)
t.goto (30,-50)
t.goto (10,-60)
t.goto (10,-50)
t.goto (0,-70)
t.goto (0,-50)
t.goto (-20,-80)
t.goto (0,-20)
t.goto (5,0)
t.goto (10,20)

t.up()
t.goto (35,40)
t.down()
t.goto (35,40)
t.goto (45,60)
t.goto (90,0)
t.goto (100,-30)
t.goto (80,-10)
t.goto (80,-40)
t.goto (70,-20)
t.goto (60,-50)
t.goto (10,-130)
t.goto (10,-110)
t.goto (0,-130)
t.goto (0,-110)
t.goto (-10,-130)
t.goto (-10,-110)
t.goto (-30,-130)
t.goto (-20,-110)
t.goto (-50,-130)
t.goto (30,-50)

t.end_fill ()

t.up ()
t.goto (-40,40)
t.down ()

t.fillcolor ("black")
t.begin_fill ()
t.circle (4)
t.end_fill ()


t.screen.exitonclick()
t.screen.mainloop()