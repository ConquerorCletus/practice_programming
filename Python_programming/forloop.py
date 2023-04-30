prices = [10,20,30]
# prices is the array being iterated 
total = 0

for price in prices:
    #price is being iterated in prices.
    total += price
print("Total = {}".format(total))

print("__________________________________________________________")
# Nested loops
for x in range(4):
    for y in range(3):
        print("{}{}".format(x,y))