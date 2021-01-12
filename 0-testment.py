# someDictionary = {
# 	"hey":"hey" , 
# 	"age" : 19 , 
# 	"years" : 100 , 
# 	"profession" : "PoliceOfficer"
# }

# print(type(someDictionary.values()))
# import random

# someList = ["firstt" , "second" , "third" , "forth" , "first" , "sixth" , "seventh"]

# print(someList.index("first"))

# firstSample = random.sample(someList, 3)

# print(firstSample)

# someList = ["hey" , "this" , "is"]

# someDictionary = {
# 	"hey":"name" ,
# 	"age" : "someAge"
# }


# print(type([someDictionary["hey"]]))

# print(someList)

nums = [1,2,4,9,3,9,9,9]

for num in range(1,len(nums)+1):
	if num not in nums:
		print(num)
