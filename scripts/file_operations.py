import pickle
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random



class Password:

    def __init__(self,site='',link='',password=''):
        self.site = site
        self.link = link
        self.password = password
        self._IV = Random.new().read(16)

    def __str__(self):
        return 'site :' + self.site +'\nlink :'+self.link + '\npassword :'+ self.password +'\n'


    def _encrypt_pw(self,key):
        """
        Encrypt the password using pycrypto module and the AES 
        encryption algorithm.
        For a good tutorial see DrapsTV on youtube in advanced python playlist
        """

        IV = self._IV
        encryptor = AES.new(key, AES.MODE_CBC,IV)
        ## the len of the string should be multiple of 16 for this algo
        if len(self.password)%16 !=0:
            self.password += b' ' *(16- (len(self.password)%16) )
        self.password = encryptor.encrypt(self.password)

    def _decrypt_pw(self,key,IV):
        """
        Decryption of the password with same algo
        """
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        self.password = decryptor.decrypt(self.password)



##############  functions for the Gui  #########################

def loading_pw(pathname='./',filename = 'mypw.pkl'):
    if os.path.isfile(os.path.join(pathname,filename) ):
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
        

# def getHashedKey(dir = os.getcwd()):
#     """
#     Get the hashed key choosen at the begining
#     """
#     dir  = os.path.join(dir,'.config')
#     with open(os.path.join(dir,'config_file.txt'),'w') as f:
#         a = f.read()
#     hashed_key = 'To be coded'
#     return hashed_key        



def test_key(entry):
    """
    Test if the admin password (used to encrypt and decrypt
    passwords) is the one chosen by admin at the begining
    """
    # Get all hash txt file containing the key
    dir = os.getcwd()
    dir  = os.path.join(dir,'.config')
    with open(os.path.join(dir,'config_file'),'rb') as f:
        a = f.read()

    # Now hash the entered key
    hasher = SHA256.new(entry.encode('utf-8'))
    entry_hash = hasher.digest()
    # print(entry_hash)
    

    if entry_hash in a :
        print('ok, it seems you have the admin pw')
        return entry_hash
    
    return []



if __name__ == "__main__":
    one_pw = Password('','','')
    print(one_pw)
    another_pw = Password('youtube','youtube.com','motdepasse')
    print(another_pw)
    last_pw = Password('mozilla',"mozilla.com",'renard')

    bankpw = [one_pw,another_pw,last_pw]
    print(bankpw[0])

    # test test_entry
    print(test_key("hello"))
    print(test_key("Fi122346914.Gg"))
