
# patient_name = 'John Smith'
# patient_age = 20
# patient_is_new = True
#
# # ()  this means we are calling that function or executing that function
#
# name = input('What is your name? ')    #calling the input function and store it in a variable -- the input from the user
# print ('Hi ' + name)
#
# favourite_color = input('What is your favourite color? ')
#
# print (name  + ' likes ' + favourite_color + ' color')
#
# birth_year = input('What is your birth year? ')
# print(type(birth_year))
# age = 2021 - int(birth_year)   #making the birth_year integer
# print(type(age))
# print(age)

# weight_in_pounds  = input('How much pound you weigh? ')
#
# x_interger = int(weight_in_pounds)
#
#
# weight_in_kilograms = x_interger * 2.2
#
#
# print('Your weight is ' + str(int(weight_in_kilograms)) + ' kilograms' )
#
# #the triple quotes used for multiple lines of string.,
# course= '''
# Hello there,
#
# this is our email about leaving the comapny
#
# Thank you
#
# '''
# print(course)
#
# new = 'Python for Beginners'
# print(len(new))


# price_of_house = 1000000
#
#
# buyer_has_good_credit = False
#
# if buyer_has_good_credit:
#     print('He will pay ' + str(int(price_of_house * 10/100)) + ' as down payment')
# else:
#     # print( 'He will pay ' + str(int(price_of_house * 20/100)) + ' as down payment')
#     # you can also write this as
#     down_payment = 0.2 * price_of_house
#     print(f"Down Payment: ${down_payment} ")


# entered_weight = int(input("Weight: "))
#
# print(type(entered_weight))
# l_or_k = input('L(lbs) OR K(kilos): ')
# if l_or_k.upper() == 'L': #.upper will convert any input from user to capital/uppercase
#     converted_weight = entered_weight * 0.45
#     print(f"You are {converted_weight} kilos")
# else:
#     converted_weight_again =  entered_weight//0.45  #if we use single / it will return floating point number or will return // regular number interger
#     print(f"You are {converted_weight_again} lbs")

#While Loop
#
# while condition: #as long as this condition is true.. the code that is written below will keep repeating
#     code here

# i = 1
# while i<= 5:
#     print('*' * i)
#     i = i + 1 #have increment otherwise i will be 1 infinitely. - the above condition will always be true.
# print("Done")
#
# print("Guess a Number: YOU ONLY HAVE 3 CHANCES TO Guess the Right Number")
#
# secret_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == 9:
#         print("You Win!")
#         break #to terminate the loop
# else:
#     print("Sorry You failed!")

#Building a Car Game
   #> this symbol there then enter command
   #help command
        # start  - to start the car
        #     - print Car Started ... Ready to go
        # stop   - to stop the car
        #     - Car stopped
        # quit   - to exit
        #     - Program Terminated
        # if User writes any other command   - just print i dont understand that


#
# new_command = input("> ")
# car_started = False # we are initially make it False as the car not started yet.
# while True: #new_command == "start" or "stop" or "quit" or "help":  # Can also write ---  while True: /which means it block of code will get excuted repeatedly untill that does not exit.
#     if new_command == "help":
#         print(f" start - To start the car\n stop - To stop the car \n quit - To exit")  #can also use multiline """start - to s...  """
#         new_command = input("> ")
#     elif new_command == "start":
#         if car_started:     #this automatically means car_started = True
#             print("Car is already started!")
#         else:
#             car_started = True
#             print("Car Started... Ready to go!")
#         new_command = input("> ")
#     elif new_command == "stop":
#         if car_started:
#             car_started = False
#             print("Car Stopped")
#         else:
#             car_started:False
#             print("Car is already stopped")
#         new_command = input("> ")
#     elif new_command == "quit":
#         exit()  ## can write break
#     else:
#         print("I don't understand that")
#         new_command = input("> ")

#FOR LOOPS  -- in while loop we iterate over bloc of code --
# BUT IN FOR LOOP - we iterate over items of collections
# such as a string - its a sequence of characters - we use for loops to iterate over each character
#example

