# TCP - Transport Control Protocol
#Transport layer - where computer makes a phone call to another computer

#pipe
#this is called sockets - one process running on one computer and another process running on another computer
#data phone calls between applications
#application may be on one side its browser and on the other side its a web server
#So this data phone call - we call it socket

#it has to be decided which of the sysyem we are going to talk to 

#TCP Port Number
    #A port is an application-specific or process-specific sofware communications endpoint
    #it allows multiple networked applications to coexist on the same server
    #there is a list of well-known TCP port numbers
    #or you can say extension of something like port number
    #its like i am the server and please enter the extension you would like to talk to
    
    #for example
    # 25  - incoming E-mail
    # 23  - login or secured login
    # 80  - Unsecured web on 80
    # 443 - Secured web on 443
    # 109 and 110  - different local email client like Thunderbirds or Apple mails - they are on different ports
    
    #by convention they have standard that tell us what to roughly expect 
      #for example - when you talk to port 80 you are expected to talk to a web server - http and 443 - you exepect to talk to telnet or secured server
      #in URL you see :8080  -- that means its a web server  that is running other than port no:80 - they are called non-standard port
      
#Sockets in Python

#Python has built-in support for TCP Sockets

#import socket  #its the library that is in-built

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #in socket.socket - the first is the socket libraby and .socket - is the socket function
        #AF_INET is that - we are making a socket that goes on the internet and Its STREAM socket - that meas its a searis of characters that will come one after the another rather than a series of blocks of texts
        #Just type the above line - means that its goin to create a socket that is not yet associated
#mysock.connect(('data.pr4e.org', 80)) #here the first is the Host and 80 is the Port
    #now in the above line we are making a connection
    #we are saying that Dear Socket extend yourself to the internet and  make a phonecall or connection to the Host called data.pr4e.org on the Port 80
    #its like making the phone call HERE ITS LIKE -- data.pr4e.org is the NUMBER and 80 is the extension
    #here we have not sent any data yet its just we have rung the phone
    #if there is no one or nothing like it it will blow up

#Application Protocols 
# after making connection we should know what kind of data are we supposed to Send and What type of data we expect to receive accross that socket - this is called application protocols

#the most dominent application layer protocol is the HTTP Protocol on the internet - Hypertext Transfer Protocol
#was invented for the web- to retrieve HTML, images, documents, etc.
#extended to be data in addition to documents - RSS, Web Services, etc. Basic Concept - 
    #Make a connection - Request a document - Retrive the document - Close the connection 

#http is easy to understand but there are many other protocols like for email, file transfer and many other
    #they all have a lower layer called socket and on top of there are rules of them or Protocols

# http://www.dr-chuck.com/page1.htm
# protocol // Host      // document
# Whenever we click on links of any thing on a webpage the Browser or the application makes a connection request
# In return the Web server do some work and  Constructs an answer to our phone call and send it back in web page in a format of HTML
# Our browser gets it back and render it according to the rules of html/css/js etc. and makes it a webpage 
#THIS IS CALLED REQUEST and RESPONSE CYCLE - WHICH IS GOVERNED BY a searies of Internet standards - have been built or building by a group called IETF
#this STANDARDS are called "RFCs" - "Request for Comments"

#   telnet www.dr-chuck.com 80   in terminal   -- telnet is a program to open a socket To host on a port
# GET http://www.dr-chuck.com/page1.htm HTTP/1.0
# 
#HTTP/1.1 200 OK   #this all 5 lines are the reponse from server - Called headers - its the metadata about the document that we are going to get like content type etc
#Date: Thu, 08 Jan 2015 01:57:52 GMT
#Last-Modified: Sun, 19 Jan 2014 14:25:43 GMT
#Connection: close
#Content-Type: text/html
#
#<h1> The First page </h1>
#<p>if you like, you can switch to the </p>
#Connection closed by foriegn host.



#WRITE A SIMPLE PYTHON WEB BROWSER

# import socket #importing librabry
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a socket not yet associated - socket for going accross internet and STREM is the how its going to go with searies of characters one after the another instead of Blocks of Text
# mysock.connect(('data.pr4e.org', 80)) #rung the phone call - making a phone call
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #here \n\n this means two new lines the same we had in the ternminal in telnet #encode is converting data in to UTF 8
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512) #512 characters at a time - 512 each time
#     if (len(data) <1): #if we get 0 character that means its the End of STREAM and STREAM is closed
#         break
#     print(data.decode())   #decode is to convert that encoded data and decode it into Unicode
# mysock.close()

#TEXT Processing
    #first it was American Standart character - ASCII - 1Byte
    # Then it was Unicode - could send any character but - UTF 32 - Fixed length and Four Bytes per character - It will increase the size by 4 times
    # UTF 16 - Two Bytes - subset of Unicode
    #UTF 8 -- THE BEST PRACTICE FOR MOVING DATA ACCROSS THE INTERNET OR in a file that you move between computers 
        #UTF 8 has dynamic Length - 1 to 4 Bytes
            #if its 1 byte long then Compatible with ASCII - 1 byte
            #Autometic Detection between ASCII and UTF-8
            #UTF-8 is recommended practice - it can represent all
            
    #Python 3.0 and above has all Unicode formate versis python 2 had Unicode and Bytes too
    

#Now we are doing the above thing which was with socket - We will do that with urllib
#Shorter

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')   #it does all the above things that is done in the above code encode it too.
# # for line in fhand:
# #     print(line.decode().stripe())
      
# #can also treat this like a file

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)



# fhand2 = urllib.request.urlopen('http://data.pr4e.org/page1.htm') 
# for line in fhand2:
#     print(line.decode().strip())
    

#WEB SCRAPPING

#Use the free software library called Beautiful Soup from www.crummy.com

# from bs4 import BeautifulSoup

# url = input('http://www.dr-chuck.com/page1.htm')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# #retrieve all the anchor tag

# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

    
#WIRE PROTOCOL

#HOW DATA is sent and the format that is understandable by all languages and can talk to any aplication - JSON and XML
#Sending data accross internet - JSON and XML --- independent of any languages
#SO first Serializing data  happens and Then Deserializing the same data happens by other application
#MARK UP language is used or ways to send data between computers especially on Internet and kind of protocol which every applicaion follows to understand the communication and data that is coming from other application
#XML 

