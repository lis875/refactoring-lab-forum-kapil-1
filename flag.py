from turtle import *

def colored_rectangle(text_color,width,height):
    color(text_color)
    begin_fill()
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()

def move_next():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()