from os import path, remove, listdir
from time import sleep
import shutil

class TOb:

    def __init__(self, path, settings, noremove) -> None:
        self.path = path
        self.tempfile = 'tempfile0000000.txt'

        self.files = listdir(path)
        for filename in noremove:
            try:
                self.files.remove(noremove)
            except: pass

        self.seconds = (((settings['d'] * 24) * 60) * 60) + ((settings['h'] * 60) * 60) + settings['m'] * 60 + settings['s']

    def clear(self): 
        with open(self.path+self.tempfile, 'w'): pass
        for i in range(len(self.files)):
            time = path.getctime(self.path+self.tempfile) - path.getctime(self.path+self.files[i])
            if time > self.seconds:
                try:
                    shutil.rmtree(self.path+self.files[i])
                except:
                    try:
                        remove(self.path+self.files[i])
                    except: 
                        with open(self.path+'ERROR.log', 'w') as f: f.write("TOb.pyw got stuck when deleting files/folders!")
        remove(self.path+self.tempfile)

    def auto(self, time_option, value):
        if time_option == 'h': value = (value * 60) * 60
        elif time_option == 'm': value = value * 60
        elif time_option == 'd': value = ((value * 24) * 60) * 60

        while True:
            self.clear()
            sleep(value)

#Author: Serhat Dogan
#https://github.com/serhatdog/TOb.pyw/
