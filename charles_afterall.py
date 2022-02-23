#Service Oriented Approach
 #checked that video


#WEB SERVICES API (Application Program Interface)
# API - Its a contract that says if you do this.. we are going to give you data this and this way
    #they tell you the rules, they tell you what the URLs are , THey also tell us its XML or Json, 
    #that's why its called Application Program Interface
    #its something you read and you understand

#Example of Google map APIs - Geocoding API
    # https://developers.google.com/maps/documentation/geocoding/start
    
    #Geocoding request and response (latitude/longitude lookup)
        # The following example requests the latitude and longitude of "1600 Amphitheatre Parkway, Mountain View, CA", and specifies that the output must be in JSON format.
       # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
       # after json? this are rules and it can also be encoded url - enter your API key in the back  + means SPACE and %2C means comma
       #IF YOU TYPE THIS URL IN BROWSER YOU WILL GET BACK THE JSON DOC AND RESPONSE or an object that has Key Value Pair
# ''' {
#    "results" : [
#       {
#          "address_components" : [
#             {
#                "long_name" : "1600",
#                "short_name" : "1600",
#                "types" : [ "street_number" ]
#             },
#             {
#                "long_name" : "Amphitheatre Parkway",
#                "short_name" : "Amphitheatre Pkwy",
#                "types" : [ "route" ]
#             },
#             {
#                "long_name" : "Mountain View",
#                "short_name" : "Mountain View",
#                "types" : [ "locality", "political" ]
#             },
#             {
#                "long_name" : "Santa Clara County",
#                "short_name" : "Santa Clara County",
#                "types" : [ "administrative_area_level_2", "political" ]
#             },
#             {
#                "long_name" : "California",
#                "short_name" : "CA",
#                "types" : [ "administrative_area_level_1", "political" ]
#             },
#             {
#                "long_name" : "United States",
#                "short_name" : "US",
#                "types" : [ "country", "political" ]
#             },
#             {
#                "long_name" : "94043",
#                "short_name" : "94043",
#                "types" : [ "postal_code" ]
#             }
#          ],
#          "formatted_address" : "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
#          "geometry" : {
#             "location" : {
#                "lat" : 37.4267861,
#                "lng" : -122.0806032
#             },
#             "location_type" : "ROOFTOP",
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 37.4281350802915,
#                   "lng" : -122.0792542197085
#                },
#                "southwest" : {
#                   "lat" : 37.4254371197085,
#                   "lng" : -122.0819521802915
#                }
#             }
#          },
#          "place_id" : "ChIJtYuu0V25j4ARwu5e4wwRYgE",
#          "plus_code" : {
#             "compound_code" : "CWC8+R3 Mountain View, California, United States",
#             "global_code" : "849VCWC8+R3"
#          },
#          "types" : [ "street_address" ]
#       }
#    ],
#    "status" : "OK"
# } '''

#THE ABOVE IS THE RESPONSE FROM GOOGLE APIs and WE CAN ALWAYS WRITE A PROGRAM THAT CAN READ THIS


#https://www.py4e.com/code3/




# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1:
#        break
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)

#API rate limiting - means -- Number of time you can use - or USAGE LIMIT

#Oauth (Can check later on)


# import urllib.request, urllib.parse, urllib.error
# import json
# import requests

# url_firstpart = 'https://maps.googleapis.com/maps/api/geocode/json?'  # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY


# while True:
#    address = input('Enter Location: ')
#    if len(address) < 1:
#       break
   
#    api_key = 'AIzaSyBCECWUQft4k8SQdwv5NvSQLB-9iHfyObs'
   
#    # new_url = url_firstpart + urllib.parse.urlencode({'address': address}) + urllib.parse.urlencode({'key': api_key})   # hear urlencode( { 'key' : value}) #here address is there in the url from google api https://developers.google.com/maps/documentation/geocoding/start
#             #we are paasing key and value here and the key name is address because thats how the Google Map API will get the value of address 
#             # We are passing it and concanitating with base url and encoding it to UTF8 / accepted standard as it will go the the server of Google 
   
#    # params = urllib.parse.urlencode({
#    #                  'address' : address,
#    #         'key' : api_key
#    #        })
   
#    params = {
#             'address' : address,
#            'key' : api_key
#           }
   
   
#    response_new_url = requests.get(url_firstpart, params= params)
#    print(response_new_url.url)
   
#    open_new_url = urllib.request.urlopen(response_new_url.url)
   
#    print('Retrieving', open_new_url)
#    # open_new_url = urllib.request.urlopen(new_url)
#    url_read_and_decode = open_new_url.read().decode()
#    print('Retrieved', len(url_read_and_decode), 'characters')
   
#    try:
#       js = json.loads(url_read_and_decode)
#    except:
#       js = None
      
#    if not js or 'status' not in js or js['status'] != 'OK':
#       print('===== Failur To Retrieve =====')
#       print(url_read_and_decode)
#       continue
   
