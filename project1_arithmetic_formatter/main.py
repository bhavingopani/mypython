# from arithmetic_arranger import arithmetic_arranger


# def arithmetic_arranger([a,b,c,d,e]):
#    for item in params:
#      print(item)    # output ['10+12', '15+50']    -- WE HAVE TO CONVERT THIS DATA in to saparate numbers and then creat a tuple and then print that format
#                           #                   CHECK THIS   https://www.studytonight.com/python-howtos/pass-a-list-to-a-function-to-act-as-multiple-arguments
# a = arithmetic_arranger(["32 + 698", "3801 - 2"])
# print(type(a))

# a = "6 + 8"
# b = eval(a)
# print(type(b))
# print(b)


from posixpath import split
from itertools import count


def arithmetic_arranger(list=[], ):   #START FROM HERE https://ivergara.github.io/boolean-arguments-to-functions-in-python.html - Bool or TRUE / FALSE -- WE HAVE TO ADD CONDITION - WHICH WILL BE TRUE OR FALSE>
  for item in list:
    # print(type(item))   - its string
    splitting_string= item.split()   #spliting a string in to ['30', '+', '20']    
    print("  "),
    print(splitting_string[0]),
    print("  "),
    
  print("")
  for itemnew in list:
    splitting_string1 = itemnew.split()
    print(splitting_string1[1]),
    print(""),
    print(splitting_string1[2]),
    print("  "),
  print("")
  
  for i in range(len(list)):
    print("-------"),
    print("  "),
    

arithmetic_arranger(["3252 + 6908", "3801 - 2021", "4015 + 4543", "0123 + 5649"])





# a = "Welcome to"    #THIS IS NOT WORKING -- CHECK WHY ITS NOT SUPPORTED>
# b= "GeeksforGeeks"
# print("  "),
# print(a)      ,
# print(b)

#    32     3801
# + 698   -    2
# -----   -------


# list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# a = tuple(list)
# print(a)

# # def sum_format(a, b ,c ,d ,e ,f):
# #     print()


# # list = [32 + 698, 3801 - 2, 45 + 43, 123 + 49]
# # print(list)

# myinput = "2 + 3"
# mytuple = tuple(map(int, myinput.split(' ')))





# for item in list:
# 	print(item)
# a_list = item.split()
# map_object = map (int, a_list)
# list_of_integers = list(map_object)
# print(list_of_integers)




# numbers = []
# for number in list.split():
#     if number.isdigit():
#         numbers.append(int(number))
# print(numbers)





# from __future__ import print_function
# import re

# a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# print (a)

# b = re.findall( '[0-9]+',a)
# print(b)

# Run unit tests automatically
# main()

# Assignment
# Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

#   235
# +  52
# -----
#   235
# +  52
# -----
# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

# For example
# Function Call:

# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# Output:

#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
# Function Call:

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# Output:

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# Rules
# The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

# Situations that will return an error:
# If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
# The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
# Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
# Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
# If the user supplied the correct format of problems, the conversion you return will follow these rules:
# There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
# Numbers should be right-aligned.
# There should be four spaces between each problem.
# There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
# Development
# Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

# Testing
# The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.