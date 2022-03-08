
from calendar import WEDNESDAY
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
                #print    09:40 PM

input_start_time = "10:10 PM"  #will be a valid time by default   
input_duration_hh_mm = "300:30"  #here the minute will be less than 60 whole number by default
input_day = "Monday"

possible_input_day = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']



x1= input_start_time.split()
print(x1)   #['09:40', 'PM']
x2=x1[0].split(":") 
# print(x2) #['09', '40']


y1=input_duration_hh_mm.split(":")
print(y1)  #['02', '19']

hrs= int(x2[0]) + int(y1[0])
mm = int(x2[1]) + int(y1[1])
am_pm = x1[1]

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

# print(hrs)
# print(mm)

print("--------------")

number_of_days =int(hrs/24) 

possible_input_day = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']




# print(number_of_days)
# sys.exit()

# sys.exit()
if hrs > 12 and hrs<24 and am_pm == "PM":
    hrs = hrs - 12
    am_pm = "AM"    #it changes at every 12 hrs addition -- SO its <24 .. did not consider the case of 24 - because that will be again PM too.
     #this indicates next day
elif hrs > 12 and hrs<24 and am_pm == "AM":
    hrs = hrs - 12
    am_pm = "PM"  #same logic as above
    #this indicates next day
# if more than 1 day
# hrs1 = 24
if hrs == 12 and am_pm == "AM":
    hrs = hrs
    am_pm = "PM"
    # n_days = "next day"

elif hrs ==12 and am_pm == "PM":
    hrs = hrs
    am_pm = "AM" 
    # n_days = "next day"
if hrs == 24 and am_pm =="AM":  
    hrs = int(x2[0])  #it stays the same .. after 24 hrs -- time will be same
    am_pm = "AM"   #after 24 hrs it will be AM only.
    
    # n_days = ???
elif hrs == 24 and am_pm =="PM":  
    hrs = int(x2[0])  #it stays the same .. after 24 hrs -- time will be same
    am_pm = "PM"   #after 24 hrs it will be AM only.
# print(hrs)

if hrs > 24 and am_pm == "AM":
    t_hrs=divmod(hrs, 12)  #built-in function we can use to find qaotient and remainder
    if (t_hrs[0] % 2) == 0:  #it means its its Even for example the quotient is even ..that means after 24 hrs its going to be same am_pm
        am_pm = "AM"
        hrs = int(x2[0]) 
        hrs =  int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
    if (t_hrs[0] % 2) == 1:  #its odd .. meaning 23/12   -- if the quotient is odd  here value is 1 Change am_pm and 11 styas the smae.
        am_pm = "PM"
        hrs =  int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
    # print(hrs)
# sys.exit()            
elif hrs > 24 and am_pm == "PM":
    t_hrs=divmod(hrs, 12)
    if (t_hrs[0] % 2) == 0:  #it means its its Even for example 24/12 is even that means after 24 hrs its going to be same am_pm
        am_pm = "PM"
        hrs =  int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
            am_pm = "AM" 
    if (t_hrs[0] % 2) == 1:  #its odd .. meaning 23/12   -- can not devide which means 12 and 11   +12 is Change am_pm and 11 styas the smae.
        am_pm = "AM"
        hrs =  int(x2[0]) + int(t_hrs[1])
        if hrs > 12:
            hrs = hrs - 12
            am_pm = "PM" 




# print(number_of_days)


if number_of_days >1 and number_of_days<2:
    n_days = "next day"
elif number_of_days >2:
    n = number_of_days
    n_days = str(n) + " " + "days later"
    # print(n_days)


print(hrs)
print(f"{mm:02d}")
print(am_pm)
print(n_days)


# hrs = "09"    #
# minutes = "40"  # will be a while number less than 60  By default user knows that
# hrs_m = "09:40"
# am_pm = "PM"

# output = hrs+ ":" + minutes + " " + am_pm
# print(output)