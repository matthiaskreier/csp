import random

dimension = 10

COLORS = (Color.red, Color.orange, Color.yellow, 
          Color.green, Color.blue, Color.black)

def rgb(h, s, v):
    i = math.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]
    decimal = r * 65536 + g * 256 + b

    return "#"+hex(int(decimal*256))[2:]

for x in range(int(get_width()/dimension)):
    for y in range(int(get_height()/dimension)):
        rect = Rectangle(dimension, dimension)
        rect.set_position(x*dimension, y*dimension)
        rect.set_color(rgb(random.random(), 0.5, 0.5))
        # rect.set_color("#FF00FF")
        # rect.set_color(random.choice(COLORS))
        add(rect)

print("done.")
