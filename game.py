import turtle, random

# setup turtle parameters
a = turtle.Turtle()
a.pensize(5)
a.shape('turtle')
a.speed(9)

# screen properties
screen = turtle.Screen()
screen.colormode(255)
screen.screensize(500, 2000)

# shape parameters
num_tri = 3
length = 80
enlarge = 60
colors = ['blue', 'green', 'red']

# This function is to move the turtle forward



def makeShapes(num):
    def draw(length):
        for i in range(3): 
            a.forward(length)
            a.left(120)

    for i in range(num):
        a.backward(enlarge/2)
        
        # randomly generates color
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # set color and draw
        a.pencolor(red, green, blue)
        draw(length + i*enlarge)

i = 5
hit = False
while i <= 5:
    makeShapes(i)
    if i <= 1:
        hit = True
    if hit:
        i+=2
    else:
        i-=2

    

print("hello kiros")


turtle.done()   #exits on click
