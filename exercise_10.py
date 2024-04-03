# get input integer from user
number = int(input("Enter an integer: "))

# extract digits from integer in reverse order
digits = []
while number > 0:
    digits.append(number % 10)
    number //= 10

# print digits with space separating them
print(*digits[::-1])