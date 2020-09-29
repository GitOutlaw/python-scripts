import turtle

#square
my_turtle = turtle.Turtle()


def square():
   my_turtle.forward(100)
   my_turtle.right(90)
   my_turtle.forward(100)
   my_turtle.right(90)
   my_turtle.forward(100)
   my_turtle.right(90)
   my_turtle.forward(100)

square()
my_turtle.forward(200)
square()

turtle.done()

elephant_weight = 3000
ant_weight = 0.1

if elephant_weight > ant_weight:
    print(my_turtle)