#------------------------------------------------------------------------------
#get data from Sunpass
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
    
    e_usr = selenium_aux.get_element_by_id(driver,"presence","tt_username1")
    e_pwd = selenium_aux.get_element_by_id(driver,"presence","tt_loginPassword1")
    e_usr.send_keys(USR)
    e_pwd.send_keys(PWD)

    #navigate to the LOGIN button  maybe can find by name
    #XPATH = /html/body/div[3]/div[2]/div/div/div/div/form/button

    e_pwd.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)

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
    site = "https://www.sunpass.com/vector/account/home/accountLogin.do"
    actions("abc","123",site)
