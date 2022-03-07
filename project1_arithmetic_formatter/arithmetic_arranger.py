from posixpath import split
from itertools import count

from math import *
import sys


# def arithmetic_arranger(list=[], x=bool):
#     try:
#         for j in list:
#             k = eval(j)
#             o = j.split()
#             if o[1] == '*' or o[1] == '/':
#                 print("Error: Operator must be '+' or '-'.")
#                 sys.exit()
#             if len(o[0]) > 4 or len(o[2]) > 4:
#                 print("Error: Numbers cannot be more than four digits.")
#                 sys.exit()
#     except SyntaxError:
#         print("Error: Numbers must only contain digits.")
#         sys.exit()
#     try:
#         for v in list:
#             c = eval(v)
#     except SyntaxError:
#         print("Error: Numbers must only contain digits.")
#     else:
#         if len(list) < 6:
#             for f in list:
#                 splitting_string = f.split()
#                 max_len_string = max(splitting_string, key=len)
#                 maximum_len_new1 = len(max_len_string)
#                 print(splitting_string[0].rjust(maximum_len_new1 + 2)),
#                 print("  "),
#             print("")
#             for itemnew in list:
#                 splitting_string1 = itemnew.split()
#                 max_len_new2 = max(splitting_string1, key=len)
#                 maximum_len_new2 = len(max_len_new2)  # its not two because its from the operator
#                 print(splitting_string1[1]),
#                 print(splitting_string1[2].rjust(maximum_len_new2)),
#                 print("  "),
#             print("")
#             for b in list:
#                 splitting_b = b.split()
#                 max_len_string1 = max(splitting_b, key=len)
#                 maximum_len_new3 = len(max_len_string1)
#                 print("-" * (maximum_len_new3 + 2)),
#                 print("  "),
#             print("")
#             if x == True:
#                 for u in list:
#                     splitting_u = u.split()
#                     max_len_string2 = max(splitting_u, key=len)
#                     maximum_len_new4 = len(max_len_string2)
#                     x = eval(u)
#                     print(str(x).rjust(maximum_len_new4 + 2)),
#                     print("  "),
#             print("")
#             print("")
#         else:
#             print("Error: Too many problems.")



# arithmetic_arranger(['32 + 6348', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)



# Error: Too many problems.   
# Error: Operator must be '+' or '-'.
# Error: Numbers must only contain digits.
# Error: Numbers cannot be more than four digits.

# too_many_problems=True  #can be done without assuming this or defining it.
# operator_error=True
# numbers_only=True
# four_digits_only=True




def arithmetic_arranger (list, optional_booleon=False):
    list_length = len(list)

    input_list = []
    for i in list:
      input_list.append(i.split())
    #   print(a)
    # sys.exit()
    operator_error=True
    numbers_only=True
    four_digits_only=True

    for j in input_list:
        try:
            if (j[1] != '+') and (j[1] != '-'):    
                operator_error = False
        except:
            continue
        try:
            int(j[0])  #will through an exception if no number digits
            int(j[2])
        except:
            numbers_only = False
        try:
            if (len(j[0]) > 4 or len(j[2]) > 4):
                four_digits_only = False
        except:
            continue

    if list_length > 5:
        return "Error: Too many problems."
    if operator_error== False:
        return "Error: Operator must be '+' or '-'."
    if numbers_only == False:
        return "Error: Numbers must only contain digits."
    if four_digits_only == False:
        return "Error: Numbers cannot be more than four digits."
  #taking this as emppty string value  which we will have to return as output
    operand_1 = ""
    operand_2 = ""
    dash = ""
    result_of_o1_and_o2 = ""

    for k, j in enumerate(input_list):  #enumerate is used when we want to iterate with index and the value -- so later you can print both at the same time
        # print(k)  #will print index  0 , 1 , 2 -- iterate
        # print(j)  #will print the value of j 
        operand_1_length = len(j[0]) #j prints the value so .. getting the length of the same will get operand 1 length
        operand_2_length = len(j[2]) #j prints the value so .. getting the length of the same will get operand 2 length
        num_blanks_1 = 2
        num_blanks_2 = 1
        width = operand_1_length + 2  #as we have  to consider the + and - sign and 1 place between the second operand and + and - sign
        res = 0
        num_blanks_r = 0

        if operand_1_length > operand_2_length:
            num_blanks_2 = 1 + operand_1_length - operand_2_length
        elif operand_1_length < operand_2_length:
            num_blanks_1 = 2 + operand_2_length - operand_1_length
            width = operand_2_length + 2

        operand_1_space = ""
        operand_2_space = ""
        res_space = ""

        for x in range(num_blanks_1):
            operand_1_space = " " + operand_1_space
        for y in range(num_blanks_2):
            operand_2_space = " " + operand_2_space
        for z in range(width):
            dash = dash + "-"

        operand_1 = operand_1 + operand_1_space + j[0]
        operand_2 = operand_2 + j[1] + operand_2_space + j[2]

        if j[1] == "+":
                res = int(j[0]) + int(j[2])
                res_text = str(res)
                num_blanks_r = width - len(res_text)
        elif j[1] == "-":
                res = int(j[0]) - int(j[2])
                res_text = str(res)
                num_blanks_r = width - len(res_text)

        for r in range(num_blanks_r):
                res_space = res_space + " "
                
        result_of_o1_and_o2 = result_of_o1_and_o2 + res_space + res_text

        if k < len(list)-1:
            for d in range(4):
                operand_1  = operand_1 + " "
                operand_2  = operand_2 + " "
                dash = dash + " "
                result_of_o1_and_o2= result_of_o1_and_o2 + " "

    entire_ouput_togather = operand_1 + "\n" + operand_2 + "\n" + dash
    if optional_booleon:
      entire_ouput_togather = entire_ouput_togather + "\n" + result_of_o1_and_o2

    return entire_ouput_togather




