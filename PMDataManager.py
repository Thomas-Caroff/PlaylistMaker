import os

class File: 
    #Class representing each file affected by the playlist creation and edition.
    #Caracterised by the file's name, actual position and last known position.
    
    def __init__(self, name = "", position = 0, shorten = 60):
        self.name      = name
        self.position  = position
        self.previous  = position
        
        if (len(self.name) > shorten):
            self.shortname = name[0:shorten] + ' ...'
        else:
            self.shortname = name
        
    def rename(self, prefixe=0): #Change file's position
        self.position = prefixe
        return 0
        
        
class Playlist:
    
    def __init__(self, wdir = os.getcwd()):
        self.list    = []
        self.lenght  = 0
        self.error   = []
        self.workDir = wdir
        
        self.load()
                
    def update(self, oldValue, newValue):
        if (oldValue < newValue):
            for line in range(oldValue+1 ,newValue+1):
                self.list[line-1].rename(line-1)
            self.list[oldValue-1].rename(newValue)

        elif (oldValue == newValue):
            self.error.append('Aucun changement effectué, les valeurs sont identiques')

        else:
            for line in range(newValue, oldValue):
                self.list[line-1].rename(line+1)
            self.list[oldValue-1].rename(newValue) 
        
        print(len(self.list))   
        self.overwrite()
        self.load() 
        return 0
          

    def load(self):
        dirFiles = os.listdir(self.workDir)
        loadList = []
        loadLenght = 0
        for elmt in dirFiles:
            if '#' not in elmt:
                os.rename(str(self.workDir) + str(elmt), str(self.workDir) + '#' + str(elmt))

            file = File(str(elmt), int(loadLenght) + 1)
            if (file):
                loadLenght += 1
                loadList.append(file)
            else:
                self.error.append('Le fichier %s n\'a pas pu etre ajouté' % elmt)
        
        self.list   = loadList
        self.lenght = loadLenght
        return 0
    
    def overwrite(self):
        dirFiles = os.listdir(self.workDir)     
        for file in self.list:
            #os.rename(elmt.name)
            print(file.position, file.name)
            #for elmt in dirFiles :
                #print(elmt)
        

         
        
           
            
            
            
            
        
    
        
    