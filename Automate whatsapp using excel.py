#This program retrieves the customers' data from an excel file and send them an automatic message.

import pywhatkit
import openpyxl

sheet = openpyxl.load_workbook(input("Enter path to your xlsx file: "))        #get access to the excel file.


numbers=[]
colonne = input("Enter column letter for phone numbers: ")      #choose the column where the phone numbers are stored
for i in range(1,int(input("How many People do you wish to send message to? : "))):     
    new=sheet[colonne + str(i)].value       #get the value of the 1st cell
                            
    if  new[0:2]=="00":
        new=new.replace("00","+")
                            
    if new[0]=="0":
        new="+" + new[1:]
                            
    numbers.append("+" + new)       #add the phone number to the list after writing in a format recognizable by the texting function

hrs = int(input("At hour: "))
mins = int(input("Minute: "))       #the time that you wish to send the message
pay = input("Enter the payment website: ")      #the payment website to send to the customer
for i in range(1,len(numbers)+1):

    msg= """Hello """ + str(sheet["A" + str(i)].value) + """ My name is HAMDOUDI Tarek, a selling specialist at b:hip global. We have found that one of our products interests you.
        We invite you to make your payment on the following website: """ + pay + """. Thank you for choosing our brand.\n Have a nice day :) !"""       #the message to send
    pywhatkit.sendwhatmsg(numbers[i-1], msg, hrs, mins)         #send the message to the phone number specified at a certain time
    mins += 1

    if mins == 60:
        mins = 0
        hrs += 1
    if hrs == 24:
        hrs = 0
#adjusting the time format
