def remove_chars(str, n):
  if n < len(str):
      return str[n:]
  else:
      return "n must be less than the length of the string"

# accept a string and an integer from the user
str = input("Please enter a string: ")
n = int(input("Please enter a number: "))

# remove the first n characters from the string
result = remove_chars(str, n)

print("The resulting string is:", result)