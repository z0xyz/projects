# import re 


# url = "https://www.youtube.com/watch?v=laskfdj"
# pattern = re.compile("https://www.youtube.com/watch?v=")

# new_pattern = re.compile("http")

# matches = new_pattern.finditer(url)

# for match in matches :
#     print(match)

import time

def calcProd():
    product = 1
    for i in range (1 , 1000):
        product = product * i 
    return product 


startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The ")
print("The result of consumed time :" , str(endTime-startTime))
