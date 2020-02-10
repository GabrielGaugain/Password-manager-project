import tkinter as tk
import tkinter.tix as tix
from tkinter import filedialog, Text,ttk, N,S,E,W
from tkinter.messagebox import askyesno
import os 
from random import randint, choice
import string
import sys
import file_operations as mf
from dialogue import Dialogue

# Globals
if sys.platform.startswith('win'):
    logo_path = 'logo\eliselogo.ico'
elif sys.platform.startswith('linux')
    logo_path = 'logo\eliselogo.xbm'

bg_color = "#424142"


# Start to code the GUI
class PWWatcher():
    
    def __init__(self):
        """
        Initialisation of the main window ( or root win)
        """
        # Creates the tk window, name it, set its geo and add the icone
        self.root_win = tk.Tk()
        self.root_win.title("PWWatcher")
        self.root_win.geometry("1080x720")
        self.root_win.minsize(480,360)
        self.root_win.iconbitmap(logo_path)

        # set the color -> can add option to change it ?
        self.root_win.config(background=bg_color)
        # if you want u can place a method quit 
        self.root_win.protocol("WM_DELETE_WINDOW",self.root_win.quit)
        # Creates menu bar 
        self.AddMenuBar()

        ## Add existing password stored (in the associated file) 
        ## in the main view 
        self.DisplayPasswords()
    ##############################  END INIT ######################    


    ############# Affichage principal des mots de pass  ################


    def DisplayPasswords(self):
        """
        Method which displays all the initially stored passwords
        in the main windows -> uses the method DisplayPassword
        """
        self.SBar = tk.Scrollbar(self.root_win)
        self.SBar.pack(side = tk.RIGHT, fill='y')
    
        # Frame on which to put the pws
        # self.frame_pw = tk.Frame(self.root_win,bg = bg_color,bd=1,relief = 'ridge')
        # self.frame_pw = tk.Canvas(self.root_win,bg = bg_color,yscrollcommand= self.SBar.set )
        # self.frame_pw.grid(row=0, column=0, sticky=N+S+E+W)
        # self.frame_pw.place(relwidth = 0.85,relheight =1,relx=0.135)
        # self.SBar.config(command=self.frame_pw.yview)
        # Load Existing passwords
        # passwords = mf.loading_pw()  
        passwords = [mf.Password(site='site1') , mf.Password(site='site2') ]
        mf.test_key("bonsoirEliot")
        for i , password in enumerate(passwords):
            self.DisplayPassword(password,i )
        
            
    def DisplayPassword(self,password,n):
        """
        Method to generate the common display for a password 
        with its site etc
        """
        onepwframe = tk.Frame(self.root_win,bg=bg_color,bd=1,relief = 'ridge')
        onepwframe.pack(fill=tk.BOTH)
        labelName = tk.Label(onepwframe,text = password.site,
                    bg=bg_color, fg ='white' )
        labelName.grid(row = n, column =1)
        buttonSite = tk.Button(onepwframe, text = 'link', bg = bg_color,
                            fg='white', bd=0 )
        buttonSite.grid(row=n,column=2)

        labelPw = tk.Label(onepwframe,text = password.password,
                            fg = 'white')
        labelPw.grid(row=n,column=3)

        
        
        

    ############################################################################

    def AddMenuBar(self):
            """
            Adds a menu bar with the menus u want
            """
            self.menu_bar = tk.Menu(self.root_win)
            self.menu_file = tk.Menu(self.menu_bar,tearoff=0)
            self.menu_file.add_command(label='New password', command =self.popPWEntry )
            self.menu_file.add_command(label='edit' ) #, command=edit_password)
            self.menu_file.add_command(label='delete') #, command=delete_password)
            self.menu_bar.add_cascade(label="File",menu = self.menu_file)
            # Adding the menu to the window
            self.root_win.config(menu=self.menu_bar)

    def popPWEntry(self):
        """
        pop the window where to add or gen a password which is a dialog
        window of the class Password_entry which itself herites from dialogue
        """
        d = Password_entry(self.root_win, title = "Add a new password",
                                offx= 150,offy=100) 
        
        return d.resultat

    def quit(self):
        # if askyesno("quitter l'application", "voulez vous quitter l'application?"):
        self.root_win.quit()


class Password_Display(tk.Listbox):
    def __init__(self):

        pass



class Password_entry(Dialogue) :

    def cover(self,cont):
        """
        Define the cover of the dialog window
        """
        # Defines the look of the dialog window
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

 

 

        




   # # # test onglets
        # self.notebook = ttk.Notebook(self.root_win)
        # self.notebook.pack(side ='bottom')
    
        # self.aff_pw = ttk.Frame(self.notebook)
        # self.add_pw = ttk.Frame(self.notebook)
        # self.aff_pw.pack()
        # self.add_pw.pack()

        # self.notebook.add(self.aff_pw,text='Main')
        # self.notebook.add(self.add_pw,text = 'Add password')
        # # #   


if __name__ == "__main__":
    # instanciation 
    app = PWWatcher()
    # affichage de la fenêtre principale
    app.root_win.mainloop()
    app.root_win.destroy()



# don't forget to make the exe with :
# pyinstaller --onefile pythonScriptName.py