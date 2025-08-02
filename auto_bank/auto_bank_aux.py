#-------------------------------------------------------------------------------
#aux functions to consistently do something for each bank
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def enter_bank(sewd, site):
    print('Entering into: ',site)    
    driver = sewd.Firefox()
    driver.get(site)
    driver.set_window_position(5,10)  #just in and down from top left
    return driver
#enddef

#-------------------------------------------------------------------------------
def exit_bank(driver):
    ans = input("Done with site?  Press [ENTER] to continue")
    try:
        driver.quit()
    except Exception as e:
        print("oops Browser is probably already closed")
        print("Actual error is: ", e)
    #end try
#enddef

#-------------------------------------------------------------------------------
