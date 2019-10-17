# x is the x of the canvas
# y is the y of the canvas

size(500, 500)
def tictactoe(x, y):
    """Tic Tac Toe Grid"""
    # top horizontal line
    line(0, y/3, x, y/3)
    # bottom horizontal line
    line(0, 2*y/3, x, 2*y/3)
    # left vertical line
    line(x/3, 0, x/3, y)
    # right vertical line
    line(2*x/3, 0, 2*x/3, y)

def cross(x, y):
    """cross symbol"""
    line(0, 0, x/3, y/3)
    line(0, y/3, x/3, 0)

def circles(x, y):
    """circle symbols in the middle row"""
    # middle circle
    circle(x/2, y/2, x/3)
    # left circle
    circle(x/6, y/2, x/3)
    # right circle
    circle(5*x/6, y/2, x/3)

def drawImage(x, y):
    tictactoe(x, y)
    circles(x, y)
    cross(x, y)

drawImage(width, height)
