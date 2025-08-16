#------------------------------------------------------------------------------
#Auxillary functions for selenium
#------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

#------------------------------------------------------------------------------
#explicitly wait on each element to be found (need to put a try/catch here)
def get_element_by_id(driver,ec_type,element_id):
    wtime   = 10 #sec
    element = ""
    if ec_type == 'presence':
        element = WebDriverWait(driver,wtime).until(EC.presence_of_element_located((By.ID,element_id)))
    elif ec_type == 'clickable':
        element = WebDriverWait(driver,wtime).until(EC.element_to_be_clickable((By.ID,element_id)))
    else:
        print("error in selenium_aux.py get_element_by_id")
    #endif
    return element
#enddef

def get_element_by_name(driver,ec_type,e_name):
    wtime   = 10 #sec
    element = ""
    if ec_type == 'presence':
        element = WebDriverWait(driver,wtime).until(EC.presence_of_element_located((By.NAME,e_name)))
    elif ec_type == 'clickable':
        element = WebDriverWait(driver,wtime).until(EC.element_to_be_clickable((By.NAME,e_name)))
    else:
        print("error in selenium_aux.py get_element_by_name")
    #endif
    return element
#enddef

def get_element_by_xpath(driver,ec_type,xpath):
    wtime   = 10 #sec
    element = ""
    if ec_type == 'clickable':
        WebDriverWait(driver,wtime).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    else:
        print("error in selenium_aux.py get_element_by_xpath")
    #endif
    return element
#enddef

def get_element_by_link_text(driver,ec_type,ltxt):
    wtime = 10 #sec
    element = ""
    if ec_type == 'clickable':
        element = WebDriverWait(driver,wtime).until(EC.element_to_be_clickable((By.LINK_TEXT,ltxt)))
    else:
        print("error in selenium_aux.py get_element_by_link_text")
    #endif
    return element
#enddef
