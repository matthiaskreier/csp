# 218 lines of code - make it shorter!

move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
move()
put_ball()
turn_left()
move()
put_ball()
turn_left()
move()
put_ball()
turn_left()
turn_left()

# -----------------------------------------------------------------------------

# 7 lines Mr. K using if
"""
for i in range(117):
    if front_is_clear():
        move()
        put_ball()
    else:
        turn_left()
turn_around()
"""


# 6 lines from Wayne
"""
for i in range(119):
    if front_is_clear():
        move()
        put_ball()
    else:
        turn_left()
"""


# 5 lines from Hajoon 
"""
for i in range(20):
    while front_is_clear():
        move()
        put_ball()
    turn_left()
"""


# -----------------------------------------------------------------------------

# Now WITHOUT CONDITIONAL STATEMENTS like if or while

# 7 lines Mr. K
"""
x = [9,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1]
for k in range(len(x)):
    for j in range(x[k]):
        move()
        put_ball()
    turn_left()
turn_left()
"""



# 6 lines  - updated
"""
x = [9,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0]
for k in range(len(x)):
    for j in range(x[k]):
        move()
        put_ball()
    turn_left()
"""


# -----------------------------------------------------------------------------

# Without a list or conditional statements

# 11 lines by Alex
"""
for i in range(9):
    move()
    put_ball()
turn_left()
for i in range(9):
    for j in range(2):
        for k in range(9-i):
            move()
            put_ball()
        turn_left()
turn_left()
"""

"""
for i in range(9):
    move()
    put_ball()
turn_left()
for i in range(9,0,-1):
    for k in range(2):
        for j in range(i):
            move()
            put_ball()
        turn_left()
turn_left()
"""

# 10 lines by Thai
"""
row, repeat = 9, 3
for i in range(9):
    for j in range(repeat):
        for k in range(row):
            move()
            put_ball()
        turn_left()
    repeat = 2
    row -= 1
turn_left()
"""

# 8 lines by Wayne
"""
def lane(y):
    for banana in range(y):
        move()
        put_ball()
    turn_left()
lane(9)
for i in range(19):
    lane(-1 * (i/2 - 9))
"""

# 5 lines