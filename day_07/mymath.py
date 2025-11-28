def area_triangle(base,height):
    return base * height / 2

# 원주율 값
p1 = 3.141592

def area_circle(radius):
    return radius**2 * p1

def area_prism(lenght, width,  height):
    return 2 * (lenght * width + width * height + lenght * height)
