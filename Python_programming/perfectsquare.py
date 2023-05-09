import math

def PerfectSquare(num):
    root = int(math.sqrt(num))
    return root * root == num

num = int(input("Enter a number: "))

if PerfectSquare(num):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")
