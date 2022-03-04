
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
#     sum += item    #augmented assignment operator - assume if we need to add 7 to a variable “a” and assign the result back to “a”, so we can use it
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

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

#
# message = input("> ")
# words  = message.split(' ')  #slipt method will separate where there is this character - here its space. and will also create a list for the same
# emojis = {
#     ":)":"😃",
#     ":(":"😔",
#     "<3":"😍"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)



#Functions

# def greet_user():   # to define a function - gree is the name of function #   () this will consist parameters tat are - we can always pass parameters - can be more than one
#     print('Hi there!')      #anything we write will be for the above function
#     print('Welcome aboard')
#                     #we need 2 lines break just after the function #rule of python
# print("start")
# greet_user() #can assign value to the parameter -- this is called an argument
# print("finish")

#we can directly define parameter as keyword = argument  as below
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#
# greet_user(last_name="mahesh", first_name="gandhi") #here the order of parameters can be different when we define keyword argument
#                                                     #you can always do it without keyword but it makes code redeable
# calc_cost(50,5,0.1) #here the first para is Total price , second is shipping cost and third is 0.1 discount
#             #someone reading this will not be able to understand -- here we can use keyword to make this redable
#calc_cost(total_cost = 50, shiping_cost = 5, discount = 0.1) #this is redeable
#keyword argument always comes after positional arguments

# def square(number):
#     #number * number #this does not return a value - it will be none if you check and print
#     #print(number * number)   - when call this later on this will return the value and none as well and we are printing the value or resutlt and function also does the same.
#     return number * number # return will return a value of a function and we can use it as below
#           by default every function returns value none - that means absence of a value
# result = square(3)
# print(result)











# message = input("> ")
# words  = message.split(' ')  #slipt method will separate where there is this character - here its space. and will also create a list for the same
# emojis = {
#     ":)":"😃",
#     ":(":"😔",
#     "<3":"😍"
# }
# output = ""
# for word in words:
#     output = output + emojis.get(word, word) + " "
# print(output)

#always put all things in a reusable function ... all things which are usable again - should put that only
#
# def emojis_function(message):
#     words_new = message.split(' ')
#     emojis = {
#         ":)": "😃",
#         ":(": "😔",
#         "<3": "😍"
#     }
#     result = ""
#     for word in words_new:
#         result = result + emojis.get(word, word) + " "
#     return result
#
# print(emojis_function("Hi I am bhavin :)"))
#

# age = int(input("What is your age? > "))
# print(age)
#exit code 0 in the terminal means - our program terminated successfully
#exit code 1 or anything - means program crashed
#to check the code here - you can enter values like --  asd and other things - sdfljnflsn
# when its error better to print error
#in python we have contruct called try except
# try:  ## try except contruct is used to handle exceptions in the language
#     age = int(input("What is your age? > "))
#     print(age)
# except ValueError:      #now python will not crash when its valueerror
#     print('Invalid Value')
# except ZeroDivisionError:  #when something is divided by zero this will be a typeerror
#     print('Age cannot be 0')

#Class and Objects

# class Point:             # can define methods and cod under this class
#     def move(self):  # pycharm automatically add/generates special keyword self there in the bracket
#         print("move")
#     def draw(self):    # another methon under class
#         print("draw")
#
# #now defining an object -- its an instance of a class #and a class is a blueprint of template of a class and objects are the instances based on a blueprint
# #so here we can have hundrends of points - or objects or instances
# #to create an object do the belwo
#
# point1 = Point()  #this creates a new object and returns it and we can store it in a variable
# point1.draw()   #now we can use the dot operator and we find our defined method - move and draw
# #this object can also have attributes - They are variables that belong to a particular object - for example
# point1.x = 10 #here x is an attribute of point1 object
# point1.y = 20 #here y is an attribute
# print(point1.y)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)
#in short we use classes to define new types and These types can have methods that we define in the body of the class - and they also have attributes that we can set anywhere in program


#in the above way... there will be an AttributeError.....and we will have to define x point1.x = 5 value -- to solve this problem
#constructors  --  here its possible to have point object without x or y coordinates as constructors - we need to know where that point is located - to solve this problem we use constructor
        #constructor is a function that gets called at the time of creating an object - pass x and y coordinates
# point3 = Point(10, 20) #to use this we need to add a special method called constructors -- with __init__  (here its init for short of initialization
# # point3()
#
# class Point:
#     def __init__(self, x , y):  #adding extra parameters x, y   # self is here.. is the reference to the current object
#           self.x = x              #initializing
#           self.y = y
#
# point = Point(10, 20)
# print(point.x)
# point.x = 12            #can also update value
# print(point.x)
# print(point.y)
#exercise
     #person object should have name attribute so using constructors
# class Person:
#     def __init__(self, name): #defining name attribute - we call it constructo
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# # john  = Person()
# # john.talk()
#
# rajesh = Person("Rajesh Solanki")
# rajesh.talk()
#
# mahesh = Person("Mahesh Solanki")
# mahesh.talk()

#INHERITANCE
#the below is the repeatation of code
# class Dog:
#     def walk(self):
#         print("walk")
#
# class Cat:
#     def walk(self):
#         print("walk")

