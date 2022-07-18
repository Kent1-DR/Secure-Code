import datetime



now = datetime.datetime.now()

format = input("How do you want to display the current date ? \n Enter 1 for JJ/MM/YYYY or 2 for MM/JJ/YYYY or 3 for only display the hours")
format = int(format)

if format == 1:
    print (now.strftime("Current date and time : %d-%m-%Y %H:%M:%S"))


elif format == 2:
    print (now.strftime("Current date and time : %m-%d-%Y %H:%M:%S"))

else:
    print (now.strftime("Current time : %H:%M:%S"))




