import os
import sys
import webbrowser
import pyperclip 
import time
import requests
import bs4

#function : Get reponse object
def passLink(link):
    responseObject = requests.get(link)
    try:
        responseObject.raise_for_status()
    except Exception as exec:
        print("There was a problem : %s" %(exec))

    # Write response object's content to a text file
    fileObject = open(os.getcwd()+"/18-web-scraping.html" , "wb")
    for chunk in responseObject.iter_content(100000):
        fileObject.write(chunk)
    fileObject.close()

    # BeautifulSoup return object
    someFile = open("./18-web-scraping.html" , "r")
    soupObject = bs4.BeautifulSoup(someFile , "html.parser" )
    soupMatch = soupObject.select(".wu-value-to")
    print(type(soupObject))
    print(type(soupMatch))
    print(len(soupMatch))
    print(f'The weather today at cairo : {soupMatch[0].getText()} F ')
    print(type(str(soupMatch[0])))
    print(f'The attributes of this HTML element are : {soupMatch[0].attrs} ')



passLink("https://www.wunderground.com/weather/us/ar/egypt")

# // var newPop = document.getElementsByClassName("entry-body")[0].scrollIntoView() ;
# // newInput.value = "" ;

# print(requests.get("https://www.facebook.com").text)

# socialLinks = '''
# https://www.reddit.com/r/learnpython
# https://wwww.twitter.com
# https://wwww.facebook.com
# https://www.4chan.org
# '''

# for link in socialLinks.splitlines():
#     webbrowser.open(f"{link}")
#     time.sleep(3)



# if len(sys.argv) > 1 :
#     #Get the address of the command line
#     address = " ".join(sys.argv[1:])
# else :
#     address = " ".join(pyperclip.paste())

# webbrowser.open(f"https://www.google.com/maps/place/{address}")
