#Jenoh Sam J B
#URK24CS1154
#Create a program to load an image and demonstrate
print("URK24CS1154")
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt 
image_path = (r"C:\Users\DELL\OneDrive\Desktop\carsrolls.jpeg")
image = Image.open(image_path)
image.show()
plt.imshow(image)
plt.title("Plotted Image")
plt.axis("off")
plt.show()
width, height = image.size
print(f"Image Width: {width}, Image Height: {height}")
half_size = image.resize((width // 2, height // 2))
half_size.show()
rotated = image.rotate(145, expand=True)
rotated.show()
resized = image.resize((width + 50, height + 70))
resized.show()
flip_lr = ImageOps.mirror(image)
flip_tb = ImageOps.flip(image)
flip_lr.show()
flip_tb.show()
cropped = image.crop((50, 50, 150, 150)) 
cropped.show()
gray = image.convert('L')
black_white = gray.point(lambda x: 255 if x > 127 else 0, '1')
gray.show()
black_white.show()
blurred = image.filter(ImageFilter.GaussianBlur(5))
blurred.show()





#Jenoh Sam J B
#URK24CS1154
#Create a turtle programs for national flag
print("URK24CS1154")
import turtle
def draw_rectangle(x, y, width, height, color):
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def draw_circle(x, y, radius, color):
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def draw_national_flag():
    draw_rectangle(-150, 100, 300, 50, "orange") 
    draw_rectangle(-150, 50, 300, 50, "white") 
    draw_rectangle(-150, 0, 300, 50, "green")  
    draw_circle(0, 25, 25, "blue")    
screen = turtle.Screen()
screen.setup(width=600, height=400)
turtle.speed(3)
draw_national_flag()
print("Image drawn successfully.")
turtle.hideturtle()
turtle.done()





#Jenoh Sam J B
#URK24CS1154
#Create a turtle programs for house and flag
print("URK24CS1154")
import turtle
def draw_rectangle(x, y, width, height, color):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def draw_triangle(x, y, base, height, color):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    turtle.goto(x + base / 2, y + height)
    turtle.goto(x + base, y)
    turtle.goto(x, y)
    turtle.end_fill()
def draw_circle(x, y, radius, color):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def draw_house():
    draw_rectangle(-100, 0, 100, 100, "blue")  
    draw_triangle(-100, 0, 100, 70, "yellow")  
    draw_rectangle(-65, -50, 30, 50, "white")  
def draw_flagpole():
    draw_rectangle(68, -100, 0, -140, "black") 
    draw_rectangle(27, 10, 40, 20, "blue")  
    draw_circle(68, 55, 15, "yellow") 
screen = turtle.Screen()
screen.setup(width=600, height=400)
turtle.speed(3)
draw_house()
draw_flagpole()
print("Image drawn successfully.")
turtle.hideturtle()
turtle.done()
