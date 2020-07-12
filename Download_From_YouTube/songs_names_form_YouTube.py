import requests
from bs4 import BeautifulSoup

class Songs_names_from_YouTube:
    url = ''
    def __init__(self, url):
        self.url = url
    def stat(self):
        badSoup = self.Scan_YouTubePage()
        self.BadSoup_TO_GoodSoup(badSoup)
    def Scan_YouTubePage(self):
        xmlPage = requests.get(self.url).text
        badSoup = BeautifulSoup(xmlPage, features="html.parser")
        return badSoup
    def BadSoup_TO_GoodSoup(self, badSoup):
        songsName = {''}
        num = 0
        songsName.clear()
        salt = str(badSoup.find('p', {'id': 'eow-description'}))

        while '<a href="#"' in salt:
            salt = salt[salt.index('<a href="#"'):]
            salt = salt[salt.index('</a>') + 4:]
            chack = salt[:salt.index('<br/>')]                           # validate song name start only with leters
            while True:
                if chack[0].isalpha():
                    break
                else:
                    chack = chack[1:]
            songsName.add(chack)
            salt = salt[salt.index('<br/>'):]

            if '<a href="#"' not in salt:
                print ('lol')
                num += 1
        print (salt)


        print (songsName)

    #def Get_Songs_names(self, goodSoup):

#<a href="#"