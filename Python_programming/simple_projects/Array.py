arr = [10,20,30,40,50]
# to print the element of array 
print(arr)
# accessing the element using an index
print(arr[0])
print(arr[1])
print(arr[2])
# The negative indexing access the element of the array from the end, more like a reverse form.
print(arr[-1])
print(arr[-2])

brands = ["coke","Apple","Google","Microsoft","Toyota"]
print(brands)
# len is used to find the length of the array
num_brands = len(brands)
print(num_brands)
# expecting to print the length of the array which is stored the variable num_brands
brands.append("Intel")
# the append() function adds an element to the existing array.
print(brands)
# the expecteed output is should include the intel which have been added.
del brands[4]
# The del would delete the 5th the element of array in brands which is toyota
print(brands)
brands.remove("Apple")
# remove is another way of removing element by calling the member directly, the same can be said about pop
print(brands)
brands.pop(0)
print(brands)
brands[0] = "HP"
# The element is directly changed from google to HP by directly reassigning to the index of the array.
print(brands)
arr = arr + [60,70,80]
# concatenating a string with the + operator.
print(arr)
arr = arr * 3
# This would repeat the arr array 3 times. 
print(arr)
newbrands = ["coke","Apple","Google","Microsoft","Toyota"]
print(newbrands)
print(newbrands[1:4])
print(newbrands[:3])
print(newbrands[-4:])
print(newbrands[-3:-1])