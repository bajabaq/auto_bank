#------------------------------------------------------------------------------
#get data from HSA Bank
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd
from selenium.webdriver.common.keys import Keys

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):   

    e_usr   = selenium_aux.get_element_by_id(driver,"presence","idp-discovery-username")    #User ID
    e_usr.send_keys(USR)
    #can probably use XPATH to find //button[contains(.,"Continue") instead of navigating
    e_usr.send_keys(Keys.TAB+Keys.TAB+Keys.ENTER)
    
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","okta-signin-password")      #Password
    e_pwd.send_keys(PWD)
    #can probably use XPATH to find button[contains(.,"Sign In")
    e_pwd.send_keys(Keys.TAB+Keys.TAB+Keys.ENTER)

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
    site = "https://account.hsabank.com"
    actions("abc","123",site)
