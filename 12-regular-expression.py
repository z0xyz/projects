# RegEx : "\d({3})-\d\d\d-\d\d\d\d "

# import re

# phoneNumberRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
# matchObject = phoneNumberRegex.search("My number is (415) 555-4242 , 423-999-3982 ")



# if type(matchObject) != type(None) :
# 	print(matchObject.group())
# 	print(matchObject.group(1))
# 	print(matchObject.group(2))
# 	print(matchObject.groups())


# 	areaCode , mainNumber = matchObject.groups()

# 	print(areaCode)
# 	print(mainNumber)

# 	print(type(phoneNumberRegex))

# 	print(type(re))


# Matching multiple groups

# import re

# ndRegexObject = re.compile(r"bat(man|mobile|copter|bat)")
# ndMatchObject = ndRegexObject.search("hey mostafk , how you batmobile and batman and batmobile abnd batcopter and batbat adel ")

# if type(ndMatchObject) != type(None):
# 	print(ndMatchObject.group())
# 	print(ndMatchObject.group(0))
# 	print(ndMatchObject.group(1))

#side project
#This crappy code is actually working !

# import re

# rdRegexProject = re.compile(r"\[info\] Writing video subtitles to: (.*)-.*.en.vtt\n\[download\] Downloading video \d of \d*\n\[youtube\] \w*: Downloading webpage\n\[youtube\] \w*: Downloading MPD manifest")
# matchObject = rdRegexProject.search(
# '''[info] Writing video subtitles to: Introduction to Mathematics-JbhBdOfM9EPs.en.vtt
# [download] Downloading video 2 of 165
# [youtube] rV7WjNWHOsI: Downloading webpage
# [youtube] rV7WjNWHOsI: Downloading MPD manifest

# [info] Writing video subtitles to: Addition and Subtraction of Small Numbers-rV7WjNWHOsI.en.vtt
# [download] Downloading video 3 of 165
# [youtube] fr04p6Ar9ic: Downloading webpage
# [youtube] fr04p6Ar9ic: Downloading MPD manifest''')


# if type(matchObject) != type(None):

# 	print(matchObject.group())
# 	print(".........")
# 	print(matchObject.group(1))




#Multi search & matching

import re

rdRegexProject = re.compile(r"\[info\] Writing video subtitles to: (.*)-.*.en.vtt\n\[download\] Downloading video \d of \d*\n\[youtube\] \w*: Downloading webpage\n\[youtube\] \w*: Downloading MPD manifest")
matchObject = rdRegexProject.findall(
'''[info] Writing video subtitles to: Introduction to Mathematics-JbhBdOfM9EPs.en.vtt
[download] Downloading video 2 of 165
[youtube] rV7WjNWHOsI: Downloading webpage
[youtube] rV7WjNWHOsI: Downloading MPD manifest

[info] Writing video subtitles to: Addition and Subtraction of Small Numbers-rV7WjNWHOsI.en.vtt
[download] Downloading video 3 of 165
[youtube] fr04p6Ar9ic: Downloading webpage
[youtube] fr04p6Ar9ic: Downloading MPD manifest''')


if type(matchObject) != type(None):
	for item in matchObject:
		print(item)



#This is the dold crap , it didn't work out , 
# it just printed out two matches (i assume all the matches not just the first one for some reasom 
#I solved the problem by using the (.*) metcharacter , but i wanna understand this behavior

# import re

# rdRegexProject = re.compile(r"\[info\] Writing video subtitles to: (\d|\D)*\n\[download\] Downloading video \d of \d*\n\[youtube\] \w*: Downloading webpage\n\[youtube\] \w*: Downloading MPD manifest")
# matchObject = rdRegexProject.search(
# '''[info] Writing video subtitles to: Introduction to Mathematics-JbhBdOfM9EPs.en.vtt
# [download] Downloading video 2 of 165
# [youtube] rV7WjNWHOsI: Downloading webpage
# [youtube] rV7WjNWHOsI: Downloading MPD manifest

# [info] Writing video subtitles to: Addition and Subtraction of Small Numbers-rV7WjNWHOsI.en.vtt
# [download] Downloading video 3 of 165
# [youtube] fr04p6Ar9ic: Downloading webpage
# [youtube] fr04p6Ar9ic: Downloading MPD manifest''')


# if type(matchObject) != type(None):

# 	print(matchObject.group())
# 	print(".........")
# 	print(matchObject.group(1))
