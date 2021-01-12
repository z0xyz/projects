# This is a presumably phone number validation for United kingdom

def isPhoneNumber(text):
	if len(text) != 12:
		return (False)
	for i in range(0,3):
		if not text[i].isdecimal():
			return (False)
	if text[3] != "-":
		return (False)
	for i in range(4,7):
		if not text[i].isdecimal():
			return (False)
	if text[7] != "-":
		return (False)
	for i in range(8,12):
		if not text[i].isdecimal():
			return (False)
	return (True)

def phnoCheck(text):
	for i in range(len(text)):
		chunk = text[i:i+12]
		if isPhoneNumber(chunk):
			print("Phone number found : " + chunk)

print(isPhoneNumber("333-333-3984"))
print(isPhoneNumber("my phone number is 333-333-3984"))

phnoCheck("my phone number is 333-333-3984")

# Number Validation for egypt

# def checkEg(phone):
# 	if not len(phone) in [11 , 12 , 13]:
# 		return (False)

# 	if len(phone) == 11 :
# 		if not phone.isdecimal():
# 			return (False)
# 		if not phone[0:2] == "01":
# 			return (False)
# 		if phone[2] not in ["0","1","2"] :
# 			return (False)

# 	if len(phone) == 12:
# 		if not phone.isdecimal():
# 			return (False)
# 		if not phone[0:3] == "201":
# 			return (False)
# 		if phone[3] not in ["0","1","2"] :
# 			return (False)

# 	if len(phone) == 13:
# 		if not phone[1:14].isdecimal():
# 			return (False)
# 		if not phone[0:4] == "+201":
# 			return (False)
# 		if phone[4] not in ["0","1","2"] :
# 			return (False)

# 	return (True)





# print(checkEg("01090943929"))
# print(checkEg("201090943929"))
# print(checkEg("+201090943929"))
# print(checkEg("01090943929"))