import pickle
import os


class Password:

    def __init__(self,site='',link='',password=''):
        self.site = site
        self.link = link
        self.password = password

    def __str__(self):
        return 'site :' + self.site +'\nlink :'+self.link + '\npassword :'+ self.password +'\n'

    

##############  functions for the Gui  #########################

def loading_pw():
    if os.path.isfile('mypw.pkl'):
        with open('mypw.pkl','rb') as f:
            pw_list = pickle.load(f)
        return pw_list
    else:
        return []


def add_pw(pw_list,password):
    pw_list.append(password)     
    return pw_list

def save_pw(pw_list):
    with open('mypw.pkl','wb') as f:
        pickle.dump(pw_list,f,pickle.HIGHEST_PROTOCOL)
        





if __name__ == "__main__":
    one_pw = Password('','','')
    print(one_pw)
    another_pw = Password('youtube','youtube.com','motdepasse')
    print(another_pw)
    last_pw = Password('mozilla',"mozilla.com",'renard')

    bankpw = [one_pw,another_pw,last_pw]
    print(bankpw[0])
