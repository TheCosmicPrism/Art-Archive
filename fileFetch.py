from tkinter import filedialog as FD
import os
from types import NoneType

class fileFetcher():
    def __init__(self) -> None:
        fileTypes = (("All files", "*.*"))
        self.database = None
    
    def SetFilePath(self):
        filePath = FD.askdirectory(title="Set directory", initialdir="/", mustexist=True)
        # check if data base exist, creat new database if anything but True
        if self.database != True:
            pass
        print(filePath)
    
    def GetFilePath():
        pass


