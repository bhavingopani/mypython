import sys


# from datetime import datetime


# x = "06:30 PM"
# y = "03:10"

# print( datetime(int(x)) + datetime(int(y)))

# a = x.split()
# print(a)
# print(type(a))

# b=a[0].split()
# print(b)
# print(type(b))


# finale output we want

# output  from    06:30 PM + 03:10  
# print    09:40 PM

input_start_time = "10:10 PM"  # will be a valid time by default
input_duration_hh_mm = "3:30"  # here the minute will be less than 60 whole number by default
input_day = "Monday"
input_day_converted = input_day.upper()
possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
x=list(enumerate(possible_input_day,1))
print(x)
total_days_in_week = 7
# number_of_days = 2
# for i , element in x:
#     if element == input_day_converted:
#         print(i)
#         print(element)
#         print(i, element)
#         if number_of_days <= 7:
#             total = i + number_of_days
#             print(total) 
#             if total == 7:
#                 finding_index =element #its the same
#             if total <7:
#                 sum = i+number_of_days  #here it means 6
#                 if sum <= 7:
#                    finding_index = sum      
#                 if sum > 7:
#                    finding_index= sum - 7
#                    print(finding_index)

# print(x[finding_index])
# print(element)                 
                
# sys.exit()
x1 = input_start_time.split()
print(x1)  # ['09:40', 'PM']
x2 = x1[0].split(":")
print(x2) #['09', '40']


y1 = input_duration_hh_mm.split(":")
print(y1)  # ['02', '19']

hrs = int(x2[0]) + int(y1[0])
mm = int(x2[1]) + int(y1[1])
am_pm = x1[1]
print(hrs)
print(mm)
# x = "days later"
# x = "next day"
# n = 10


# print(int(x2[0]))
# print(hrs)


# print(am_pm)

if mm == 60:
    mm = 00
    hrs = hrs + 1
elif mm > 59:
    mm = (mm - 60)
    hrs = hrs + 1

print(hrs)
print(mm)

print("--------------")

number_of_days = int(hrs / 24)
print(number_of_days)
# sys.exit()
print("----")
# possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
for i , element in x:
    if element == input_day_converted:
        print(i)
        print(element)
        print(i, element)
        print(number_of_days)
        total = int(i) + int(number_of_days)
        print(total)
        if number_of_days <= 7:
            # total = i + number_of_days
            # print(total) 
            if total == 7:
                finding_index =i #its the same
            elif total <7:
                # total = i+number_of_days  #here it means 6
                finding_index = total      
        if total > 7:
            days_calculation= divmod(total , 7)
            print(days_calculation)
            print(days_calculation[1])
            x= i +days_calculation[1]
            print(x)
            if x<=7:
                finding_index = x
            if x>7:
                # print(days_calculation)
                # print(days_calculation[1])
                finding_index = x -7 
                print(finding_index)
                # finding_index = 

output_day=possible_input_day[finding_index-1]
# print(output)

# sys.exit()  
    
    # t_hrs=divmod(hrs, 12)  #built-in function we can use to find qaotient and remainder
    # if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
    #     am_pm = "AM"
    #     hrs = int(x2[0]) 
    #     hrs =  int(x2[0]) + int(t_hrs[1])
    #     if hrs > 12:
    #         hrs = hrs - 12
                
                
                #    finding_index= sum - 7
                #    print(finding_index)
# print(number_of_days)
# sys.exit()

# sys.exit()
if 12 < hrs < 24 and am_pm == "PM":
    hrs = hrs - 12
    am_pm = "AM"  # it changes at every 12 hrs addition -- SO its <24 .. did not consider the case of 24 - because that will be again PM too.
    # this indicates next day
elif 12 < hrs < 24 and am_pm == "AM":
    hrs = hrs - 12
    am_pm = "PM"  # same logic as above
    # this indicates next day
# if more than 1 day
# hrs1 = 24
if hrs == 12 and am_pm == "AM":
    hrs = hrs
    am_pm = "PM"
    # n_days = "next day"

elif hrs == 12 and am_pm == "PM":
    hrs = hrs
    am_pm = "AM"
    # n_days = "next day"
if hrs == 24 and am_pm == "AM":
    hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
    am_pm = "AM"  # after 24 hrs it will be AM only.

    # n_days = ???
elif hrs == 24 and am_pm == "PM":
    hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
    am_pm = "PM"  # after 24 hrs it will be AM only.
# print(hrs)

