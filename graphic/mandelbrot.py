# Mandelbrot graph

minX = -2.0
maxX = 1.0
width = get_width()
height = get_height()
aspectRatio = 1

chars = [Color.red, Color.green, Color.blue, Color.yellow, Color.cyan,
    Color.orange, Color.white, Color.black, Color.gray, Color.purple,
    Color.red, Color.green, Color.blue, Color.yellow, Color.cyan,
    Color.orange, Color.white, Color.black, Color.gray, Color.purple]

yScale = (maxX-minX)*(float(height)/width)*aspectRatio

for y in range(height):
    for x in range(width):
        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for char in chars:
            if abs(z) > 2:
                break
            z = z*z+c
        rect = Rectangle(1, 1)
        rect.set_color(char)
        rect.set_position(x, y)
        add(rect)
