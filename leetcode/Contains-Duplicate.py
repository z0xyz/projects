#first solution : didn't get accepted ; because it exceeded the allowed time 

def containsDuplicate(nums):
	i = 0
	while i < len(nums) :
		poppedItem = nums[i]
		nums.pop(i)
		for item in nums:
			if item == poppedItem :
				return True


#Second solution

def cotnainsDuplicate(nums):
	if len(nums) > len(set(nums)):
		return(True)
	else :
		return (False)


