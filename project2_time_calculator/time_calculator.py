
import sys

from numpy import empty





def add_time(input_start_time, input_duration_hh_mm , input_day=empty): #hear input_day is optional
    
    

    # if input_day == str:
    #     print("WHgat")
    #     input_day_converted = input_day.upper()
        # print(input_day_converted)
    # sys.exit()
    # print(input_day_converted)
    # sys.exit()
    possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    x=list(enumerate(possible_input_day,1)) #now index will start from 1 instead of 0
    
    
    x1 = input_start_time.split() #separating and converting the string in to list so that we can access individual string
    # print(x1)  # ['09:40', 'PM']
    x2 = x1[0].split(":") #splitting or separating the first 09:40 by : so that we can access them indidually too.
    # print(x2) #['09', '40']


    y1 = input_duration_hh_mm.split(":") #input in that string  by user splitting that hr and min by :
    # print(y1)  # ['02', '19']

    hrs = int(x2[0]) + int(y1[0])  #total hrs after totalling the 09:40 PM

    mm = int(x2[1]) + int(y1[1])
    am_pm = x1[1] #assigning the user input of AM or PM to the am_pm
    # print("---") 
    # print(hrs) #to ceck the value
    # print(mm)  #to check the mm value
    

    if mm == 60:
        mm = 00
        hrs = hrs + 1
    elif mm > 59: 
        mm = (mm - 60)
        hrs = hrs + 1
    # # print("-----")
    # print(hrs) #checking again after the above check
    # print(mm)
    # print("------")
    days_hrs_calculation = divmod(hrs, 24)
    number_of_days = days_hrs_calculation[0]
    number_of_hrs_left = days_hrs_calculation[1]
    # number_of_days = int(hrs / 24) #finding the number of total days to count after hh mm counting
    # print(number_of_days)
    # sys.exit()
    # print("+++-------")
    # print(number_of_days) #total days to count after indexing
    # sys.exit()
    # print("--------")
    # possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    # if input_day != None: ??
    for i in x:
        # print(element)
        # break
        # if input_day == str:  
        # if element == input_day:
                # print("---------")
                # print(i) #printing the index of matched days
                # print(element) #printing the respective day 
                # print(i, element) #printing respective index and element
                # print("----------")
                # print(number_of_days)  #number_original days to count. with addition of of hrs and mms
                total = int(i[0]) + int(number_of_days)  #original index number of the day in the list + number_of_days
                # print(total)
                # sys.exit()
                # finding_index = int[i]
                if number_of_days <= 7:
                    if number_of_days == 7:
                            finding_index = int(i[0]) #its the same i is the index of the input_day in the list  -- index of the list monday to tuesday - starting from 1 to 7 == to find our answer
                    elif number_of_days < 7:
                        if total > 7:
                            days_calculation= divmod(total , 7)
                            finding_index= days_calculation[1]
                            if finding_index == 0:
                                finding_index = 7
                        elif total <= 7:
                            finding_index = total
                        # if total == 0:
                        #     finding_index  
                elif number_of_days > 7:
                    days_calculation= divmod(total , 7)
                    finding_index= days_calculation[1]
                    if finding_index == 0:
                        finding_index = 7
      
    
    # sys.exit()
    output_day = x[finding_index-1][1]  #possible_input_day -index starts with 0 -- so we are doing -1 as ours is as per 1
    # print(output_day)
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
    elif hrs == 12 and am_pm == "AM":
        hrs = hrs
        am_pm = "PM"
        # n_days = "next day"

    elif hrs == 12 and am_pm == "PM":
        hrs = hrs
        am_pm = "AM"
        # n_days = "next day"
    elif hrs == 24 and am_pm == "AM":
        hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
        am_pm = "AM"      # after 24 hrs it will be AM only.

        # n_days = ???
    elif hrs == 24 and am_pm == "PM":
        hrs = int(x2[0])  # it stays the same .. after 24 hrs -- time will be same
        am_pm = "PM"  # after 24 hrs it will be AM only.
    # print(hrs)

    elif hrs > 24 and am_pm == "AM":
        t_hrs = divmod(hrs, 12)  # built-in function we can use to find qaotient and remainder
        if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
            am_pm = "AM"
            # hrs = int(x2[0])
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
        elif (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- if the quotient is odd  here value is 1 Change am_pm and 11 styas the smae.
            am_pm = "PM"
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
        # print(hrs)
        # sys.exit()            
    elif hrs > 24 and am_pm == "PM":
        t_hrs = divmod(hrs, 12)
        if (t_hrs[0] % 2) == 0:  # it means its its Even for example 24/12 is even that means after 24 hrs its going to be same am_pm
            am_pm = "PM"
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
                am_pm = "AM"
        elif (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- can not devide which means 12 and 11   +12 is Change am_pm and 11 styas the smae.
            am_pm = "AM"
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
                am_pm = "PM"
    # sys.exit()
    # global final_output    
    if input_day == empty:
        # global final_output
        if number_of_days > 1 and number_of_days < 2:
            n_days_later = "(next day)"
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm
            # final_output = hrs + ":" + f"{mm:02d}" + " " + am_pm + " " + after_n_days / next day
        elif number_of_days < 1:
            n_days_later = empty   #??? #HAVE TO ADD LOGIC FOR AM AND PM CHANGE --- < 1 Does not always Answer the question like Next Day.
            if am_pm != x1[1] and x1[1] == "PM" :
                n_days_later = "(next day)"
                final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + " " + n_days_later
            else:
                final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm
            # final_output with nothing or no day just time and minuet
        elif number_of_days >= 2:
            n_days_later = "(" + str(number_of_days) + " " + "days later)"
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + " " + n_days_later
        elif number_of_days == 1:
            n_days_later = "(next day)"
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + " " + n_days_later
            # final output with n days later

        # final_output = str(hrs) + ":" + f"{mm:02d}" + "  " + am_pm + " " + n_days_later    
            # final_output= str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + " " + n_days_later    
        
        # print(type(input_day))
    # if input_day == str:
    # elif input_day == str:
    # if input_day == empty:
        # global final_output 
    
    # sys.exit()
    else:
        if number_of_days > 1 and number_of_days < 2:
            # global final_output
            final_output_day = output_day
            n_days_later = "(next day)"
            # global final_output
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + "," + " " + final_output_day + n_days_later
        elif number_of_days < 1:
            # global final_output
            final_output_day = input_day  #monday
            n_days_later = empty
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + "," + " " + final_output_day
        elif number_of_days >= 2:
            # global final_output
            final_output_day = output_day
            n_days_later = "(" + str(number_of_days) + " " + "days later)"
            final_output = str(hrs) + ":" + f"{mm:02d}" + " " + am_pm + "," + " " + final_output_day + n_days_later
    
    return final_output
    # return final_output

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)
# add_time("11:43 PM", "24:20", "tueSday")  # NOT PASSED
#     #Traceback (most recent call last):
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 282, in <module>
#     add_time("3:00 PM", "3:10")
# TypeError: add_time() missing 1 required positional argument: 'input_day'

# add_time("11:30 AM", "2:32", "Monday") #PASSED
# add_time("11:30 AM", "2:32", "Monday")

# add_time("11:43 AM", "00:20") # NOT PASSED
# Traceback (most recent call last):
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 288, in <module>
#     add_time("11:43 AM", "00:20") 
# TypeError: add_time() missing 1 required positional argument: 'input_day'

# add_time("10:10 PM", "3:30") # NOT PASSED
# Traceback (most recent call last):
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 294, in <module>
#     add_time("10:10 PM", "3:30")
# TypeError: add_time() missing 1 required positional argument: 'input_day'

# add_time("11:43 PM", "24:20", "tueSday") #NOT PASSED
# Traceback (most recent call last):
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 302, in <module>
#     add_time("11:43 PM", "24:20", "tueSday")
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 259, in add_time
#     final_output = str(hrs) + ":" + f"{mm:02d}" + am_pm + "," + " " + final_output_day + n_days_later
# UnboundLocalError: local variable 'final_output_day' referenced before assignment

# add_time("6:30 PM", "205:12")   # NOT PASSED
# Traceback (most recent call last):
#   File "/home/g21/Projects/mypython/project2_time_calculator/test_code.py", line 310, in <module>
#     add_time("6:30 PM", "205:12")   # NOT PASSED
# TypeError: add_time() missing 1 required positional argument: 'input_day'