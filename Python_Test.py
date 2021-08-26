#      # this is how you import stuff

# This is how you make comments in python !

###########################################
# Variables and Printing

print()
word = "Hi World"
myNum = -5
print(word)
print(abs(myNum))
print("")

###########################################
# Take Input

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!")
# print("You are " + age + ".")

###########################################
# Basic Addition Calculator

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# By default input() takes all input as a string, so if you want a number you have to convert it
# can use int() or float()
# result = float(num1) + float(num2)
#
# print(result)

###########################################
# Mad Libs

# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

###########################################
# Lists (Kinda like arrays)

# Lists can take elements of different data types, it accepts them all
# test_list = ["Kevin", 2, True]

# friends = ["Kevin", "Karen", "Jim", "Sara", "Alice"]
# print(friends[1:3])
# print(friends[1:])
# print(friends[-1])
# friends[2] = "Jorge"
# print(friends[2])

###########################################
# List Functions

# lucky_nums = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Sara", "Alice"]
# friends.extend(lucky_nums) # adds two lists together
# friends.append("Jeff") # adds to the end of the list
# friends.insert(1, "Kelly")  # inserts element at certain index
# friends.remove("Jim")
# friends.clear()   # empties list
# friends.pop()   # removes last element in list
# print("Jim is at index: " + str(friends.index("Jim")))    # prints index of stated element
# print("The number of Jims is: " + str(friends.count("Jim")))   # counts the instances of the element
# lucky_nums.reverse()   # reverses the list

# friends2 = friends.copy()
#
# print(lucky_nums)
# print(friends)
# print(friends2)
###########################################
# Tuples (a type of data structure kinda like a list)

# coordinates = (4,5)   # Tuples cannot be modified after its creation!!!!
# # coordinates[1] = 10     # this will get an error since tuples cant be changed
#
# coordinates_two = [(4,5) , (3,9) , (1,6) , (2,8)]
# print(coordinates[0])
# print(coordinates_two[1])

###########################################
# Functions

# def say_hi():
#     print("Hi User! :D")
#
# say_hi()
#
# def say_hi(name, age):
#     print("Hi " + name + "! :D")
#     print("You are " + str(age) + "!")
#
# say_hi("Chris", 21)

###########################################
# Return Statements
#
# def cube(num):
#     return num*num*num
#
# result = cube(4)
# print(result)
# print(cube(3))

###########################################
# If Statements

# is_male = False
# is_tall = True
#
# if is_male or is_tall:
#     print("You are a male or tall or both!")
# elif is_male and not(is_tall):
#     print("You are a short male!")
# elif not(is_male) and is_tall:
#     print("You are a tall female!")
# else:
#     print("You aren't male nor tall!")

###########################################
# Comparisons
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#     # ==, != also work here
#
# print("The max num is: " + str(max_num(3,40,5)) )

###########################################
# Better Calculator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid Operator")

###########################################
# Dictionaries

# cant have duplicate "keys"
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     10: "Test"
# }

# print(monthConversions["Jan"])
# print(monthConversions.get("Feb"))
# print(monthConversions.get("Luv", "Not a valid key"))
# print(monthConversions[10])

###########################################
# While Loops
















