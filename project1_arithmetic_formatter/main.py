# from arithmetic_arranger import arithmetic_arranger


def arithmetic_arranger(*params):
   for item in params:
     print(item)  output  ['10+12', '15+50']    -- WE HAVE TO CONVERT THIS DATA in to saparate numbers and then creat a tuple and then print that format
      
a = arithmetic_arranger(["10+12","15+50"])
print(a)
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

    