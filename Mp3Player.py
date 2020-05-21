
# This is a basic music player - done with Python Tkinter and Pygames

# The structure of the logic of the coding is written first by commenting

# The program should contain:

# import Tkinter and Pygame
from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import pygame

# Define the playlist
playlist = []

# Define the player functions under the application. The frame of player goes in as attribute

class Application(Frame):
    
    def __init__(self, master):
        
        # self.create_widgets()
        self.playlistbox = Listbox(self, width = 40, height = 10, selectmode = SINGLE)
        for song in playlist:
            self.playlistbox.insert(END, song)
        
        # Define parts of the player as class attributes:
        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row=1)
        self.playButton = Button(self, text, = 'Play', command = self.play)
        self.loopButton = Button(self, text, = 'Loop', command = self.loop)
        self.addButton = Button(self, text, = 'Add', command = self.add)
        self.playButton.grid(row = 4, column = 0)
        self.loopButton.grid(row = 4, column = 1)
        self.addButton.grid(row = 4, column = 2)
        self.pack()
        
        # pygame initialize
        pygameme.init()
    
    # Define player functions as methods of the class
    def play(self):
        """Define when playlist is empty: Show graphical notice."""
        if(len(playlist) == 0):
            tk2.showinfo('Notice', 'No song in your playlist!\nClick Add to add songs.')
        """Define actions when playing list, incl. stop, select song,
        play the playlist, and load and play."""
        else:
            pygame.mixer.music.stop()
            selectedSongs = self.playlistbox.curselection()
            global playlistbox
            playIt = playlist[int(selectedSongs[0])] # list of selected songs into variable playIt
            pygame.mixer.music.load(playIt) # loads the list of songs stored in the variable
            pygame.mixer.music.play(0, 0.0)
    
    # Define looper functions as methods:
    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,0.0)
        
    # Define add-function of the player as a method:
    def add(self):
        initialdir = input('Give the path for your directory of the music: ')
        file = tk.askopenfilenames(initialdir)
        songsTuple = root.splitlist(file) # Turn user's opened filenames into tuple
        songList = list(songTuple) # convert the formed tuple into list
        
        # Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songsList:
            playlist.append(song)
            tempArray = song.split('/')
            songShort = tempArray[len(tempArray)-1]
            self.playlistbox.insert(END, songShort)
            
root = Tk()
root.title('Text Editor')
root.geometry('500x200')
app = Application(root)
app.mainloop()
