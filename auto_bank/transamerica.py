#------------------------------------------------------------------------------
#get data from Transamerica SIP
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

from selenium.webdriver.common.keys import Keys

"""
#------------------------------------------------------------------------------
# A SUMMARY OF ACTIONS THAT MAY HAVE WORKED
#-----------
def actions(ssleft,sstop,sswidth,ssheight):
    action= "review Defined Benefit"
    if pyautogui_aux.prompt_next(title,action) == "OK":
        input("input the monthly benefit into Gnucash, then press [ENTER]")
    #else skip this action
    #endif

    action= "review Defined Contribution"
    if pyautogui_aux.prompt_next(title,action) == "OK":
        status = get_dc(ssleft,sstop,sswidth,ssheight)
        if status == 'error':
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('        Error             ')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!')            
        #endif
    #else skip this action
    #endif

    #you are inside the Defined Contribution page (Account Overview)
    action= "get Balance"
    if pyautogui_aux.prompt_next(title,action) == "OK":
        status = get_balance(ssleft,sstop,sswidth,ssheight)
        if status == 'error':
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('        Error             ')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!')            
        #endif
    #else skip this action
    #endif
    
    return    
#enddef


#------------------------------------------------------------------------------
def get_dc(ssleft,sstop,sswidth,ssheight):
    
    #wait for page to load
    img2find   = 'trans_defined_contrib.png'
    numtry     = 10    
    signin_loc = pyautogui_aux.img_locate(numtry,img2find,ssleft,sstop,sswidth,ssheight)    
    if signin_loc == 'error':
        return 'error'
    #endif

    bleft   = signin_loc.left
    btop    = signin_loc.top
    mwidth, mheight = pyautogui_aux.img_middle(img2find)
    pyautogui.click(bleft+mwidth, btop+int(mheight*2.25))
    time.sleep(1)    
    pyautogui.press('tab')
    time.sleep(1)

    #View Details is selected, press enter
    pyautogui.press('enter')
    
    return 'ok'
#enddef

#------------------------------------------------------------------------------
def get_balance(ssleft,sstop,sswidth,ssheight):
    
    #wait for page to load
    img2find   = 'tsa_myplan.png'
    numtry     = 10    
    signin_loc = pyautogui_aux.img_locate(numtry,img2find,ssleft,sstop,sswidth,ssheight)    
    if signin_loc == 'error':
        return 'error'
    #endif

    bleft   = signin_loc.left
    btop    = signin_loc.top
    mwidth, mheight = pyautogui_aux.img_middle(img2find)
    time.sleep(1)

    #navigate to Balance, press enter
    img2find   = 'tsa_balance.png'
    numtry     = 10    
    signin_loc = pyautogui_aux.img_locate(numtry,img2find,ssleft,sstop,sswidth,ssheight)    
    if signin_loc == 'error':
        return 'error'
    #endif

    bleft   = signin_loc.left
    btop    = signin_loc.top
    mwidth, mheight = pyautogui_aux.img_middle(img2find)
    pyautogui.click(bleft+mwidth, btop+mheight)
    
    #wait until it loads
    input('press [ENTER] to continue')
    
    return 'ok'
#enddef
"""

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):   
    e_usr   = selenium_aux.get_element_by_id(driver,"presence","userName")      #User ID
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","password")      #Password
    e_login = selenium_aux.get_element_by_id(driver,"presence","loginBtn")      #Password

    e_usr.send_keys(USR)
    e_pwd.send_keys(PWD)

    #can probably use XPATH to find button[contains(.,"Sign In")
    #e_pwd.send_keys(Keys.TAB+Keys.TAB+Keys.ENTER)  #login

    #going to try and click directly on the button    
    e_login.click()

    return driver
#enddef

#------------------------------------------------------------------------------
def actions(USR,PWD,site):
    driver = auto_bank_aux.enter_bank(sewd,site)

    driver = page_login_se(driver,USR,PWD)

    action = "review Defined Benefit"
    print(action)
    action = "review Defined Contribution"
    print(action)

    print("COME UPDATE THE CODE IN transamerica.py TO BE MORE USEFUL")

    action = "NO MORE ACTIONS DEFINED - YET"
    print(action)
    
    auto_bank_aux.exit_bank(driver)
    
    return
#enddef

#------------------------------------------------------------------------------
if __name__ == "__main__":
    site = "https://secure2.transamerica.com/login"
    actions("abc","123",site)

