def square(num: float | int) -> float | int:
    return num * num

def cube(num: float | int) -> float | int:
    return num * num * num

def custom_map(func, arg_list: list[int | float]) -> list[int | float]:
    size = len(arg_list)
    result = [0 for i in range(size)]

    for i in range(size):
        result[i] = func(arg_list[i])
    
    return result

#=====================================================
# Pass a function to another function as an argument
#=====================================================

numbers = [1, 2, 3, 4, 5]

print(custom_map(square, numbers)) # prints: [1, 4, 9, 16, 25]
print(custom_map(cube, numbers))   # prints: [1, 8, 27, 64, 125]
