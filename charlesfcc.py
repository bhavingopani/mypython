from math import floor
# from tkinter.messagebox import NO

from pyparsing import WordStart

#ELEVETOR FLOOR CONVERSION APP

#You are in Eourope and lost -- and You want to know what floor i will be if i were in US??

# Europe floor ? 0- Ground floor
# US floor ? 1    - Ground floor


# eu_floor = int(input('Enter Eroupe Floor? '))
# usa_floor = eu_floor + 1

# print(usa_floor)


#
# word = "bananana"
# i = word.find("na")
# print(i)

#dictionaries

# purse = dict()
# purse['money'] =12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)

# family_names= dict()
# family_names['Bhavin'] = 1
# family_names['Sandip'] = 1
# family_names['Hitesh'] = 1
#
# print(family_names)
# family_names['Bhavin'] = family_names['Bhavin'] + 1  #if Bhavin already exist then add one to it
# print(family_names)

#another example
# counts = dict() #currently its empty
# names = ['bhavin', 'sandip', 'hitesh','sandip','bhavin','hitesh','bhavin','bhavin']
#we can use in operater to check if its there .. but here we will have to use the for loop for counting
# for name in names:
#     if name not in counts:
#         counts[name] = 1 #if name not in there in dict or counts we add 1 to it
#     else:
#         counts[name] = counts[name] + 1 #otherwise add 1 to it and get back to it.
# print(counts)

#in the above example  the entire if condition can be replaced with get method
        # if name in counts:
        #     x = counts[name]  #if name in dictionary then fine you will get back the key that is there otherwise you get the default value.
        # else:        #otherwise x or counts[name] is 0
        #     x = 0            #here 0 is the default value - if nothing there

# for name in names:
#     counts[name] = counts.get(name,0) + 1 #here 0 is the default value  --  the above 4 lines are equal to this line and we are adding 1 to it.
#                     #this means if name's value is 1 then it will add 1 and if its not there that means the value is 0(default) and we can add 1 to it.
#                     #so if new word then it will be 1 and if already there then existing value of the key + 1 will be the output
# print(counts)

#Counting words in the file

# counts = dict()
# line = input()

# words = line.split()

# print('Words:', words)

# print('counting')
# for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# name = input('Enter file:') #asking for the file name
# handle = open(name)      #opening the file

# counts = dict() #making an empty dictionary
# for line in handle:      #iteration variable that will go throgh the lines in the file
#         words = line.split()    #it will slipt all the lines into words
#         for word in words:      #going throgh each word
#             counts[word] = counts.get(word, 0) + 1   # this will run for each line and every word and here the outer loop is going by line and inner loop is going by word if the word is there it will add 1 and if not there than this will add 1 to its default value which is 0 
        
# #now we want to find the largest one - largest value in key:value pair in the dictionery

# bigcount= None
# bigword = None
# for word,count in counts.items():
#         if bigcount is None or count > bigcount:
#                 bigword = word
#                 bigcount = count
# print(bigword, bigcount)

#Tuples (immutable) not changeble
 #Tuples can not be altered. But Lists can
 #once tuples are made its not modifieble
        #quicker to access
        #more efficiet than list
        #only count and index method works with tuple.. but lists has a lot of methods you can use
        #high performance and efficient memory use

        

#sorting list of tuples
#the below is sorting items by keys
d = {'a':10, 'c':1, 'b':22}
print(d.items())
print(sorted(d.items()))

#new example
t = {'a':11, 'd':1, 'b':22}
t = sorted(t.items())
print(t)

for k, v in t:
        print(k,v)

#the below is sorting items by values instead of keys
#here we have create a data structure where we have values first and keys second

c = {'a':12, 'g':98, 's':78, 'f':1, 'c':6}

print(c.items()) #this will give list of tuples where there is key first and then value

#now to make the value first and key later datastructure 

tmp = list() #creating empty list first
#the below loop is for appending 
for k, v in c.items():    #here k,v goes into list of items as k and v
        tmp.append((v,k)) #here we append them in value first and key second.
        
print(tmp) #now we have a temporary data structure that we have constructed to make our job really easy.

tmp = sorted(tmp) #by default sorted sort it by ascending order - small value first
print(tmp) 
tmp = sorted(tmp, reverse=True) #to sort this by descending order - large value first - reverse should be true by default its false 
print(tmp)

#Top 10 most common words 

opening_file = open('words.txt')  #opening file
counts = dict()     #creating empty dictionery
for line in opening_file:  #looping line by line in the file
        words = line.split()  #spliting each word and saving it to words in list
        for word in words: #looping throgh list of words with word iteration variable
                counts[word]  = counts.get(word, 0) + 1  #idiom we are using #checking if the word is already till the current list of words in the dictinay IF NOT it will store the word with default value 0 and then add 1 to it and store the value in the word
#now we have lists of values - we can work on that as below and sort it
lst = list() #creating empty list
for key , val in counts.items(): #looping throgh list of tuples that is created by .items()
        newtup = (val, key) #we are flipping the order of the above key and val thing
        lst.append(newtup) #appending the tuple to the list.. - earlier we directly wrote (val, key) - that can also be done.. but to understand this one is better
        
lst = sorted(lst, reverse=True)  #sorting the listt of tuples as descending order - so high value first -- as we want top 10 so - it starts with 0 which is the 1st record

for val, key in lst[:10]:  #loop till it reaches to 10th tuple - 10th one is NOT INCLUDED
        print(key,val) #printing the top 10 now and printing it as Key Value as that is the ideal way - Val , Key done to fine the top 10 


#REGULAR EXPRESSIONs
import re

x = 'Aantava: 23 aa antava 24: oo antava 10 aa natava 4'
y = re.findall('[0-9]+', x) #[0-9]+ says 0 to 9 digits and + is for one or more
print(y)

z = re.findall('^A.+:',x)  #here its saying   ^(Starts) A(with A) + one or more and : ends with column - if it has two ends -- it will print the larger one - TO STOP THIS YOU CAN USE ? so that it will not print the longer one
print(z)

#  \S at least one nowhite space character -- means non-blank characters
#  * means many times
#  . match any character
#  () - whatever written in this  will come out and will be extracted -- Without this you get the entire condition output extracted- with () you match the entire condition BUT the extraction output will be of () condition only
 









        


        





 































