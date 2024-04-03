# define the two lists of numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# create a new list with odd numbers from first list and even numbers from second list
new_list = [num for num in list1 if num % 2 == 1] + [num for num in list2 if num % 2 == 0]

# print the new list
print(new_list)