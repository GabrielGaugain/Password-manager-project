from setuptools import setup
from scripts import initialization
import os

### Initiates the admin password 
if not os.path.isfile(".config/config_file"):
    initialization.Add_the_Admin_Key()

# List of scripts to add to make the package
# list_scripts = [ f for f in os.listdir('scripts/') if os.path.isfile(os.path.join('scripts/',f)) ]
list_scripts = [ "set_interface.py","dialogue.py","file_operations.py"]
scripts = [os.path.join('scripts/',scriptname) for scriptname in list_scripts]

setup(
    name = "PWWatcher",
    version = '0.1',
    scripts = scripts,
    author = 'Gaugain G.',
    author_email = 'gabriel.ggain@gmail.com',
    description = "Just a little prog to generate en manage passwords",
    keywords = "Password Manager",
    install_requires = ["PyCrypto >= 0.1"],

)