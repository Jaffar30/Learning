# from turtle import Turtle, Screen
# from random import randint
# import os
# import colorgram

# # absolute path of script
# script_dir = os.path.dirname(__file__)
# img_path = os.path.join(script_dir, "img.png")
# print(img_path)
# colors = colorgram.extract(img_path, 30)



# def main():
#     screen = Screen()
#     turtle = Turtle()
#     turtle.speed("fastest")
    

#     for i in range(100):
#         turtle.circle(100)
#         turtle.setheading(turtle.heading()+10)

    
    
    
#     screen.exitonclick()

# # main()




from turtle import Turtle, Screen
from random import randint,choice
import colorgram

# absolute path of script
# rgb_colors = []
# colors = colorgram.extract(r"c:\Users\Jaffar_Pc\OneDrive\Desktop\my-projects\Learning\python\day18\img.png", 30)

# for color in colors:
#     r  = color.rgb.r
#     g  = color.rgb.g
#     b  = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(233, 233, 232), (231, 232, 236), (234, 231, 233), (224, 232, 226), (207, 158, 80), (56, 89, 130), (146, 92, 41), (221, 204, 111), (139, 26, 46), (134, 175, 201), (157, 46, 87), (44, 55, 105), (130, 189, 144), (165, 159, 38), (84, 20, 45), (189, 140, 165), (186, 92, 105), (43, 41, 60), (86, 121, 179), (88, 156, 93), (57, 39, 33), (80, 153, 165), (194, 83, 73), (46, 74, 77), (79, 74, 45), (161, 202, 220), (57, 131, 126), (214, 178, 188), (171, 206, 174), (180, 188, 210)]

def main():
    screen = Screen()
    screen.colormode(255)
    turtle = Turtle()
    turtle.shape("circle")
    turtle.speed("fastest")
    turtle.hideturtle()
    
    turtle.setheading(225)
    turtle.penup()
    turtle.forward(300)
    turtle.pendown()
    turtle.setheading(0)

    for i in range(10):
        turtle.color(choice(color_list))
        for j in range(10):
            turtle.dot(20,choice(color_list))
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()
        if i != 10:
            turtle.setheading(180)
            turtle.penup()
            turtle.forward(500)
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(0)
            turtle.pendown()

    
    
    
    
    screen.exitonclick()

main()