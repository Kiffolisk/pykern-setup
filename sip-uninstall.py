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
        print("Attempting to uninstall package " + args[1])
        try:
            os.remove(osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
        except:
            print("Failed to uninstall package or package not installed in the first place.")
