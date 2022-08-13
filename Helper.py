from tkinter import filedialog as FD
from tkinter.messagebox import askyesno, showwarning 
import os
import sqlite3 as SQ

class fileFetcher():
    def __init__(self) -> None:
        self.fileTypes = (("All files", "*.*"))
        self.database = None
        self.filePath = None
        self.databaseIsThere = False
    
    def LookFor(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                #print(os.path.join(root, name), "file found")
                return True
            if name not in files:
                #print("file not found in ", os.path.join(root))
                return False
        pass
    
    def SetFilePath(self):
        self.filePath = FD.askdirectory(title="Set directory", initialdir="/", mustexist=True)
        # check if data base exist, creat new database if anything but True
        if not self.LookFor("Archive.sqlite", self.filePath):
            if askyesno("Need a database?", "The path you've entered dose not have a SQLite 3 Database, do you wish to create a new one?"):
                self.CreateDatabase()
                print(0)
            else:
                showwarning("Warning!", "Database creation cancelled. you will lose any information not saved in a database! select a new path with a database or create a new database.")
        else:
            self.databaseIsThere = True
            
        
    
    def CreateDatabase(self):
        if self.filePath == None:
            
            self.SetFilePath()

        if self.databaseIsThere == False:
            path = self.filePath + "/Archive.sqlite"
            self.database = SQ.connect(path)
            print(1)
        else:
            if askyesno("conformation", "Database found, do you wish to overwrite it?"):
                path = self.filePath + "/Archive.sqlite"
                self.database = SQ.connect(path)
                print(2)

    def CloseDatabase(self, quit):
        if self.database != None:
            self.database.close()
        quit()
        


