# Nolan Clarke
# Class:CS20
# House
# 30/09/2020
# x is the x of the canvas
# y is the y of the canvas
size(500, 500)


def houseoutline(x, y):
    """houseoutline"""
    rect(x/10, 3*y/10, 21*x/50, 2*y/5)
    triangle(x/10, 3*y/10, 3*x/10, 3*y/50, 13*x/25, 3*y/10)
    square(7*x/50, 8*y/25, x/10)
    square(19*x/50, 8*y/25, x/10)
    rect(8*x/25, 14*y/25, 3*x/25, 7*y/50)
    square(2*x/5, 16*y/25, x/50)


def windows(x, y):
    """windows"""
    line(19*x/100, 8*y/25, 19*x/100, 21*y/50)
    line(7*x/50, 37*y/100, 6*x/25, 37*y/100)
    line(43*x/100, 8*y/25, 43*x/100, 21*y/50)
    line(19*x/50, 37*y/100, 12*x/25, 37*x/100)
    rect(17*x/50, 29*y/50, 2*x/25, x/25)
    line(19*x/50, 29*y/50, 19*x/50, 31*x/50)
    line(17*x/50, 3*y/5, 21*x/50, 3*y/5)
    square(7*x/50, 14*y/25, x/10)
    line(19*x/100, 14*y/25, 19*x/100, 33*y/50)
    line(7*x/50, 61*y/100, 6*x/25, 61*y/100)
    line(7*x/50, y/50, x/5, y/50)
    line(7*x/50, y/50, 7*x/50, y/4)
    line(x/5, y/50, x/5, 9*y/50)
houseoutline(width, height)
windows(width, height)


    
