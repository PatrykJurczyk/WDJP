import math

def foo(a: int, b: int , c: int) -> float:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        return -1
    elif (delta == 0):
        x = (-b) / (2 * a)
        return x
    else:
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(foo(6,1,3))
print(foo(1,2,1))
print(foo(1,4,1))

