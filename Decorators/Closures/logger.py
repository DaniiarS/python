import logging

#===========================
# SET Logging Config
#===========================

logging.basicConfig(filename="logger.log", level=logging.INFO)

#===========================
# Define logger function
#===========================

def logger(func):
    def display_log(*args):
        logging.info(f"Executing {func.__name__} with arguments {args} - {func(*args)}")
    
    return display_log

def mult(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2

def div(num1: int | float, num2: int | float) -> int | float:
    try:
        result = num1/num2
        return num1/num2
    except ZeroDivisionError as e:
        return e

#===========================
# Test logger
#===========================
my_logger = logger(mult)

my_logger(3,5)
my_logger(10,5)
my_logger(1,0)

another_logger = logger(div)

another_logger(10,5)
another_logger(20,10)
another_logger(1,0)