import random

dimension = 10
width = get_width()
height = get_height()

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: ret = (65536*v + 256*t + p)
    if i == 1: ret = (65536*q + 256*v + p)
    if i == 2: ret = (65536*p + 256*v + t)
    if i == 3: ret = (65536*p + 256*q + v)
    if i == 4: ret = (65536*t + 256*p + v)
    if i == 5: ret = (65536*v + 256*p + q)
    return f"#{ret:06X}"

hue = 0
w_x = int(width/dimension)
w_y = int(height/dimension)
pixel = w_x * w_y
for x in range(w_x):
    print(x)
    for y in range(w_y):
        rect = Rectangle(dimension, dimension)
        rect.set_position(x*dimension, y*dimension)
        hue += 1
        # rect.set_color("#FFC600")
        rect.set_color(hsv_to_rgb(hue/pixel, 1, 1))
        # rect.set_color(rgbhex(rgba(hue/100, 0.5, 0.5)))
        # rect.set_color(hsv_to_rgb(((x + y*width)/(width*height)), 1, 1))
        add(rect)

print("done.")
