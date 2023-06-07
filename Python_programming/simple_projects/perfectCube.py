import math

def PerfectCube(num):
    cube = round(num ** (1/3))
    return cube ** 3 == num

num = int(input("Enter a number: "))

if PerfectCube(num):
    print(num, "is a perfect cube")
else:
    print(num, "is not a perfect cube")
