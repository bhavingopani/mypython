# from arithmetic_arranger import arithmetic_arranger
# a = "6 + 8"
# b = eval(a)
# print(type(b))
# print(b)

  #    Error: Operator must be '+' or '-'.


from posixpath import split
from itertools import count
import sys



# list = ['23', '+', '40']

# if list[1] != '+' or list[1] != '-':
#   sys.exit("Error: Operator must be '+' or '-'.")  


def arithmetic_arranger(list=[], x = bool): 
    # max_len = -1
    # for q in list:
    #   # g = eval(q)
    #   p = q.split()
    #   print(type(p))
    #   # if len(p) > max_len:
    #   #   max_len = len(p)
    #   max_len=max(p,key=len)
    #   print(max_len)
    #   print(len(max_len))
      
       
    try:
      for j in list:
        k = eval(j)
        o = j.split()
        if o[1] == '*' or o[1] == '/':
          print("Error: Operator must be '+' or '-'.")
          sys.exit()
        if len(o[0]) > 4 or len(o[2]) > 4:
          print("Error: Numbers cannot be more than four digits.")
          sys.exit()  #we could have passed the above print statement here.. But the program could not have stopped with exit code 0 - that means it was not terminated successfully. That's why we added that in diffrent print statement
    except SyntaxError:
      print("Error: Numbers must only contain digits.")
      sys.exit()
    
    try:
      for v in list: 
        c=eval(v)     
    except SyntaxError:
      print("Error: Numbers must only contain digits.")
    else: 
      if len(list) < 6:
        for f in list:
          # print(type(item))   - its string
          splitting_string= f.split()   #spliting a string in to ['30', '+', '20']    
          max_len_string=max(splitting_string,key=len)
          # print(max_len_string)
          maximum_len_new1= len(max_len_string)
          # print(maximum_len_new1)
          # len_of_first_element= len(splitting_string[0])   #as we want to make the 1 space from operater and if its one line than max space of charactor of the largest + 'space of operator'
          # print(maximum_len)
          # print(maximum_len)
          # print(" "),   #LOGEST OF OPERANDS AND OPERATOR SHOULD HAVE 1 SPACE ONLY --- first row starting from the 1st number
          # str = splitting_string[0]
          # e = numpy.char.rjust
          # print(maximum_len)
          # print(type(maximum_len))
          # print(type(splitting_string[0]))
          print(splitting_string[0].rjust(maximum_len_new1 + 2 )), # 1 for operater and 1 for (between the 2nd operand and operater there will be 1 space ..so 2 space.)
          # print(splitting_string[0]),
          # print(""),  #by default there is one space here and 1 space of print statement and join... and 2 space we give.. So total 4 spaces
          # 
          print("  "),  #3 spaces -- as its not dynamic -- 1 by defaut and 3 we added -- so that both the problem has 4 spaces in between
        print("")  #for new line
        # sys.exit()
        for itemnew in list:
          splitting_string1 = itemnew.split()
          max_len_new2=max(splitting_string1,key=len)
          maximum_len_new2= len(max_len_new2)   #its not two because its from the operator
          # len_of_second_element= len(splitting_string1[2]) 
          # print(maximum_len_new)
          # print(""), #4 spaces required
          print(splitting_string1[1]), #4 spaces required so.
          # print(""),
          # print(maximum_len_new2)
          print(splitting_string1[2].rjust(maximum_len_new2)),  
          # print(splitting_string1[2]),
          print("  "),   #4 spaces - no need any dynamic value
        print("")   #for new line
        
        for b in list:
          splitting_b = b.split()
          max_len_string1=max(splitting_b,key=len)
          maximum_len_new3= len(max_len_string1) 
          print("-"*(maximum_len_new3+2)),
          # print("-------"),
          print("  "),
          
        print("") #for new line
        if x == True:
          for u in list:
            splitting_u = u.split()
            max_len_string2=max(splitting_u,key=len)
            maximum_len_new4= len(max_len_string2) 
            # print(maximum_len_new4)
            
            x = eval(u)
            # print(""),
            print(str(x).rjust(maximum_len_new4+2)),
            print("  "),
      
      
      else:
        print("Error: Too many problems.") 
      # else:    
      #   sys.exit("Error: Operator must be '+' or '-'.")
    # print("out of loop")     
        


arithmetic_arranger(["345 - 6584", "301 + 2243", "4015 + 4543", "123 + 649", "4007 + 5543"],True)





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