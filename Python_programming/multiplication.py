# Get the size of the multiplication table, this would generate from 1 - given size specified.
size = int(input("Enter the size of the multiplication table: "))

# Create the multiplication table
for i in range(1, size+1):
    for j in range(1, size+1):
        print(i*j, end='\t')
    print()
