while True:
	print("Enter your username")
	username = input()
	if username.isalpha():
		break

while True :
	print("Enter your age")
	age = input()
	if age.isdecimal():
		break
	print("Please enter a NUMBER for your age")


while True:
	print("Enter a new password (numeric & letters) ")
	password = input()
	if password.isalnum():
		break

print("your information is :\n" , "username:\t" , username , "\n" , "password:\t" , password)