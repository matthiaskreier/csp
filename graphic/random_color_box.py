import random

dimension = 10

COLORS = (Color.red, Color.orange, Color.yellow, 
          Color.green, Color.blue, Color.black)

for x in range(int(get_width()/dimension)):
    for y in range(int(get_height()/dimension)):
        rect = Rectangle(dimension, dimension)
        rect.set_position(x*dimension, y*dimension)
        # rect.set_color("FF00FF")
        rect.set_color(random.choice(COLORS))
        add(rect)

print("done.")
