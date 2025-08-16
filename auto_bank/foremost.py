#------------------------------------------------------------------------------
#get data from Foremost
#------------------------------------------------------------------------------
#import undetected_geckodriver as sewd
from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):   

    e_cookie = selenium_aux.get_element_by_id(driver,"clickable","onetrust-accept-btn-handler")
    e_cookie.click()
    
    #e_logintop = selenium_aux.get_element_by_link_text(driver,"clickable","Log In")
    e_logintop = selenium_aux.get_element_by_id(driver,"clickable","Log In")           #Log In TOP OF PAGE
    e_logintop.click()

    e_usr   = selenium_aux.get_element_by_id(driver,"presence","usernameInputField")  #User ID
    e_usr.send_keys(USR)
    e_usr.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)

    print("TODO - REST")
    print("copy and paste the PWD into the password field:")
    print(PWD)

    input("hit enter to continue")
    """    
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","dom-pswd-input")      #Password
    e_login = selenium_aux.get_element_by_id(driver,"clickable","dom-login-button")   #Log In
    

    e_pwd.send_keys(PWD)
    e_login.click()
    """
    
    return driver
#enddef

#------------------------------------------------------------------------------
def actions(USR,PWD,site):   
    driver = auto_bank_aux.enter_bank(sewd,site)

    print("TODO - not working yet...")
    #driver = page_login_se(driver,USR,PWD)

    #NO MORE ACTIONS DEFINED - YET

    auto_bank_aux.exit_bank(driver)
    
    return
#enddef

#------------------------------------------------------------------------------
if __name__ == "__main__":
    site  = "https://foremost.com"
    actions("abc","123",site)