# def arithmetic_arranger(list=[], optional_booleon=bool):
    
#     list_length = len(list)
#     # print(list_length)

#     operator_error=True
#     numbers_only=True
#     four_digits_only=True

#     for i in list:
#         # print(i) #print in 32+6348 form
#         # print(type(i)) #str
#         # try:
#         #     converting_i_to_int = eval(i)   #its not the good way to convert something into int... hence dropped.. and it was doing the sum of both the values after converting the int.
#         # except:
#             # numbers_only==False
#             # continue
#         # print(converting_i_to_int)
#         # print(type(converting_i_to_int))  int
#         converting_i_to_list = i.split() #will get ['32','+','3801'] - so that we can access it individually
#         # print(type(int(converting_i_to_list[0])))  #converting to list
#         # print(type(converting_i_to_list)
#         try:
#             if converting_i_to_list[1] == '*' or converting_i_to_list[1] == '/':
#               operator_error == False
#         except:
#             continue  
#         try:
#             int(converting_i_to_list[0])  #trying to convert it to int.. if it throughs an error that means its not an integer or number
#             int(converting_i_to_list[2])
#         except:
#             numbers_only==False
#         try:
#             if len(converting_i_to_list[0]) > 4 or len(converting_i_to_list[2]) > 4:
#                 four_digits_only==False
#         except:
#             continue



#     if list_length > 5:
#         return "Error: Too many problems."
#     if operator_error == False:
#         return  "Error: Operator must be '+' or '-'."
#     if numbers_only==False:
#         return "Error: Numbers must only contain digits."
#     if four_digits_only==False:
#         return "Error: Numbers cannot be more than four digits."



#     # sys.exit()    

#     for j in list:
#         # print(j)  #32 + 6348
#         converting_j_to_list = j.split()  
#         # print(converting_i_to_list_new) #['32','+','3801'] 
#         logenst_string_of_list_j = max(converting_j_to_list, key=len)  #used to know the logest string of any list
#         # print(logenst_string_of_list)  
#         length_of_longest_string_j= len(logenst_string_of_list_j) #know the lenght of the logest string
#         print(converting_j_to_list[0])   #65  \n  32 ...
#         # print(type(converting_j_to_list[0]))  #str
#         print(converting_j_to_list[2])   #652  \n  324
#         # print(type(converting_j_to_list[2]))   #str
                  
        
#         # print(length_of_longest_string) #4
#         # print(converting_j_to_list[0].rjust(length_of_longest_string_j + 2),end="    ") #adjusting to the right
#         # break
#         # print("  "),
#     sys.exit()
#     # print(""),
#     sys.exit()
#     for k in list:
#         # print(k)  #32 + 6348
#         converting_k_to_list = k.split()  
#         # print(converting_k_to_list) #['32','+','3801'] 
#         logenst_string_of_list_k = max(converting_k_to_list, key=len)  #used to know the logest string of any list
#         # print(logenst_string_of_list_k)  
#         length_of_longest_string_k= len(logenst_string_of_list_k) #know the lenght of the logest string
#         # print(length_of_longest_string) #4
#         print(converting_k_to_list[1],end=" ")
#         print(converting_k_to_list[2].rjust(length_of_longest_string_k),end="    ")
#     print(""),
    
#     # sys.exit()
    
#     for l in list:
#         converting_l_to_list = l.split()
#         logenst_string_of_list_l  = max(converting_l_to_list, key=len)
#         length_of_longest_string_l= len(logenst_string_of_list_l)
#         print("-" * (length_of_longest_string_l + 2),end="    "),
#         # print("  "),
#     print("")
#     #START FROM HERE AGAIN.
#     sys.exit()
#     if optional_booleon == True:
#         for m in list:
#             converting_m_to_list = m.split()
#             logenst_string_of_list_m  = max(converting_m_to_list, key=len)
#             length_of_longest_string_m= len(logenst_string_of_list_m)
#             x = int(converting_m_to_list[0]+converting_m_to_list[2])
#             print(str(x).rjust(length_of_longest_string_m + 2),end="")
#             # print("  "),
#     # print("")
#     # print("")



print(arithmetic_arranger(['32 + 6348', '1 - 3801', '45 + 43', '1234 + 49', '988 + 40'], True))