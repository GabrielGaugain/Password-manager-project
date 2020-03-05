import os 
import sys

# Tkinter imports
import tkinter as tk
from tkinter import filedialog, N,S,E,W

# Import to simply generate pw
from random import randint, choice
import string

#modules import
import file_operations as mf
from dialogue import Dialogue
from Globals import *

#### All the pop windows herit from dialogue class 

############   Pop win to enter a new password   ############
class Password_entry(Dialogue) :

    def cover(self,cont):
        """
        Define the cover of the dialog window
        """
        # Defines the look of the dialog window
        if sys.platform.startswith('win'):
            self.iconbitmap(logo_path)
        self.geometry("360x240")
        self.minsize(230,100)
        self.maxsize(480,360)
        self.config(background=bg_color)
        cont.config(background=bg_color)
        # Labels
        NameLabel = tk.Label(cont, text = "Name : ",bg = bg_color,fg ='white')
        NameLabel.grid(row = 1,column =1,pady=5)
        SiteLabel = tk.Label(cont, text = "url (opt) : ",bg = bg_color,fg ='white')
        SiteLabel.grid(row=2,column=1,pady =5)
        PwLabel = tk.Label(cont,text = "Password : ", bg = bg_color,fg ='white')
        PwLabel.grid(row=3 , column=1,pady=5)
        # Add their corresponding input
        self.NameEntry = tk.Entry(cont)
        self.NameEntry.grid(row=1, column=2)
        self.SiteEntry = tk.Entry(cont)
        self.SiteEntry.grid(row=2,column=2)
        self.PwEntry = tk.Entry(cont)
        self.PwEntry.grid(row=3 , column=2)
        
        return self.NameEntry

        
    def apply(self):
        """
        Method which gets the entered infos and return  them as a 
        Password object
        """
        name = self.NameEntry.get()
        url = self.SiteEntry.get()
        pw = self.PwEntry.get()
        self.resultat = mf.Password(site=name , link = url,password = pw)
        print(self.resultat)

    def boitBoutons(self):
        """
        Method which adds buttons to get infos and generate pw or quit
        """
        boite = tk.LabelFrame(self, text="") 
        boite.config(background = self.color)
        # add the entered info to the db 
        w1 = tk.Button(boite, text = "Add.", width = 10,
                           command = self.ok, default = tk.ACTIVE)
        w1.pack(side=tk.LEFT, padx = 5, pady = 5)       
        # Generate password button
        w2 = tk.Button(boite, text = 'Generate', width=10,
                            command = self.generate_password)
        w2.pack(side = tk.LEFT, padx=5,pady=5)
        # Cancel button
        w3 = tk.Button(boite, text = "Cancel", width = 10,
                            command = self.cancel)
        w3.pack(side=tk.LEFT, padx = 5, pady = 5)       
        
        self.bind("<Return>", self.ok)     
        self.bind("<Escape>", self.cancel)        
        boite.pack()        
        return w1
    
    def generate_password(self,nb_char=10):
        """
        Methods to easily generate random password using string
        """

        all_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join( choice(all_chars) for x in range(nb_char) )
        self.PwEntry.delete(0,tk.END)
        self.PwEntry.insert(0,password)
        return password


###########  Pop window to changes settings of the app   ##############
class Settings_win(Dialogue):
    
    def cover(self,cont):
        # Defines the look of the dialog window
        if sys.platform.startswith('win'):
            self.iconbitmap(logo_path)
        self.geometry("480x360")
        self.minsize(230,100)
        self.maxsize(480,360)
        self.config(background=bg_color)
        cont.config(background=bg_color)
        
    
    def apply(self):
        pass

    def boitBoutons(self):
        pass

