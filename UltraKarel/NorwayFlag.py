# Norway flag, dimensions: top left 6x6 red, then 1,2,1 white blue white
# Going down this is 6, 4, 6 so 16 height
# Going right this is 6, 4, 11 so 21 width

def go(distance):
    for l in range(distance):
        move()

def rect(x, y, width, height, color_of_rectangle):
    # Let's move to the starting position
    turn_left()
    go(y)
    turn_right()
    go(x)
    # Now paint the rectangle
    for k in range(height):
        for i in range(width - 1):
            paint(color_of_rectangle)
            move()
        paint(color_of_rectangle)
        turn_around()
        go(width - 1)
        if k < (height - 1):
            turn_left()
            move()
            turn_left()
    # Go home
    turn_left()
    go(y - height + 1)
    turn_right()
    go(x)
    turn_around()


# Norway
"""
rect(0, 15, 6, 6, color['red'])
rect(10, 15, 11, 6, color['red'])
rect(0, 5, 6, 6, color['red'])
rect(10, 5, 11, 6, color['red'])
rect(7, 15, 2, 16, color['blue'])
rect(0, 8, 21, 2, color['blue'])
"""

# France
"""
rect(0, 15, 7, 16, color['blue'])
rect(14, 15, 7, 16, color['red'])
"""


# Italy
rect(0, 15, 7, 16, color['green'])
rect(14, 15, 7, 16, color['red'])
