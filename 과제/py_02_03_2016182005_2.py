Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.shape('turtle')
>>> t.goto(0,500)
>>> t.goto(500,500)
>>> t.goto(500,0)
t
>>> t.goto(0,0)
>>> t.goto(0,100)
>>> t.forward(500)
t
>>> t.goto(500,200)
>>> t.back(500)
>>> t.goto(0,300)
>>> t.forward(500)
>>> t.goto(500,400)
>>> t.back(500)
>>> t.penup()
>>> t.goto(100,0)
>>> t.left(90)
>>> t.pendown()
>>> t.forward(500)
>>> t.goto(200,500)
>>> t.back(500)
>>> t.goto(300,0)
>>> t.forward(500)
t
>>> t.goto(400,500)
>>> t.back(500)
>>> turtle.exitonclick()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    turtle.exitonclick()
NameError: name 'turtle' is not defined
>>> t.exitonclick()
>>> 