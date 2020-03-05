import os 
import sys

# Tkinter imports
import tkinter as tk
from tkinter import filedialog, Text,ttk, N,S,E,W
from tkinter.messagebox import askyesno

#modules import
import file_operations as mf
from PopWindows import *


from Globals import *


# Start to code the GUI
class PWWatcher():
    
    def __init__(self):
        """
        Initialisation of the main window ( or root win)
        """
        # Creates the tk window, name it, set its geo and add the icone
        self.root_win = tk.Tk()
        self.root_win.title("PWWatcher")
        self.root_win.geometry("720x480")
        self.root_win.minsize(480,360)
        if sys.platform.startswith('win'):
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
    
        # Load Existing passwords
        # passwords = mf.loading_pw()  
        passwords = [mf.Password(site='site1',link = 'supide.com',username = 'Kev',password = 'password'),
                     mf.Password(site='site2',link = 'beauf.fr',username="Jonnhy", password = 'Jonnhy17'),
                     mf.Password(site='testsitewithoutlink', username='Testy', password="azerty"),
                     ]

        for i , password in enumerate(passwords):
            self.DisplayPassword(password,i )
        
            
    def DisplayPassword(self,password,n):
        """
        Method to generate the common display for a password 
        with its site etc
        """
        onepwframe = tk.Frame(self.root_win,bg=bg_color,bd=0.5,relief = 'ridge')
        onepwframe.pack(fill=tk.BOTH)

        labelName = tk.Label(onepwframe, text = password.site,
                    bg=bg_color, fg ='white' )
        labelName.configure(font = descFont)

        labelName.grid(row = n, column =1,ipadx =20, padx =2)

        labelUser = tk.Label(onepwframe, text = 'Username : '+password.username,
                            bg = bg_color, fg = 'white')
        labelUser.grid(row= n, column =2,ipadx=20)
        labelUser.configure(font = descFont)
    
        buttonSite = tk.Button(onepwframe, text = password.link, bg = bg_color,
                            fg='white', bd=0 )
        buttonSite.grid(row=n, column=3, ipadx=20)

        labelPw =   tk.Label(onepwframe, text = 'Password: ' +password.password, bg=bg_color,
                            fg = 'white')
        labelPw.grid(row=n, column=4, ipadx = 20)
        labelPw.configure(font = descFont)

        buttonCppw =tk.Button(onepwframe, text = 'Copy', bg=bg_color,
                                fg = 'white' )
        buttonCppw.grid(row = n,column = 5)

        
        

    ############################################################################

    def AddMenuBar(self):
            """
            Adds a menu bar with the menus u want
            """
            self.menu_bar = tk.Menu(self.root_win)
            self.menu_file = tk.Menu(self.menu_bar,tearoff=0)
            self.menu_file.add_command(label='New password', command =self.popPWEntry )
            self.menu_file.add_command(label='edit', command=self.popEdit)
            self.menu_file.add_command(label='delete', command=self.popDelete)
            self.menu_file.add_command(label='Settings', command = self.popSettings)
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

    def popSettings(self):
        """
        Pop the settings window where u can choose font, colors etc
        """
        # To be coded
        # Settings_win(self.root_win, title = "Settings", offx = 150, offy = 100)
        pass
    
    def popEdit(self):
        """
        pop the a window where u can select an existing password and modify it
        """
        pass

    def popDelete(self):
        """
        pop a window to delete passwords
        """
        pass


    def quit(self):
        # if askyesno("quitter l'application", "voulez vous quitter l'application?"):
        self.root_win.quit()




# class Password_Display(tk.Listbox):
#     def __init__(self):

#         pass

       
    #from tkinter import ttk

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