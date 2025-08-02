#------------------------------------------------------------------------------
#get data from Discover Bank
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import auto_bank_aux
import selenium_aux

from selenium.webdriver import Keys, ActionChains

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):   
    e_login = selenium_aux.get_element_by_xpath(driver,'clickable','//button[text()="Log In"]')
    e_login.click()
    
    e_usr   = selenium_aux.get_element_by_id(driver,'presence',"userid")    #User ID
    e_pwd   = selenium_aux.get_element_by_id(driver,'presence',"password")  #Password        
    e_usr.send_keys(USR)
    e_pwd.send_keys(PWD)
    
    ActionChains(driver)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .perform()
    ActionChains(driver)\
        .send_keys(Keys.ENTER)\
        .perform()

    return driver
#enddef

#------------------------------------------------------------------------------
def actions(USR,PWD,site):
    driver = auto_bank_aux.enter_bank(sewd,site)

    print("PAGE IS BROKE")    
    #driver = page_login_se(driver,USR,PWD)

    #NO MORE ACTIONS DEFINED - YET

    auto_bank_aux.exit_bank(driver)
    
    return
#enddef

if __name__ == "__main__":
    actions("abc","123","https://discover.com")
