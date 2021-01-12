# import os
# import requests
# import bs4
# import googletrans

# # Function to scrap the oxrod dictionary
# def passLink(link):
#     responseObject = requests.get(link)
#     # try:
#     #      requests.get(link).raise_for_status()
#     # except Exception :
#     #     print(f"This site {link}is not working ")

#     if ( responseObject.status_code == requests.codes.ok):
#         print(f"The site {link} is working")
    
#     openedFile = open(os.getcwd()+"/20-web-scraping.txt" , "wb")
#     for chunk in responseObject.iter_content(10000):
#         openedFile.write(chunk)
#     openedFile.close()
#     sameOpenedFile = open(os.getcwd()+"/20-web-scraping.txt" , "r")
#     soubObject = bs4.BeautifulSoup( sameOpenedFile , "html.parser")
#     print(soubObject.select(".fw3eif"))
#     return (responseObject)

# passLink("https://www.dictionary.cambridge.org/us/dictionary/english/game")
# passLink("https://www.asfdasdfasdfsa.com")



from google_trans_new import google_translator
import sys

translator = google_translator()

word = input("Add some word to translate : ")

target = input('''Which language you wanna translate the word to :
\tru-\tRussian
\ten-\tEnglish
\tfr-\tFrench
\tfi-\tFinish
''')

print(translator.translate(word , lang_tgt=target))




# passLink("https://translate.google.com/?sl=en&tl=ru&text=game&op=translate")
# googletrans.Translator.translate("cyka" , dest="en")