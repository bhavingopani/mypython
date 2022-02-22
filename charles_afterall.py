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

#Oauth


import urllib.request, urllib.parse, urllib.error
import json
import requests

url_firstpart = 'https://maps.googleapis.com/maps/api/geocode/json?'  # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY


while True:
   address = input('Enter Location: ')
   if len(address) < 1:
      break
   
   api_key = 'AIzaSyBCECWUQft4k8SQdwv5NvSQLB-9iHfyObs'
   
   # new_url = url_firstpart + urllib.parse.urlencode({'address': address}) + urllib.parse.urlencode({'key': api_key})   # hear urlencode( { 'key' : value}) #here address is there in the url from google api https://developers.google.com/maps/documentation/geocoding/start
            #we are paasing key and value here and the key name is address because thats how the Google Map API will get the value of address 
            # We are passing it and concanitating with base url and encoding it to UTF8 / accepted standard as it will go the the server of Google 
   
   # params = urllib.parse.urlencode({
   #                  'address' : address,
   #         'key' : api_key
   #        })
   
   params = {
            'address' : address,
           'key' : api_key
          }
   
   
   response_new_url = requests.get(url_firstpart, params= params)
   print(response_new_url.url)
   
   open_new_url = urllib.request.urlopen(response_new_url.url)
   
   print('Retrieving', open_new_url)
   # open_new_url = urllib.request.urlopen(new_url)
   url_read_and_decode = open_new_url.read().decode()
   print('Retrieved', len(url_read_and_decode), 'characters')
   
   try:
      js = json.loads(url_read_and_decode)
   except:
      js = None
      
   if not js or 'status' not in js or js['status'] != 'OK':
      print('===== Failur To Retrieve =====')
      print(url_read_and_decode)
      continue
   
   lat = js["results"][0]["geometry"]["location"]["lat"]
   lng = js["results"][0]["geometry"]["location"]["lng"]
   location = js["results"][0]["formatted_address"]
   print("lat", lat)
   print("lng", lng)
   print("Location_Address", location)
   
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
            
           
            
   
   
   
































