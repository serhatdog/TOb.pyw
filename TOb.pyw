from os import path, remove, listdir, removedirs, system
from time import sleep

class TOb:

    def __init__(self, path, settings) -> None:
        self.path = path
        self.tempfile = 'tempfile0000000.txt'

        self.files = listdir(path)
        self.files.remove('desktop.ini')

        self.seconds = (((settings['d'] * 24) * 60) * 60) + ((settings['h'] * 60) * 60) + settings['m'] * 60 + settings['s']

    def clear(self): 
        with open(self.path+self.tempfile, 'w'): pass
        for i in range(len(self.files)):
            time = path.getatime(self.path+self.tempfile) - path.getatime(self.path+self.files[i])
            if time > self.seconds:
                try:
                    remove(self.path+self.files[i])
                except:
                    folder = listdir(self.path+self.files[i])
                    for j in range(len(folder)):
                        remove(self.path+self.files[i]+'\\'+folder[j])
                    try:
                        removedirs(self.path+self.files[i])
                    except: system('pause')
        remove(self.path+self.tempfile)

    def auto(self, time_option, value):
        if time_option == 'h': value = (value * 60) * 60
        elif time_option == 'm': value = value * 60
        elif time_option == 'd': value = ((value * 24) * 60) * 60

        while True:
            self.clear()
            sleep(value)