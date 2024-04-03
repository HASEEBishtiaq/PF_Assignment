# accept a string from the user
str = input("Please enter a string: ")

# display characters that are present at an even index number
result = [char for index, char in enumerate(str) if index % 2 == 0]

print("The characters at even index numbers are:")
for char in result:
    print(char)