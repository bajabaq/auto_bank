from PIL import Image

import pyautogui
import webbrowser
import time

#------------------------------------------------------------------------------
def open_site(site):   
    print('Use pyautogui to get stuff from ',site)
    #move mouse to corner, so webbrowser opens top left (not 0,0 which is FailSafe loc)    
    pyautogui.moveTo(5,5)                    

    #open the website and login
    webbrowser.open_new(site)

    time.sleep(3)
#enddef


#------------------------------------------------------------------------------
def print_warning():
    msg = "!"*20+"\n"
    msg = msg + "!\tTHIS NAVIGATION IS FLAKY\n"
    msg = msg + "!"*20+"\n"
    print(msg)
#enddef

#------------------------------------------------------------------------------
def prompt_next(title,action):
    txt = 'To '+action+' click "OK"; otherwise click "Cancel"'
    res = pyautogui.confirm(text=txt, title=title)
    return res
#enddef

#------------------------------------------------------------------------------
def img_locate(numtry,img,left,top,width,height):
    found  = False
    for i in range(0,numtry):
        try:
            loc = pyautogui.locateOnScreen(img,region=(left,top,width,height))
            found = True
            break
        except pyautogui.ImageNotFoundException:
            print('Image not found, trying ',int(numtry-(i+1)),' more times')
    #endfor
    if found:
        print('Image found')
        return loc
    if not found:
        print('Something is wrong, image (', img ,') not found')
        return 'error'
    #endif
#enddef

#send in the image, find the "middle"
def img_middle(img2find):
    img = Image.open(img2find)
    iwidth,iheight = img.size   
    mwidth  = iwidth // 2     #integer division
    mheight = iheight // 2
    return mwidth, mheight
#endef
