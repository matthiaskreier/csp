# csp

<img src="graphic/challenge.png" align="right" width="20%">

Some Karel code from CodeHS and Python. And used in the [challenges](https://sites.google.com/ssis.edu.vn/apcsp/home/challenges) on our schools website.

## Efficient Code

[Try for yourself on CodeHS here](https://codehs.com/sandbox/mkreier2022/10-minute-task-2022-09-19) or with this [Task 218](https://codehs.com/sandbox/mkreier2022/mastery-check-module-2-challenge-218) to solve the maze in less steps than 218.

The starting point to the maze looks like the left, the final is the right. What is the minimum amount of lines to solve the maze, put a ball on each spot and face East? The [218 procedural steps](https://github.com/kreier/csp/blob/main/SuperKarel/218steps.py) could possibly be reduced with some algorithms.

<img src="SuperKarel/start.png" width="45%"> <img src="SuperKarel/final.png" width="45%">

### Shortest solution - just 5 lines, Hajoon 2022/09/19

``` py
for i in range(20):
    while front_is_clear():
        move()
        put_ball()
    turn_left()
```

### No condition (if or while) allowed - 6 lines

``` py
x = [9,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0]
for k in range(len(x)):
    for j in range(x[k]):
        move()
        put_ball()
    turn_left()
```

## No lists, arrays or conditional statements (if or while) allowed

### Alex started with just 11:

``` py
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
```

### Thai reduced it to 10 lines

``` py
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
```

#### Update 2022/09/20 - 9 lines is possible

``` py
repeat = 3
for i in range(9,0,-1):
    for j in range(repeat):
        for k in range(i):
            move()
            put_ball()
        turn_left()
    repeat = 2
turn_left()
```

### Update 2022/09/20 - Wayne needed only 8 lines!

``` py
def lane(y):
    for banana in range(y):
        move()
        put_ball()
    turn_left()
lane(9)
for i in range(19):
    lane(-1 * (i/2 - 9))
```