#    lat = js["results"][0]["geometry"]["location"]["lat"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
#    location = js["results"][0]["formatted_address"]
#    print("lat", lat)
#    print("lng", lng)
#    print("Location_Address", location)
   
# address = "surat"  
# key = "AIzaSyBCECWUQft4k8SQdwv5NvSQLB-9iHfyObs"

# url = "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}".format(address=address, key=key )
# print(url)
# # http://127.0.0.1:5000/data?key=xxxx&secret=xxxx
   
# def get_mood_url():
#         url='https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?'
#         params = {
#               "sort":0,
#                   "start":0,
#               "num":20,
#             "cgi_host": "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6",
#               "replynum":100,
#               "callback":"_preloadCallback",
#               "code_version":1,
#             "inCharset": "utf-8",
#             "outCharset": "utf-8",
#             "notice": 0,
#               "format":"jsonp",
#               "need_private_comment":1
              
#               }
#         url = url + urllib.parse.urlencode(params)
#         print(url)    
   
# get_mood_url()   
            
           
# class PartyAnimal:
#    x = 0
#    def party(self):  #self works as alias for an below  - 
#       self.x = self.x + 2
#       print(self.x)
      
# an = PartyAnimal()      #Contructing and assigning it to an
# an.party()    #Calling the party method - now when call the party method - passes the parameter which is self and self.x (x is the variable here)
# an.party()                  
# an.party()

#the primary purpose of constructor we use to set up any initial values if necessary 
#the constructor is usually used to set up variables. and The destructor is seldom used


# class PartyAnimal1:
#     x = 1
#                 #self is served as the first argument and init method is served as constructor of the class
#                 #its usually used to initialize some attributes or some functions
#                 #Because this is the first method which will be called when we create an instance of the class
#     def __init__(self):  #__init__ is a special name here or is a function/method is called every time an object is created from class - IT IS CALLED WHEN INSTANCE IS ABOUT TO BE CREATED - Construct 
#         print('I am constructed and the __init__ is called')

#     def party1(self):
#         self.x = self.x + 1
#         print('So far', self.x)
    
#     def __del__(self):
#         print('I am desctructed', self.x)    
    
        
# ann = PartyAnimal1()  ##Creating Instance/object to use it further __init_ is the first method which will be called when we create an instance of the class
# #have create instance first to access the class -- so created ann = PartyAnimal() - then we can access ann. something something
# ann.party1()
# ann.party1()
# ann = 42 #this is overwriting or vaparising the the above contructors that we have created -- ITS DESCTRUCTOR -SO before this line completes it calls the- SO WILL CALL THE __del__ method and printing 42
# print('ann contains', ann) #So here ann is no longer an object - its gone its now INTEGER- So object was created and used and now its gone or destroyed
#We are allowed while building this class or object that i want to be involved at the time of creating OBJECT __init__ and AT THE TIME OF DESTRUCTED so its __del__

#In object oriented programming, a constructor in a class is a special block of statements called when an object is created
#self is the object itself
#class is a template or shape
class PartyAnimal3:
    x = 0   #called instance variables or object fields or variables
    name = ""  #called instance variables or object fields or variables
    #here we have taken two variables this time
    def __init__(self, z): #self/PartyAnimal3 is there and its when the object is contructed and z is another parameter
        self.name = z
        print(self.name, "constructed")

    def party(PartyAnimal3): #Self can also be written instead of PartyAnimal3
        PartyAnimal3.x = PartyAnimal3.x + 1
        print(PartyAnimal3.name, "party count", PartyAnimal3.x)

s = PartyAnimal3("Sully") #creating instance and passing parameter - so it will take place of z
s.party() #usig the instance

j = PartyAnimal3("Jim") #creating second instance and passing parameter - at the place of z 
j.party() #using the second instance

j.party()
s.party()     
#in the above case we have two independent Instances which retains their respective values of their respactive variables.
   
#INHERITANCE   -- its about taking one class and extending and make something new out of it
        #its the ability to extend the class to make a new class
        
#for example - there is an existing class with some data and now we just want to modify it or extend it so that we have our required class or method
#AS A RESULT , We do not have to create a new class and object with new all variables... JUST EXTEND THE EXISTING CLASS -- so its called inheritance
#its like i have got this code and data -- i just need to add this and i will get this... So that i dont have to create whole new thing or class

#here in the below example we are going to extend the above class PartyAnimal3

class FootballFan(PartyAnimal3):  #here it means - FootballFan inherites everything that PartyAnimal3 including x = 0 variables all methods and objects etc
                                  #here FootballFan is a class which extends PartyAnimal3 and it has all the capabilities of PartyAnimal3 and more.
    points= 0                       #now we are going to add a new variable
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
            
x = PartyAnimal3("Rajesh")   #self.name = Rajesh and self.x = 1  
x.party()          #self.name = Rajesh and self.x = 1  
            
f = FootballFan("Bhavin") #contructing an objecct or creating instance
f.party()     #self.x = 1 , self.name = Bhavin
f.touchdown()  #  self.points = 7 , self.name = Bhavin, self.x = 2(for that party methon in the touchdown method)



































