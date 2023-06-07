def add_function():
    a = eval(input("ENTER THE FIRST NUMBER: "))
    b = eval(input("ENTER THE SECOND NUMBER: "))
    c = a + b
    return(c)
x = add_function()
print("The sum of the number: {}".format(x))
# the def key word is used to define a function.
# def function_name(parameters)