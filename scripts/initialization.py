import os 
import sys
import tkinter
from tkinter.filedialog import *

from Crypto.Hash import SHA256

from random import randint, choice
import string

# First of all, ask an admin password (key) to protect data
def Add_the_Admin_Key():
    print("""
    You need to enter an admin password.
    Warning: once added it cant be modified so choose it carrefully and write it somewhere.
    Do you understand ?
    Press Enter once understood and read those lines
        """)
    input()
    
    IsOk = 1

    while IsOk:
        print("Enter your Admin Password: ")
        admin_password = input()

        print('\nYour admin password is: ',admin_password ,'\n')
        print("""
        Just a reminder you wont be able to change it after and if you lose
        this password, all password saved with this programme will be lost
        (impossible to decrypt with this password)\n
        Do you confirm your Password ?(y/n):
                """)
        yon_entry = input()
        print('\n')

        if (yon_entry == 'y')|(yon_entry== 'Y')|(yon_entry=='yes'):
            break

    # Hash the admin_password with SHA256 algo
    hasher = SHA256.new( admin_password.encode('utf-8') )
    admin_hash = hasher.digest()
    print(admin_hash)
    print(type(admin_hash))
    # Now we need to save this Hash in a safe place
    print("""
        Now we will store this private info in a safe place.
        By default will be stored in a hidden folder in the dir where this app is installed.
        But if you want (and it is recommanded), you can save this info in a safer place in your computer.
        Do your want,to entrer your own folder ? (Y/n)
        """)
    yon_entry = input()
    print('\n')
    dirname = []
    # open tkinter dialogbox to select a folder
    if (yon_entry =='y')|(yon_entry =='Y')|(yon_entry=='yes'):
        while len(dirname) ==0 :
            root = tkinter.Tk()
            root.path = askdirectory(initialdir=os.getcwd(),title='Please select your personnal folder')
            dirname = root.path
            print(dirname)
            root.destroy()
            if len(dirname) == 0:
                print('You have not enter a directory, try again.\n')
    # directory is the current one
    else :
        print('Création par défaut. \n')
        dirname = os.getcwd()
    
    dirname = os.path.join(dirname,'.config' ) 
    os.mkdir( dirname )

    new_file = os.path.join(dirname,'config_file')
    select_line = randint(0,250)
    with open(new_file,'wb') as f:
        for lines in range(250):
            if lines == select_line:
                if select_line ==249:
                    f.write(admin_hash)
                    f.write(bytes(str(select_line),'utf-8') +'\n')
                else:
                    f.write(admin_hash)
                    f.write(b'\n')
                

            else:
                all_chars = string.ascii_letters + string.punctuation + string.digits
                password = "".join( choice(all_chars) for x in range(len(admin_password)) )
                hasher = SHA256.new( password.encode('utf-8') )
                hashrand = hasher.digest()
                if lines == 249:
                    f.write(hashrand)
                    f.write(bytes(str(select_line),'utf-8') +b'\n')   
                else:
                    f.write(hashrand)
                    f.write(b'\n')   
            
            

        
        
    print("END TEST")






if __name__ == "__main__":
    Add_the_Admin_Key()