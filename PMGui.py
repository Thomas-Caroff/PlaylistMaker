import tkinter as tk
import PMDataManager as man
import os

class Line:
    
    def __init__(self, frame, position, title):
        self.memPosition = position
        self.position = tk.IntVar(value = position, master = root)
        self.title    = tk.StringVar(value = title, master = root)
        self.entry    = tk.Entry(frame, width=3, text = self.position)
        self.label    = tk.Label(frame, text=title, justify='left')
        self.button   = tk.Button(frame, text="▶", command=self.validate)
        
    def create(self,rowNum):
        self.entry.grid(row=rowNum, column=1)
        self.label.grid(row=rowNum, column=2, sticky = "W")
        self.button.grid(row=rowNum, column=0)

    def validate(self):
        newPosition = self.position.get()
        oldPosition = self.memPosition
        playlist.update(oldPosition, newPosition)
        oldPosition = newPosition
        

def generateList(playlist, frame = None):
    table = []
    size = playlist.lenght
    for i in range(1, size+1):
        line = Line(frame, playlist.list[i-1].position, playlist.list[i-1].shortname)
        line.create(i)
        table.append(line)
    frame.update()
    return table

def updateList(table,playlist):
    for elmt in table:
        if (table[elmt].position != playlist.list[elmt].position):
            table[elmt].position = playlist.list[elmt].position

def generateGui(playlist):
    global root
    root = tk.Tk()
    root.title('Playlist Maker (Version alpha)')

    #root.title('Playlist Maker (' + playlist.workDir +')')
    root.geometry('1100x600')
    
    canvas = tk.Canvas(root)
    canvas.grid(row=0, column=0, sticky='nswe')
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    
    hScroll = tk.Scrollbar(root, orient='horizontal', command=canvas.xview)
    vScroll = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
    hScroll.grid(row=9, column=0, sticky='we')
    vScroll.grid(row=0, column=9, sticky='ns')
    
    canvas.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
    
    frame = tk.Frame(canvas)
    
    generateList(playlist,frame)
    
    canvas.create_window(0, 0, window=frame, anchor='nw')
    canvas.configure(scrollregion=canvas.bbox('all'))
    
    root.mainloop()

if __name__ == '__main__':
    path = os.getcwd() + '\\data\\'
    playlist = man.Playlist(path)
    table = generateGui(playlist)
