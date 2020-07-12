
from songs_names_form_YouTube import Songs_names_from_YouTube
from downlod_from_mp3clan import Downlod_from_mp3clan

#songsNames = Songs_names_from_YouTube('https://www.youtube.com/watch?v=0Asv4qcyazE')
songsNames = Songs_names_from_YouTube(input('Enter URL '))
songsNames.stat()
downlod = Downlod_from_mp3clan('mark ronson')
downlod.DownlodSong()