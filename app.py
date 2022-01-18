
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



new_command = input("> ")
car_started = False # we are initially make it False as the car not started yet.
while True: #new_command == "start" or "stop" or "quit" or "help":  # Can also write ---  while True: /which means it block of code will get excuted repeatedly untill that does not exit.
    if new_command == "help":
        print(f" start - To start the car\n stop - To stop the car \n quit - To exit")  #can also use multiline """start - to s...  """
        new_command = input("> ")
    elif new_command == "start":
        if car_started:     #this automatically means car_started = True
            print("Car is already started!")
        else:
            car_started = True
            print("Car Started... Ready to go!")
        new_command = input("> ")
    elif new_command == "stop":
        if car_started:
            car_started = False
            print("Car Stopped")
        else:
            car_started:False
            print("Car is already stopped")
        new_command = input("> ")
    elif new_command == "quit":
        exit()  ## can write break
    else:
        print("I don't understand that")
        new_command = input("> ")