#with inheritance you can write above code as below

# class Mammal:   #instead of the above way what we did was that... we created Mammal class and we inherita other class in dog and cat class
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal): #this means all the mehtods that Mammal class has inherited to Dog and the same is true for Dog
#     # pass           # PYTHON does not accept an empty class So if you have nothing to write you can always use pass - so that it will skip the same.
#     def bark(self):
#         print("Bark")
#
# class Cat(Mammal):
#     # pass
#     def cute(self):
#         print("cuty")
#
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.cute()

#modules   #its like refering to each file as a module
        #for example below code is there but we can take the below code and put them in a module called converter
#the below code we put it in different code
# def lbs_to_kg(weight):
#     return weight * 0.45
#
# def kg_to_lbs(weight):
#     return weight / 0.45

#the above code can be put in a module called converter and we can import that module in any programe that needs converter

# import converters  #write this without the extension .py and this is an object now
# from converters import lbs_to_kg            #if you want to import a specific method from the module that can also be done instead of importing entire module
# print(lbs_to_kg(100))                #can use this as defined in the above function
# print(converters.kg_to_lbs(20))

#ALWAYS USE MODULE TO BETTER ORGANIZE OUR CODE.. instead of writing all the code in one module or file

#exercise
#
# numbers = [10, 3, 6, 2]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#taken the below code into converter module or file will use it here - this was an example
# def find_max(numbers):
#     max = numbers[0]
#     for number in numbers:
#         if number > max:
#             max = number
#     print(max)

# import utils  #way of importing - importing entire file or module
# from utils import find_max #another way of importing - to import just a method
# x = [100,299,398]
# find_max(x)
# utils.find_max(x)

# PACKAGES    -- ANOTHER WAY TO ORGANIZE OUR CODE
#Real projects contain thousand or hundreds of modules  - NO need to add all those modules here in the LEFT BAR
# because then this directory will be bloated with multiple files
#just keep only related files only

#best approach is to keep related modules in Packages -- package is a container for multiple modules
#In file system terms a package is a directory or folder
#so in a project we can add new directory and in that we add all the related modules
#all packages or directory has   __init__.py file --- python treat that as package - a directory can not be empty

#ecommerce is a package that we have created
#to use that
# import ecommerce.shipping  #one way
# from ecommerce import shipping #to import one module from a package -
# from ecommerce.shipping import calc_shipping  #another way to import specific
# calc_shipping()
# ecommerce.shipping.calc_shipping()
# shipping.calc_shipping()

#GENERATING RAMDOM VALUES

#using built-in python modules -

import random  #its built-in module so we dont need file in the directory

# for i in range(4):
#     print(random.random()) #can use random as object and can use dot operater to access it   #random method generates random value between 0 to 1
# #print between numbers - check other method
# for x in range(3):
#     print(random.randint(10, 20))
#can also print random from list
# members = ['bhavin', 'sukhi', 'rajesh']
# random.choice(members)    #choice is a method that we can use from the built in random module - like other methods
# print(random.choice(members))

#EXERCISE OF RANDOM  -- Rolling two dice and every time different values
#THE BELOW DONE BE ME was a wrong method
# dice1 = [1, 2, 3, 4, 5, 6]
# dice2 = [1, 2, 3, 4, 5, 6]
# print((random.choice(dice1),random.choice(dice2)))
#THE ABOVE DONE BE ME was a wrong method

# class Dice:
#     def roll(self):
#         dice1 = [1, 2, 3, 4, 5, 6]  #my way -- but we can use   first number = random.randiant(1,6)
#         dice2 = [1, 2, 3, 4, 5, 6]  #my way -- but we can use   first number = random.randiant(1,6)
#         print((random.choice(dice1),random.choice(dice2)))  #we can use return here instead of print -- and will use print when we call the object below
#
# dice = Dice()
# dice.roll()
#

#WORKING WITH DIRECTORIES
# from pathlib import Path   #There are two type of paths when working with directories

#Absolute Path  #we start from the root of our harddisk
    # c:\Program Files\Microsoft   - for windows
    # /usr/local/bin               - for linux
#Relative Path  #path from your current directory
    #can use this
#Path()  #if we keep it empty , this will refenrence current directory autometically
# path = Path ()  # we can add file or directory  as string - this returns a path object that we stored in path
# print(path.exists())   #we can check to see if the path exists by calling the exists method - this will return Boolean
# path.mkdir()      #we can use mkdir method to create a directory if it does not exist - write down name of the folder or directory in the place of ecommerce
# path.rmdir()      #the same way we can remove a direcroty
# print(path.glob('*.py'))   #'' this will define a search patter  '*' - this means all files and folder  and   '*.*' - to get all the files in the current directory and '*.py' or any extension -search for all the py files
    #this will return or print generator object
    #SO WE HAVE TO LOOP THROGH IT
# for file in path.glob('*.py'):   #to print files from the object or instead of printing generator object
#     print(file)

#pypi.org   -- packages - you can find any packages here

#openpyxl  - name of the package in pypi for working with el

#check spreadsheet project in another branch







































































































