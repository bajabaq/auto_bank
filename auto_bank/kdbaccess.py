import pyautogui
import pykeepass    

def get_kp(KDB):
    #catch exceptions
    kp = None
    while True:
        try:
            xtext = 'Enter KeePass password'
            xtitle= 'Get data from KeePassXC database'
            kpwd  = pyautogui.password(text=xtext,title=xtitle,default='',mask='*')
            #print('x',kpwd,'x')
            if kpwd == None:
                break
            #endif
            try:
                kp = pykeepass.PyKeePass(KDB, password=kpwd)
            except Exception as e:
                print(e)
                print('oops')
            #endtry
        except:
            continue
        else:
            break
        #endtry
    #endwhile
    return kp
#endef
    
def get_usr_pwd(kp, ret):
    print('getting usr/pwd from KeePassXC database')
    entry = kp.find_entries(title=ret,first=True)
    usr   = entry.username
    pwd   = entry.password
    return(usr, pwd)
#enddef

#------------------------------------------------------------------------------
if __name__ == '__main__':
    kdb = 'keepassXC database'
    kp  = get_kp(kdb)

    ret = 'record_entry_title'
    
    usr,pwd = get_usr_pwd(kp, ret)
#endif

