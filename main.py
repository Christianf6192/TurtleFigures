import turtle

def main():
  squirt = turtle.Turtle()
  squirt.penup()
  squirt.goto(0,150)
  draw_red_triangle(squirt)
  squirt.penup()
  squirt.goto(-150,20)
  squirt.pendown()
  draw_blue_square(squirt)
  squirt.penup()
  squirt.goto(0,-280)
  squirt.pendown()
  draw_black_circle(squirt, 150)
  
def draw_blue_square(turtle):
  turtle.color('blue')
  for i in range(4):
    turtle.forward(300)
    turtle.right(90)

def draw_red_triangle(turtle):
  turtle.color('red')
  turtle.pendown()
  turtle.goto(150, 50)
  turtle.goto(-150,50)
  turtle.goto(0,150)

def draw_black_circle(turtle, radius):
  turtle.color('black')
  turtle.circle(radius)


if __name__ == "__main__":
    main()