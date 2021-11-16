import os
import urllib.request

def run(funcs, ivars):
    setpathfunc = funcs[0]
    args = ivars[3]
    curpath = ivars[2]
    osdir = ivars[0]
    username = ivars[1]
    if len(args) != 2:
        print("SIP - Super Installer Package")
    else:
        print("Attempting to install package " + args[1])
        canDownload = True
        if canDownload == True:
            try:
                url = "https://raw.githubusercontent.com/Kiffolisk/pykern-sip/main/" + args[1] + ".py"
                print("Downloading to " + curpath + "/" + args[1] + ".py")
                urllib.request.urlretrieve(url, osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
            except:
                print("Failed to install package!")
        else:
            print("Please move to /user/YOURUSERNAME/pkg.")
