import os

# print(os.path.join("user","bin","spam"))

# print(os.getcwd())


# myFiles = ["firstFile.docs" , "secondFile.docs" , "thirdFile.docs"]

# for file in myFiles:
# 	print(os.path.join(os.getcwd() , file))



newTextFile = open("/media/usr/localdisk/python/python-projects/newfile.txt", "a")

print(type(newTextFile))

print(newTextFile.write("hey , this is an append"))

newTextFile.close()

readMode = open("/media/usr/localdisk/python/python-projects/newfile.txt")

print(readMode.read())

