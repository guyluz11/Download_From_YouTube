import os
from colorama import Fore, Style


class DelMp3Com:
    thereIsNoPlaceLike_127_0_0_1 = ''

    def __init__(self, place):
        self.thereIsNoPlaceLike_127_0_0_1 = place

    def start(self):
        self.change_dir_to_start_location(self.thereIsNoPlaceLike_127_0_0_1)
        self.fuck_all(self.thereIsNoPlaceLike_127_0_0_1)

    def change_dir_to_start_location(self, place):
        os.chdir(place)

    def chnge_name_to(self, file):
        if ' [mp3clan.com]' in file:
            os.rename(file, file.replace('[mp3clan.com]', ''))
        elif ' - (4songs.PK)' in file:
            os.rename(file, file.replace(' - (4songs.PK)', ''))
        elif '- YouTube' in file:
            os.rename(file, file.replace('- YouTube', ''))
        elif 'YouTube'in file:
            os.rename(file, file.replace('YouTube', ''))

    def fuck_all(self, folder):
        print(folder)
        os.chdir(folder)
        for folderOrFile in os.listdir(folder):
            try:
                if os.path.isdir(folderOrFile):
                        self.fuck_all(folder+'/'+folderOrFile)
                        os.chdir(folder)
                else:
                    self.chnge_name_to(folderOrFile)
            except():
                print(Fore.RED + "can't do this faking shit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)

