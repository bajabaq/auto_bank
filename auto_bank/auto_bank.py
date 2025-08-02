#------------------------------------------------------------------------------
#open a variety of financial firm websites and do something useful
#------------------------------------------------------------------------------
import configparser
import importlib
import os
import pathlib
import sys

from . import kdbaccess

#------------------------------------------------------------------------------
#remove '"' from around values
class MyConfigParser(configparser.ConfigParser):
    def get(self, section, option, *args, **kwargs):
        value = super().get(section, option, *args, **kwargs)
        return value.strip('"')

#------------------------------------------------------------------------------
def main(inifile):
    #do some basic setup before the real work
    config = MyConfigParser()
    
    #read the inifile
    config.read(inifile)

    kdb_str = config.get('keepass','kdb')
    kdb     = pathlib.Path(kdb_str)
    if not kdb.exists():
        print('file not found',kdb)
        return
    #endif

    print('Getting KeePass db')
    kp  = kdbaccess.get_kp(kdb)
    if kp == None:
        print('Canceled getting KeePass db')
        return
    #endif
    
    #get the fintech accounts
    sections = config.sections()
    sections.remove('keepass') #the fintech sections are all that's left
        
    #loop over each fintech account and do something interesting
    for fintech in sections:
        fmod = config.get(fintech,'module')
        name = config.get(fintech,'name')
        site = config.get(fintech,'site')
        ret  = config.get(fintech,'ret')
                
        print('-'*20)
        print(name)            
        ans = input("Press [ENTER] or 's' to skip or 'q' to quit: ")
        if ans.lower() == 's':
            continue #do next fintech
        elif ans.lower() == 'q':
            break #get out of for loop
        #endif
            
        #get usr/pwd from keypassdb row entry title
        usr,pwd = kdbaccess.get_usr_pwd(kp, ret)            

        #----------------------------------------------------------------
        #navigate and login per fintech site and do something interesting
        #----------------------------------------------------------------
        #load the fintech module
        fintech_mod = importlib.import_module('auto_bank'+'.'+fmod)
        #print(fintech_mod.__name__)

        #look for the 'actions' function in the 'FINTECH file, eg 'chase.py' file in the 'chase' subdirectory
        status = fintech_mod.actions(usr,pwd,site)
        if status == 'error':
            print('Error - what do we do now')
            break
        #endif       
        os.chdir('../')
    #endfor looping over fintech accounts
#enddef

