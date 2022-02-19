  
#WIRE PROTOCOL

#HOW DATA is sent and the format that is understandable by all languages and can talk to any aplication - JSON and XML
#Sending data accross internet - JSON and XML --- independent of any languages
#SO first Serializing data  happens and Then Deserializing the same data happens by other application
#MARK UP language is used or ways to send data between computers especially on Internet and kind of protocol which every applicaion follows to understand the communication and data that is coming from other application
#XML 

#XML Schema - a language that allows you to decide whether a particular XML document meets a particular contract or an arrangement
    #description a legal format
    #used to specify a contract between system its like "My system will only accept XML that confirms to this particular schema"
    #If a particular piece of XML meets the specification of the Schema - It is said to "validate"
    #XML Schema Contract
        #it is XML only but kind of complex XML written - a particular fomat that validates a XML doc
#XML Document and XML Schema Contract ---- THere is a XML validation - we say if this is validated or not 

#There are many XML Schema Languages were out there like DTD , SGML, XSD Schema from W3C
#XSD more 
#XML in python

# import xml.etree.ElementTree as ET  #this is a library  ET we created a shortcut so we dont have to type in long
# data = '''<person>   
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''  #''' triple quoted is as there are lines \n at each one so its like opening a file and read it.. Otherwise this data usually comes from file or network - just to understand we have taken it as string in '''

# tree = ET.fromstring(data) #passing all the data here - this can have syntex error too.. and it might blow up if it had a syntex error like forgeting little slash or somthing
#                 #we are getting this back as an object tree ... Its an object we can then pull query to pull data out of it
# print('Name:',tree.find('name').text) #here tree.find('name') gives us both Tag and text... but we wanted text only so we can use .text
# print('Attr:',tree.find('email').get('hide'))  #here the same as above it will get email tag.. but to filter we can ask it via get and enter the attribute which is hide

#XML is best for Rich info or rich document Whereas JASON good for just pulling data out of two systems.

#JASON (Javascript Object Notation)
#this is not an internation standard - it was discovered from js and people started using it widely and hence became kind of standard for getting data between two application and sytems.
#JOSON represents data as nested "lists" and "dictionaries"

import json #library
data = '''{
    "name" : "Chuck",
    "phone":{
        "type":"intl",
        "number":"+1 734 303 4456"
    },
    "email": {
        "hide" : "yes"
    }
}'''
#in python all are dictionaries or lists or dictionaries within lists
info = json.loads(data)   #info is a dictionary
print('Name:',info["name"])   #so we can use python way to find values - info sub name
print('Hide:',info["email"]["hide"]) #the same way info sub email sub hide

#another type of json where the outer brackat is a square bracker - that is called list - below example
input = '''[
    { 
        "id" : "001",
        "x"  : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x"  : "7",
        "name" : "Chuck"        
    }
]'''  #also called list of dictionaries

info_new = json.loads(input)
print('User Count:', len(info_new))  #this will give how many object or info or items
for item in info_new: #it will loop throgh each object means items .
    print('Name', item['name'])
    print('id', item['id'])
    print('Attribute', item['x'])
    



