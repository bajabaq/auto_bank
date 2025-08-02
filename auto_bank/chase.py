#------------------------------------------------------------------------------
#get data from Chase
#------------------------------------------------------------------------------
import undetected_geckodriver as sewd
#from selenium import webdriver as sewd

import sys
import os

from . import auto_bank_aux
from . import selenium_aux

"""
#------------------------------------------------------------------------------
def page_get_qfx(ssleft,sstop,sswidth,ssheight):
    #get date range (ask user for start "MM/DD/YYYY" and end "MM/DD/YYYY")
    d_start = pyautogui.prompt(text='start date (MM/DD/YYYY)', title='Activity range', default='')
    d_end   = pyautogui.prompt(text='end date (MM/DD/YYYY)', title='Activity range', default='')
    #d_start = '10/01/2024'
    #d_end   = '10/26/2024'
    
    #click on more
    loc_more = pyautogui_aux.img_locate(10,'chase_more.png',ssleft,sstop,sswidth,ssheight)
    pyautogui.click(loc_more.left+15, loc_more.top+15)
    time.sleep(1)
    
    #click on "Spending summary" (or move with keyboard)
    pyautogui.press('down',presses=3)
    pyautogui.press('enter')

    print('find Download Transactions')
    #click on "Download transactions"
    loc_download_t = pyautogui_aux.img_locate(10,'chase_download_transactions.png',ssleft,sstop,sswidth,ssheight)    
    pyautogui.click(loc_download_t.left+15, loc_download_t.top+15)
    time.sleep(1)

    #select account, file type, activity, then download    
    #move to "account", move right, click, move down, click
    print('find Account')
    loc_account = pyautogui_aux.img_locate(10,'chase_account_choose.png',ssleft,sstop,sswidth,ssheight)
    print(loc_account)
    bleft   = loc_account.left
    btop    = loc_account.top
    bwidth  = loc_account.width
    bheight = loc_account.height
    #print(bleft,btop,bwidth,bheight)
    pyautogui.click(loc_account.left+int(bwidth/2), loc_account.top+int(bheight/2))
    pyautogui.click(loc_account.left+int(bwidth/2), loc_account.top+bheight)       
    time.sleep(1)
    
    #move to "file type", move right, click, arrow down, hit enter
    print('find File Type')
    loc_file_t = pyautogui_aux.img_locate(10,'chase_file_type.png',ssleft,sstop,sswidth,ssheight)    
    print(loc_file_t)
    #use same height info from account location
    pyautogui.click(loc_file_t.left+int(bwidth/2), loc_file_t.top+int(bheight/2))
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

    #Move to activity: tab, enter, move arrow down 7 times (to move to "choose date range"), enter
    print('find Activity')    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('up') #reverse list naviagation (starts at bottom) #down',presses=7)
    pyautogui.press('enter')
    pyautogui.press(['tab','tab'])

    pyautogui.write(d_start)
    pyautogui.press('esc')
    pyautogui.press(['tab','tab'])
    pyautogui.write(d_end)
    pyautogui.press('esc')

    #Download the file
    print('Download file....sometimes does not work - manually either...b/c have to clear cookies from website')
    pyautogui.press(['tab','tab','tab'])
    pyautogui.press('enter')

    return('ok')
#enddef
"""

#------------------------------------------------------------------------------
#use selenium to login
def page_login_se(driver,USR,PWD):       
    e_usr   = selenium_aux.get_element_by_id(driver,"presence","userId-input")  #User ID
    e_pwd   = selenium_aux.get_element_by_id(driver,"presence","password")      #Password
    e_login = selenium_aux.get_element_by_id(driver,"clickable","signin-button")#LogIn
    e_usr.send_keys(USR)
    e_pwd.send_keys(PWD)
    e_login.click()

    return driver
#enddef

#------------------------------------------------------------------------------
def actions(USR,PWD,site):
    driver = auto_bank_aux.enter_bank(sewd,site)

    print("PAGE BROKE")
    #driver = page_login_se(driver,USR,PWD)

    #NO MORE ACTIONS DEFINED - YET
    #GET QFX - TODO

    auto_bank_aux.exit_bank(driver)
    
    return
#enddef

#------------------------------------------------------------------------------
if __name__ == "__main__":
    site = "https://chase.com"
    actions("abc","123",site)