#for loop_varible    # In each iteration this variable will hold one item
    # code          Whatever we type here will be executed in each iteration
# for item in 'Python': # here we call loop_varible is item and we iterate over Python string.
#       print(item)                   #in each iteration item will hold one character at a time - like in first its P then in second iteration its y and so on
#
# #instead of strings it could be list as well
# for item in ['rajesh', 'pragnesh', 'mohit']:
#     print(item)
# for item in [1,2,3,4,5,6,7]: #can iterate over list of numbers
#     print(item)
# #what if we want to iterate over large list of numbers for example if we have 100 numbers we can write that .. we can use python range functions
# for item in range(95):   #here the range function creates an object - at each iteration this will object will spit out new number
#     print(item)
# for item in range(5,10): #5 to 10 - 10 excluded
#     print(item)
# for item in range(5,10,2): # 2 incremeted and printed like 5 7 9
#     print(item)

#Exercise - total costs of all the items in the shopping cart
# item1 = 10
# item2 = 20
# item3 = 30
#
# prices = [item1,item2,item3]
# sum = 0
# for item in prices:
#     sum = sum + item # here we can use augmented assignment operators to simplify the code  --
# #    sum += item    #augmented assignment operator - assume if we need to add 7 to a variable “a” and assign the result back to “a”, so we can use it
# print(sum)
#

#nested loop - adding one loop inside of another loop
#with this technique we can do some amazing things
#for example we can easily generate list of coordinates
# (x,y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# (2,0)
# (2,1)
# (2,2)
 #we can generate this coordinates using nested loop
#first do with x
# for x in range(4):  #outer loop
#     for y in range(4):  #called inner loop
#         print(f'({x},{y})')
# 5
# 2
# 5
# 2
# # 2
#
# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     output = '' # this is empty as we have to reset the value of output everytime the loop goes on
#     for count in range(x_count):
#         output = output + 'x'
#     print(output)

#List
# names = ['johs', 'bob', 'Mosh', 'soha', 'sharah' ]
# print(names[1:4])

#find the largest number in the list
#
# numbers = [10, 122, 523, 485, 589,875, 562, 564, 598]
# max= numbers[0]
# for number in numbers:
#     if number > max:
#         max = number  #resetting it to max
# print(max)

# matrix = [
#     [1,2,3],
#     [5,6,7],
#     [8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
#
#Remove duplicates on the List

# names = ['bhavin', 'bhavin', 'rajesh', 'vidya', 'vidya', 'imagica']
# uniques = []
# for name in names:
#     if name not in uniques:
#         uniques.append(name)
# print(uniques)

#TUPLE  -- similar to list but its with () and we can add new items in it - its immutable
# numbers = (1,2,3)
# numbers.
#tuple can be used .... like if you want to create list that can not be modified or changed then use tuple.
#for example coordinates (x, y, z)
# coordinates = (1,2,3)
# # coordinates[0] * coordinates[1] * coordinates[2] #we can do this ---but its longer so better to check the below all. the unpacking method in python
# x, y, z = coordinates  # unpacking  concept  # we can use this concept with list as well
# print(y)
#dictionaries
# customer = {}  #defining dictionaries - its Empty
# customer = {
#     "name":"John Smith", #key and value pair its called
#     "age":30,
#     # "age":40, Duplication of key:value pair is not allowed - key should be unique
#     "is_varified":True
# }
#
# #accessing the above keyvalue pair
# print(customer["name"]) #its a case sensitive - so it has to be same
# #print(customer["birthdate"]) #this key does not exist so will be a key error
# print(customer.get("birthdate"))  #this will not generate key error - it will through none - its an object
# print(customer.get("birthdate", "Jan 10 1980")) #this way we can add a key and the default value of that key.
# customer["name"] = "Rajesh Solanki" #to update value
# print( customer["name"])
# customer["fathername"] = "jitujitu"  #the same way we can add new key and value of the same - adding to disctionary
# print(customer["fathername"])
#exercise
#to do - it will ask for phone number







































































