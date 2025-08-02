import os
import sys

from auto_bank import auto_bank

#------------------------------------------------------------------------------
if __name__ == '__main__':
    cwd   = os.getcwd()
    cdir  = os.path.join(cwd,"clients")
    error_msg = ""
    inifile   = ""
    if len(sys.argv) > 1:
        ifile = sys.argv[1]
        if ifile.endswith("ini"):
            inifile = os.path.join(cdir,ifile)
            if not os.path.exists(inifile):
                error_msg = "file not found"
            #endif
        else:
            error_msg = "argument must end in 'ini'"
        #endif 
    else:
        error_msg = "provide an 'ini' file name"
    #endif

    if len(error_msg) > 0:
        msg = "ERROR: " + error_msg + "\n\n"
        msg = msg + "usage: python auto_bank INIFILE \n"
        msg = msg + "INI files available are:\n"
        flist = ""
        for file in os.listdir(cdir):
            if file.endswith(".ini"):
                msg = msg + file + "\n"
            #endif
        #endfor
        msg = msg + "\n"
        print(msg)        
    else:
        auto_bank.main(inifile)           #DO THE WORK        
    #endif
#endef
