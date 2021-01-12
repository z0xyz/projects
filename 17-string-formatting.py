class comedian:
	def __init__(self,first_name,second_name):
		self.name = first_name
		self.suffix = second_name
	
	def call(self ,calledName):
		return (f"hey {calledName} , my name is {self.name} ")

newComedian = comedian("mostafa" , "mahmoud")

print(newComedian.suffix)
print(f'{newComedian.call("adel")}')

firstVariable = "hey"
secondVariable = "cool"

print(
	f"Hi {firstVariable} " 
	f"How you doing {secondVariable}." \
	f" Are you okay {firstVariable} " \
)

