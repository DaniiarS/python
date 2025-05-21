""" The confusion of error description with probelm appearing in the second.py is due to the fact that
    when first.py is run directly via "python3 first.py" the name of the module is converted into "__main__" instead of "firsrt".
    That's why it revisits the "first.py" the second time. And beacuse it already visited the "second.py" and could not find the func_b there(beacuse it wasn't delcared on that line yet, it returns the error indicating "second.py' module.)
"""