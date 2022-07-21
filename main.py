import turtle


T = turtle.Turtle()
B = turtle.Turtle()
B.color("red")
B.pensize(5)
T.pensize(2)
screen = turtle.Screen()

def circle():
  T.circle(100)

def square():
  for x in range(4):
    B.forward(200)
    B.right(90)



def pattern():
  for i in range(35):
    circle()
    T.right(10)
  
def pattern2():
  for i in range(36):
    square()
    B.right(10)
    

screen.onkey(pattern, "o")
screen.onkey(pattern2, "p")
screen.listen()