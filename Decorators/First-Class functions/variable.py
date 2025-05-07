def square(num: float | int) -> float | int:
    return num * num

def cube(num: float | int) -> float | int:
    return num * num * num

#================================================================
# Assign functions square() and cube() as variables to f and g
#================================================================

f = square
print(f(5)) # prints 25

g = cube
print(g(5)) # prints 125