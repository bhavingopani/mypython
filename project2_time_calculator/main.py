# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("6:30 PM", "205:12"))


# # Run unit tests automatically    
# main(module='test_module', exit=False)

# # days_calculation= divmod(21 , 7)
# # finding_index= days_calculation[1]
# # print(finding_index)

# possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# x=list(enumerate(possible_input_day,1)) #now index will start from 1 instead of 0
# print(x[1][1])

# input_day=""
# print(type(input_day))


# from ast import Str




# def test_time(input_start_time, input_duration_hh_mm , input_day=None):  #*args is not just 1 argument.. it takes multiple argument.. so to access the first one you can aceess it lik args[0]
#     # print(type(*args))
#     print(type(input_day))
#     if type(input_day) == str:
#         print("WHgat")
#         input_day_converted = input_day.upper()
#         print(input_day_converted)
    
    
#     if (type(input_day)) != None:
#         output = input_start_time + " " + input_duration_hh_mm + " " +  input_day.upper()  #*args is not just 1 argument.. it takes multiple argument.. so to access the first one you can aceess it lik args[0]
#     if (type(input_day)) == None:
#         output = input_start_time + " " + input_duration_hh_mm

#     return output


 

   

# print(test_time("3:00 PM", "3:10", "MONDaY") )