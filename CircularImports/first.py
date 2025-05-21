

def func_a():
    print("func_a() in module first.py")

from second import func_b

func_a()
func_b()