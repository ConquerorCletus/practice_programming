# function to calculate the factorial of a number
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)


num = int(input("Input number: "))
print("Factorial of", num, "is", factorial(num))
