#this script is complete
#it prompots the user to enter some data
#then it just prints it saves it in a file
#as some sort of a minmalistic database

import os

birthdays = {"alice":"apr1" , "bob":"aug28" , "amanda":"jan30"}

while True:
	name = input("Add your name: (leave blank to quit) ")
	if name == "":
		break
	if name in birthdays:
		print("The birthday for :" , name , "is :" , birthdays[name])
	else :
		print("I don't have the birthday for :" , name)
		print("what's their birthday ?")
		bday = input()
		birthdays[name] = bday
		print("The user has been added to the database")

dummyString = ""
for keyName in birthdays:
	dummy = "\t" + keyName  + "\t:\t" + birthdays[keyName] + "\n"
	dummyString += dummy 


print(dummyString)

birthdaysFileObject = open("/media/usr/localdisk/python/python-projects/newfile.txt" , "w")
birthdaysFileObject.write(dummyString)
birthdaysFileObject.close()
print('The database has been updated')
