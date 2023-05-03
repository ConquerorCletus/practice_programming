phone = input("phone number : ")
numbers_in_word = {
    "1": "one",
    "2" : "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "zero"
}
output = ""
for number in phone:
    output += numbers_in_word.get(number) + " "
print(output)
