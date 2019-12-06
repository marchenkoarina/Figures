import turtle 

def triangle(x, y, size, colour, angle):
    # TODO: (Olya)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(colour)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.penup()
    pass
  
def square(x, y, size, colour, angle):
    # TODO: (Arina)
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(angle)
    turtle.pendown()
    turtle.pencolor(colour)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    pass
  
 def main():
    
    # TODO: (Olya) figure 1
    square(-120, 60, 60, 'red', 0)
    triangle(-105, 150, 30, 'red', 270)
    triangle(-60, 120, 30, 'red', 270)
    triangle(-30, 90, 30, 'red', 180)
    triangle(-75, 60, 30, 'red', 270)
    triangle(-120, 90, 30, 'red', 270)
    triangle(-150, 120, 30, 'red', 0)
    pass
  
    # TODO: (Arina) figure 2
    triangle(30, 150, 30, 'yellow', 0)
    triangle(60, 180, 30, 'yellow', 180)
    square(60, 120, 30, 'yellow', 0)
    triangle(90, 90, 30, 'yellow', 90)
    square(90,90, 30, 'yellow', 90)
    triangle(150, 120, 30, 'yellow', 180)
    triangle(60, 60, 30, 'yellow', 90)
    triangle(150, 60, 30, 'yellow', 0)
    pass
  
  
    # TODO: (Arina) figure 3
    triangle(30, -60, 30, 'blue', 180)
    triangle(60, -30, 30, 'blue', 180)
    triangle(90, -60, 30, 'blue', 180)
    triangle(30, -90, 30,'blue', 90)
    triangle(60, -120, 30, 'blue', 0)
    square(60, -120, 30, 'blue', 90)
    square(90, -120, 30, 'blue', 0)
    triangle(150, -90, 30, 'blue', 180)
    pass
  
  
    # TODO: (Olya) figure 4
    triangle(-90, -60, 30, 'green', 90)
    triangle(-120, -90, 30, 'green', 270)
    square(-60, -90, 30, 'green', 0)
    triangle(-60, -90, 30, 'green', 270)
    triangle(-90, -120, 30, 'green', 0)
    square(-90, -120, 30, 'green', 90)
    triangle(-30, -120, 30, 'green', 90)
    triangle(-60, -150, 30, 'green', 270)
    pass

main()
  
