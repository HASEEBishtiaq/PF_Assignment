# get input number from user
number = int(input("Enter a number: "))

# reverse the number
reversed_number = 0
original_number = number
while number > 0:
    reversed_number = reversed_number * 10 + (number % 10)
    number //= 10

# check if the number is a palindrome
if original_number == reversed_number:
    print(original_number, "is a palindrome number")
else:
    print(original_number, "is not a palindrome number")