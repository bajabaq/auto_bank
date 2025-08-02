#------------------------------------------------------------------------------
#get data from Corebridge
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux


#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):      
    e_usr   = selenium_aux.get_element_by_id(driver,"presence","username")      #User ID
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","password")      #Password
    e_login = selenium_aux.get_element_by_id(driver,"clickable","btnSubmit")     #Login

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
    site  = "https://portal.annuities.corebridgefinancial.com/annuities/book-of-business/public/login#/"
    actions("abc","123",site)
