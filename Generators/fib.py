import time

# Generate infinite list of Fibonacci numbers
def fib_nums():
    first, second = 0, 1
    while True:
        time.sleep(1)
        result = first + second
        first = second
        second = result
        yield result

for num in fib_nums():
    print(num)