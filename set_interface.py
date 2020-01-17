import tkinter as tk
from tkinter import filedialog, Text
import os 
from random import randint, choice
import string
# import file_operations as mf



bg_color = "#424142"

class PWWatcher():
    
    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.title("PWWatcher")
        self.root_window.geometry("1080x720")
        self.root_window.minsize(480,360)
        self.root_window.iconbitmap('eliselogo.ico')
        self.root_window.config(background=bg_color)

        # Creat menu bar 
        self.menu_bar = tk.Menu(self.root_window)
        self.menu_file = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_file.add_command(label='New password', command =self.open_pwwin )
        self.menu_file.add_command(label='edit' ) #, command=edit_password)
        self.menu_file.add_command(label='delete') #, command=delete_password)
        self.menu_bar.add_cascade(label="File",menu = self.menu_file)
        # Adding the menu to the window
        self.root_window.config(menu=self.menu_bar)

        # Loading the existing password if existing
        # passwords = mf.loading_pw()




        
    def open_pwwin(self):
        # configuration nouvelle fenêtre
        newwin = tk.Tk()
        newwin.title("Add a password ")
        newwin.geometry("360x240")
        newwin.minsize(72,48)
        newwin.maxsize(480,360)
        newwin.iconbitmap('eliselogo.ico')
        newwin.config(background=bg_color)

        #Add labels
        NameLabel = tk.Label(newwin, text = "Name : ",bg = bg_color,fg ='white')
        NameLabel.grid(row = 1,column =1,pady=5)
        SiteLabel = tk.Label(newwin, text = "url (opt) : ",bg = bg_color,fg ='white')
        SiteLabel.grid(row=2,column=1,pady =5)
        PwLabel = tk.Label(newwin,text = "Password : ", bg = bg_color,fg ='white')
        PwLabel.grid(row=3 , column=1,pady=5)
        # Add thir corresponding input
        NameEntry = tk.Entry(newwin)
        NameEntry.grid(row=1, column=2)
        SiteEntry = tk.Entry(newwin)
        SiteEntry.grid(row=2,column=2)
        PwEntry = tk.Entry(newwin)
        PwEntry.grid(row=3 , column=2)
        



        


    def generate_password(self,nb_char=10):
        all_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join( choice(all_chars) for x in range(nb_char) )
        return password
    
    

    



    


if __name__ == "__main__":
    # instanciation 
    app = PWWatcher()
    # affichage de la fenêtre principale
    app.root_window.mainloop()



# don't forget to make the exe with pyinstaller --onefile pythonScriptName.py