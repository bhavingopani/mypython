
possible_input_day = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
x=list(enumerate(possible_input_day,1)) #now index will start from 1 instead of 0
input_day = "THURSDAY"
hrs = 26
days_hrs_calculation = divmod(hrs, 24)
# print(days_hrs_calculation[0])   #top item when doing devision
# print(days_hrs_calculation[1])  #remainder -- shows how many hrs left after counting days by 24 hrs
number_of_days = days_hrs_calculation[0]
number_of_hrs = days_hrs_calculation[1]
# print(number_of_days)
# print(number_of_hrs)



print(number_of_days)
for i, element in x:
    # if input_day == i[1]:
    if element == input_day:
        total = int(i[0]) + int(number_of_days)
        # print(total)
        print("yes")
    
    # print(int(i[0]))
    #