import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class Downlod_from_mp3clan:
    songName = ''
    def __init__(self, songName):
        self.songName = songName
    def DownlodSong(self):
        url = 'http://mp3clan.com/mp3/%s.html' % (self.songName)
        xml_page = requests.get(str(url)).text
        badsoup = BeautifulSoup(xml_page, features="html.parser")
        bucket = badsoup.find('div', {'class': 'mp3list-download'})
        salt = bucket.find('a')
        print (salt)
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element_by_class_name('mp3list-download')

        #driver.find_element_by_css_selector(1[herf='http://mp3clan.com/dl.php?type=get&amp;s=e92a991c527c9af684e26ffa45db3aa0&amp;tid=273800380_368498294&amp;name=Alan_Walker_-_Fade(original_Mix)'])
        #driver.find_element('href', 'http://mp3clan.com/dl.php?type=get&amp;s=e92a991c527c9af684e26ffa45db3aa0&amp;tid=273800380_368498294&amp;name=Alan_Walker_-_Fade(original_Mix)').click()
        #driver.find_element_by_xpath("//a[@href='http://mp3clan.com/dl.php?type=get&amp;s=e92a991c527c9af684e26ffa45db3aa0&amp;tid=273800380_368498294&amp;name=Alan_Walker_-_Fade(original_Mix)']/ax").click()
        #print requests.get(salt.get('href'))
##        "//div[@class='plan right']/a"



        #driver.get("http://www.cdot.in")
        #window_before = driver.window_handles[0]
        #print window_before
        #driver.find_element_by_xpath("//a[@href='http://www.cdot.in/home.htm']").click()
        #window_after = driver.window_handles[1]


#http://mp3clan.com/dl.php?type=get&s=c6c71314fb8eee8db111451988a744ba&tid=273800380_368498294&name=Alan_Walker_-_Fade(original_Mix)
