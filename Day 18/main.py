# import colorgram
# rgb_colors=[]
# colors= colorgram.extract('Day 18/image.jpg', 80)

# for color in colors:
#     new_color=(color.rgb.r,color.rgb.g,color.rgb.b)
#     rgb_colors.append(new_color)
#print(rgb_colors)
from turtle import Turtle,Screen
import random
color_list=[(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]
t=Turtle()
t.hideturtle()
screen=Screen()
screen.colormode(255)
t.shape('circle')
t.speed("normal")
def draw_dot_row():
    a=10
    for i in range (10):
        t.dot(10,random.choice(color_list))
        t.penup()
        t.forward(25)
        a+=25
        t.pendown()
t.penup()
for i in range(10):
    t.pendown()
    draw_dot_row()
    t.penup()
    t.home()
    x=t.xcor()
    y=t.ycor()
    t.setposition(x,y+((i+1)*25))
    




screen.exitonclick()