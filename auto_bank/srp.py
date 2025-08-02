#------------------------------------------------------------------------------
#get data from SRP FCU
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

from selenium.webdriver.common.keys import Keys

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):
    e_usr = selenium_aux.get_element_by_name(driver,"presence","UserName")       #User ID
    e_usr.send_keys(USR)
    
    e_pwd = selenium_aux.get_element_by_name(driver,"presence","Password")      #Password
    e_pwd.send_keys(PWD)

    e_pwd.send_keys(Keys.TAB+Keys.ENTER)

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
    site = "https://srpfcu.org"
    actions("abc","123",site)
