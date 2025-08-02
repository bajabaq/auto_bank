#------------------------------------------------------------------------------
#get data from Paypal
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

import time

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):

    e_login_top = selenium_aux.get_element_by_id(driver,"clickable","_ul-btn_18pa1_1")  #Log In Top
    e_login_top.click()
    
    e_usr   = selenium_aux.get_element_by_id(driver,"presence","email")        #email/mobile
    e_usr.send_keys(USR)

    e_usr_next = selenium_aux.get_element_by_id(driver,"clickable","btnNext")  #Next button
    e_usr_next.click()

    time.sleep(3)
    
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","password") #Password
    e_pwd.send_keys(PWD)

    e_login = selenium_aux.get_element_by_id(driver,"presence","btnLogin") #Log In
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
    site = "https://paypal.com"
    actions("abc","123",site)
