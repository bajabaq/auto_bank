#------------------------------------------------------------------------------
#automatically do stuff at AmericanTraditions (INSURANCE)
#------------------------------------------------------------------------------
#import undetected_geckodriver as sewd
from selenium import webdriver as sewd

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import auto_bank_aux
import selenium_aux

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):
    
    e_usr   = selenium_aux.get_element_by_id(driver,"presence","txtPolicyNumber")  #Policy Number
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","txtPassword")      #Password
    e_login = selenium_aux.get_element_by_id(driver,"clickable","btnSubmit")       #Log In
    
    e_usr.send_keys(USR)
    e_pwd.send_keys(PWD)
    e_login.click()
    return driver
#enddef

#------------------------------------------------------------------------------
def actions(USR,PWD,site):
    driver = auto_bank_aux.enter_bank(sewd,site)
    
    driver = page_login_se(driver,USR,PWD)

    #NO MORE ACTIONS DEFINED - YET

    auto_bank_aux.exit_bank(driver)
    
    return
#enddef

#------------------------------------------------------------------------------
if __name__ == "__main__":
    site = "https://portal.jergermga.com/CustomerPortal/"
    actions("abc","123",site)
