# import sys



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
# # print    09:40 PM
# input_day=None
# if type(input_day)== None:
#     print("yes its none")
# sys.exit()
def add_time(input_start_time, input_duration_hh_mm , input_day): #hear input_day is optional





    # input_start_time = "3:30 PM"  # will be a valid time by default
    # input_duration_hh_mm = "2:12"  # here the minute will be less than 60 whole number by default
    # input_day = "Monday"
    input_day_converted = input_day.upper()
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

    number_of_days = int(hrs / 24) #finding the number of total days to count after hh mm counting

    # print("+++-------")
    # print(number_of_days) #total days to count after indexing
    # sys.exit()
    # print("--------")
    # possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    for i , element in x:
        if element == input_day_converted:
            # print("---------")
            # print(i) #printing the index of matched days
            # print(element) #printing the respective day 
            # print(i, element) #printing respective index and element
            # print("----------")
            # print(number_of_days)  #number_original days to count. with addition of of hrs and mms
            total = int(i) + int(number_of_days)  #original index number of the day in the list + number_of_days
            if number_of_days <= 7:
                if number_of_days == 7:
                    finding_index = int(i) #its the same i is the index of the input_day in the list  -- index of the list monday to tuesday - starting from 1 to 7 == to find our answer
                if number_of_days < 7:
                    if total > 7:
                        days_calculation= divmod(total , 7)
                        finding_index= days_calculation[1]
                        if finding_index == 0:
                            finding_index = 7
                            # days_calculation= divmod(total , 7)
                            # finding_index = days_calculation[1]

                    if total <= 7:
                        finding_index = total
                        # if finding_index == int[i] +1:
                        #  after_n_days = "(next day)"
                        # if finding_index > int[i] + 1
                        #  after_n_days = 
                    # if total == 7:
                    #     finding_index = total
            if number_of_days > 7:
                # if total > 7:
                days_calculation= divmod(total , 7)
                finding_index= days_calculation[1]
                if finding_index == 0:
                    finding_index = 7

               
                # if finding_index > 7:
                #     days_calculation= divmod(total , 7)
                #     finding_index = days_calculation[1] #now the remainder is the answer


    output_day=x[finding_index][1]  #possible_input_day -index starts with 0 -- so we are doing -1 as ours is as per 1

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
        if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
            am_pm = "AM"
            # hrs = int(x2[0])
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
        if (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- if the quotient is odd  here value is 1 Change am_pm and 11 styas the smae.
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
        if (t_hrs[0] % 2) == 1:  # its odd .. meaning 23/12   -- can not devide which means 12 and 11   +12 is Change am_pm and 11 styas the smae.
            am_pm = "AM"
            hrs = int(x2[0]) + int(t_hrs[1])
            if hrs > 12:
                hrs = hrs - 12
                am_pm = "PM"


    # if number_of_days >1 or number_of_days < 2:
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






    # print("=-=-=-=MIDDLE OUTPUT TO CHECK--=-=-=-=-=-=")
    # print(hrs)
    # print(f"{mm:02d}")
    # print(am_pm)
    # # print(n_days)
    # print(output_day)
    # print("=-=-=-=--=-=-=-=-=-=")






    # hrs = "09"    #
    # minutes = "40"  # will be a while number less than 60  By default user knows that
    # hrs_m = "09:40"
    # am_pm = "PM"



    #condition 1
    #if input_day mentioned then print the day ..
            #the same day if the time is on the same day
            #print next day if the output day is on the next day
            #print the respective day if the output day is not on the same or next day - Also print n days later with the day too 
    #condition 2
        #if input day is not metioned
            #then dont print any day if its on the same day.
            #then print next day if the output day is on the next day
            #then if its more than 1 day
                #then print only n days later
                
    if type(input_day) == None:
            if number_of_days > 1 and number_of_days < 2:
                n_days_later = "(next day)"
                # final_output = hrs + ":" + f"{mm:02d}" + " " + am_pm + " " + after_n_days / next day
            if number_of_days < 1:
                n_days_later = ""
                # final_output with nothing or no day just time and minuet
            if number_of_days >= 2:
                n_days_later = "(" + number_of_days + "later)"
                # final output with n days later
    if type(input_day) == str:
            if number_of_days > 1 and number_of_days < 2:
                final_output_day = output_day
                n_days_later = "(next day)"

            if number_of_days < 1:
                final_output_day = input_day
                n_days_later = ""
                # final_output  -- print with the same day that is in the input
            if number_of_days >= 2:
                final_output_day = output_day
                n_days_later = "(" + number_of_days + "later)"
                # final_output -- print with the respective day and also print n days later
            
    if type(input_day) == None:
        final_output= hrs + ":" + f"{mm:02d}" + " " + am_pm + " " + n_days_later
    if type(input_day) == str:
        final_output = str(hrs) + ":" + f"{mm:02d}" + am_pm + "," + " " + final_output_day + n_days_later
    
    return final_output

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