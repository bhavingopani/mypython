# # from unicodedata import name


# class Robot:
#     #creating constructor
#     #the below is the constructor and name, color , weight is the parameters to the constructor in the bracket
#     def __init__(self, name , color, weight): #custom constructer -- after this we do not have to specify attribute name every time we create an object
#         self.name = name   #this is instance variable
#         self.color = color   #these are instace variable
#         self.weight = weight  #instance variable
    
#     def introduce_self(self):  #Instance method
#         print ("My name is " + self.name)
    

# #creating first object
# #the blow can be removed and we can use contructor
# # r1 = Robot()   
# # #the below three are attributes of this object r1
# # r1.name = "Tom"
# # r1.color = "red"
# # r1.weight = 30

# # r2 = Robot()
# # #the below three are attributes of this object r2
# # r2.name = "Jerry"
# # r2.color = "blue"
# # r2.weight = 40
# #r1 and r2 below are the two objects of the class
# r1 = Robot("Tom", "red", 30 ) #this will do the same as above but we have created a custom constructer in the class so..
# r2 = Robot("Jerry", "blue", 40 )


# r1.introduce_self()
# r2.introduce_self()

# # Robot.introduce_self()

# #accessing instance variable


from ctypes import resize
import sys





#Input Example












#Category: food , clothing, and entertainmet

category1 = "food"
category2 = "clothing"
category3 = "entertainment"

initial_deposit_food = input("Pls enter initial current deposit amount that you have for food: ")
inital_deposit_description_food = input("pls enter description of initial deposit food: ")



asking_if_wants_to_enter_expenses_in_food_category = input("Do you want to add expenses in food category? Yes/No? ")
result = []
while asking_if_wants_to_enter_expenses_in_food_category == "Yes":
    add_expense_for_food = input("Pls enter amount of the expense for food category food: ")
    add_expense_description_for_food = input("Pls enter description of the same for food ")
    asking_if_wants_to_enter_expenses_in_food_category = input("Do you want to add more expenses in food category? Yes/No? ")
    result.append(add_expense_description_for_food)
    result.append(add_expense_for_food)
    
print(result)
# print(result[0])
# print(result[1])
result2 = []
print(inital_deposit_description_food, initial_deposit_food)
for i, element in enumerate(result):
# print(add_expense_description_for_food, add_expense_for_food)
    result2.append (element, i)
print(result2)


    #deposit
       #amount 
       #description   
          #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    #withdraw
        #amount
        #description
            # the amount passed in should be stored in the ledger as a negative number
            #If there are not enough funds, nothing should be added to the ledger. 
            #This method should return True if the withdrawal took place, and False otherwise.
    #get_balance
        #A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    #transfer
        #A transfer method that accepts an amount and another budget category as arguments.
        #The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        #The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
        #If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    #check_funds
        #A check_funds method that accepts an amount as an argument.
        #It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        #This method should be used by both the withdraw method and transfer method.
    
    
# Output Example
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
    
    
    
    #create_spend_chart
        #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
        #It should return a string that is a bar chart
        #The chart should show the percentage spent in each category passed in to the function. 
        #The percentage spent should be calculated only with withdrawals and not with deposits.
        #Down the left side of the chart should be labels 0 - 100. 
        #The "bars" in the bar chart should be made out of the "o" character. 
        #The height of each bar should be rounded down to the nearest 10. 
        #The horizontal line below the bars should go two spaces past the final bar. 
        #Each category name should be written vertically below the bar.
        #There should be a title at the top that says "Percentage spent by category".
        #This function will be tested with up to four categories.


#OUTPUT EXAMPLE OF CHART
#Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o  o     
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g     
