import re


if re.search("[0-9][0-9][0-9]" , "somega123meyay"):
	print("Found a match")
	print(re.search("123" , "some123yay"))
	print(re.search("123" , "some123yay").span())
else :
	print("No match")

# r"\[info\] Writing video subtitles to: ((\D|\d)*)\n\[download\] Downloading video \d of \d*\n\[youtube\] \w*: Downloading webpage\n\[youtube\] \w*: Downloading MPD manifest"