if hrs > 24 and am_pm == "AM":
    t_hrs = divmod(hrs, 12)  # built-in function we can use to find qaotient and remainder
    if (t_hrs[
            0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
        am_pm = "AM"
        # hrs = int(x2[0])
        hrs = int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
    if (t_hrs[
            0] % 2) == 1:  # its odd .. meaning 23/12   -- if the quotient is odd  here value is 1 Change am_pm and 11 styas the smae.
        am_pm = "PM"
        hrs = int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
    # print(hrs)
# sys.exit()            
elif hrs > 24 and am_pm == "PM":
    t_hrs = divmod(hrs, 12)
    if (t_hrs[
            0] % 2) == 0:  # it means its its Even for example 24/12 is even that means after 24 hrs its going to be same am_pm
        am_pm = "PM"
        hrs = int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
            am_pm = "AM"
    if (t_hrs[
            0] % 2) == 1:  # its odd .. meaning 23/12   -- can not devide which means 12 and 11   +12 is Change am_pm and 11 styas the smae.
        am_pm = "AM"
        hrs = int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
            am_pm = "PM"

        # print(number_of_days)

if 1 < number_of_days < 2:
    n_days = "next day"
elif number_of_days > 2:
    n = number_of_days
    n_days = str(n) + " " + "days later"
    print(n_days)


print(hrs)
print(f"{mm:02d}")
print(am_pm)
# print(n_days)
print(output_day)
# hrs = "09"    #
# minutes = "40"  # will be a while number less than 60  By default user knows that
# hrs_m = "09:40"
# am_pm = "PM"

# output = hrs+ ":" + minutes + " " + am_pm
# print(output)


















# # ==========


# input_start_time = "3:30 PM"  # will be a valid time by default
# input_duration_hh_mm = "2:12"  # here the minute will be less than 60 whole number by default
# input_day = "Monday"
# input_day_converted = input_day.upper()
# possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# x=list(enumerate(possible_input_day,1))
# print("-")
# print(x)
# print('--')
# total_days_in_week = 7
# # number_of_days = 2
# # for i , element in x:
# #     if element == input_day_converted:
# #         print(i)
# #         print(element)
# #         print(i, element)
# #         if number_of_days <= 7:
# #             total = i + number_of_days
# #             print(total) 
# #             if total == 7:
# #                 finding_index =element #its the same
# #             if total <7:
# #                 sum = i+number_of_days  #here it means 6
# #                 if sum <= 7:
# #                    finding_index = sum      
# #                 if sum > 7:
# #                    finding_index= sum - 7
# #                    print(finding_index)

# # print(x[finding_index])
# # print(element)                 
                
# # sys.exit()
# x1 = input_start_time.split()
# print(x1)  # ['09:40', 'PM']
# x2 = x1[0].split(":")
# print(x2) #['09', '40']


# y1 = input_duration_hh_mm.split(":")
# print(y1)  # ['02', '19']

# hrs = int(x2[0]) + int(y1[0])
# mm = int(x2[1]) + int(y1[1])
# am_pm = x1[1]
# print("---")
# print(hrs)
# print(mm)
# print("----")
# # x = "days later"
# # x = "next day"
# # n = 10


# # print(int(x2[0]))
# # print(hrs)


# # print(am_pm)

# if mm == 60:
#     mm = 00
#     hrs = hrs + 1
# elif mm > 59:
#     mm = (mm - 60)
#     hrs = hrs + 1
# print("-----")
# print(hrs)
# print(mm)
# print("------")

# number_of_days = int(hrs / 24)

# print("+++-------")
# print(number_of_days)
# # sys.exit()
# print("--------")
# # possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']




# for i , element in x:
#     if element == input_day_converted:
#         print("---------")
#         print(i)
#         print(element)
#         print(i, element)
#         print("----------")
#         print(number_of_days)
#         total = int(i) + int(number_of_days)
#         print(total)
#         print("------------")
#         if number_of_days <= 7:
#             # total = i + number_of_days
#             # print(total) 
#             if total == 7:
#                 finding_index =i #its the same
#             elif total <7:
#                 # total = i+number_of_days  #here it means 6
#                 finding_index = total      
#         if total > 7:
#             days_calculation= divmod(total , 7)
#             print("=-----------")
#             print(days_calculation)
#             print(days_calculation[1])
#             print("=---------------")
#             x= i +days_calculation[1]
#             print("=----------------")
#             print(x)
#             print("=-----------------")
#             if x<=7:
#                 finding_index = x
#                 print("===")
#                 print(finding_index)
#                 print("===")
#             if x>7:
#                 # print(days_calculation)
#                 # print(days_calculation[1])
#                 finding_index = x -7
#                 print("=============") 
#                 print(finding_index)
#                 # finding_index = 
#                 print("=============")
# output_day=possible_input_day[finding_index-1]
# # print(output)

# # sys.exit()  
    
#     # t_hrs=divmod(hrs, 12)  #built-in function we can use to find qaotient and remainder
#     # if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
#     #     am_pm = "AM"
#     #     hrs = int(x2[0]) 
#     #     hrs =  int(x2[0]) + int(t_hrs[1])
#     #     if hrs > 12:
#     #         hrs = hrs - 12
                
                
#                 #    finding_index= sum - 7
#                 #    print(finding_index)
# # print(number_of_days)
# # sys.exit()

# # sys.exit()
# if 12 < hrs < 24 and am_pm == "PM":
#     hrs = hrs - 12
#     am_pm = "AM"  # it changes at every 12 hrs addition -- SO its <24 .. did not consider the case of 24 - because that will be again PM too.
#     # this indicates next day
# elif 12 < hrs < 24 and am_pm == "AM":
#     hrs = hrs - 12
#     am_pm = "PM"  # same logic as above
#     # this indicates next day
# # if more than 1 day
# # hrs1 = 24
# if hrs == 12 and am_pm == "AM":
#     hrs = hrs
#     am_pm = "PM"
#     # n_days = "next day"

# elif hrs == 12 and am_pm == "PM":
#     hrs = hrs
#     am_pm = "AM"
#     # n_days = "next day"
# if hrs == 24 and am_pm == "AM":
#     hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
#     am_pm = "AM"  # after 24 hrs it will be AM only.

#     # n_days = ???
# elif hrs == 24 and am_pm == "PM":
#     hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
#     am_pm = "PM"  # after 24 hrs it will be AM only.
# # print(hrs)

# if hrs > 24 and am_pm == "AM":
#     t_hrs = divmod(hrs, 12)  # built-in function we can use to find qaotient and remainder
#     if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
#         am_pm = "AM"
#         # hrs = int(x2[0])
#         hrs = int(x2[0]) + int(t_hrs[1])
#         if hrs > 12:
#             hrs = hrs - 12
#     if (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- if the quotient is odd  here value is 1 Change am_pm and 11 styas the smae.
#         am_pm = "PM"
#         hrs = int(x2[0]) + int(t_hrs[1])
#         if hrs > 12:
#             hrs = hrs - 12
#     # print(hrs)
# # sys.exit()            
# elif hrs > 24 and am_pm == "PM":
#     t_hrs = divmod(hrs, 12)
#     if (t_hrs[0] % 2) == 0:  # it means its its Even for example 24/12 is even that means after 24 hrs its going to be same am_pm
#         am_pm = "PM"
#         hrs = int(x2[0]) + int(t_hrs[1])
#         if hrs > 12:
#             hrs = hrs - 12
#             am_pm = "AM"
#     if (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- can not devide which means 12 and 11   +12 is Change am_pm and 11 styas the smae.
#         am_pm = "AM"
#         hrs = int(x2[0]) + int(t_hrs[1])
#         if hrs > 12:
#             hrs = hrs - 12
#             am_pm = "PM"

# # print(number_of_days)
# # n_days = "next day"
# # print("=")
# # print(n_days)
# # print("=")


# # if number_of_days == 0:
# #     pass

# if 1 < number_of_days < 2:
#     n_days = "next day"
#     print("=")
#     print(type(n_days))
#     print(n_days)
#     print("=")
# if number_of_days > 2:
#     n = number_of_days
#     n_days = str(n) + " " + "days later"
#     print("===")
#     print(n_days)
#     print("===")

# print("=-=-=-=--=-=-=-=-=-=")
# print(hrs)
# print(f"{mm:02d}")
# print(am_pm)
# # print(n_days)
# print(output_day)
# print("=-=-=-=--=-=-=-=-=-=")






# # hrs = "09"    #
# # minutes = "40"  # will be a while number less than 60  By default user knows that
# # hrs_m = "09:40"
# # am_pm = "PM"

# # final_output = hrs + ":" + f"{mm:02d}" + " " + am_pm , str(output_day) , n + "days later"
# # print(final_output)

# #condition 1
#    #if input_day mentioned then print the day ..
#         #the same day if the time is on the same day
#         #print next day if the output day is on the next day
#         #print the respective day if the output day is not on the same or next day - Also print n days later with the day too 
# #condition 2
#     #if input day is not metioned
#         #then dont print any day if its on the same day.
#         #then print next day if the output day is on the next day
#         #then if its more than 1 day
#             #then print only n days later
            
    
# # add_time("3:00 PM", "3:10")
# # # Returns: 6:10 PM

# # add_time("11:30 AM", "2:32", "Monday")
# # # Returns: 2:02 PM, Monday

# # add_time("11:43 AM", "00:20")
# # # Returns: 12:03 PM

# # add_time("10:10 PM", "3:30")
# # # Returns: 1:40 AM (next day)

# # add_time("11:43 PM", "24:20", "tueSday")
# # # Returns: 12:03 AM, Thursday (2 days later)

# # add_time("6:30 PM", "205:12")
# # # Returns: 7:42 AM (9 days later)