# import sys
# from numpy import empty


# class Category:

#     def __init__(self, ledger):
#         self.ledger = [ ]

#     def deposit(self,amount, description=empty): #instance method and its parameters   -- default value of description is empty
#         pass
        
        
        
#         pass   #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
#     def withdraw(self,amount, description): #instance method
#         pass   # the amount passed in should be stored in the ledger as a negative number
#                 #If there are not enough funds, nothing should be added to the ledger. 
#                 #This method should return True if the withdrawal took place, and False otherwise.
#     def get_balance(self):
#         pass    #A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
#     def transfer(self):
#         pass #A transfer method that accepts an amount and another budget category as arguments.
#              #The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
#              #The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
#              #If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
#     def check_funds(self):
#         pass #A check_funds method that accepts an amount as an argument.
#              #It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
#              #This method should be used by both the withdraw method and transfer method.


# # When the budget object is printed it should display:
#     #A title line of 30 characters where the name of the category is centered in a line of * characters.
#     #A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. 
#         #The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
#     #A line displaying the category total.

# #Here is an example of the output:
# # *************Food*************
# # initial deposit        1000.00
# # groceries               -10.15
# # restaurant and more foo -15.89
# # Transfer to Clothing    -50.00
# # Total: 923.96


# # Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
# # It should return a string that is a bar chart.



# budget = Category()






# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)