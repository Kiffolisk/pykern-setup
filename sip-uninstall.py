import os
import urllib.request

def run(setpathfunc, osdir, username, curpath, args):
    if len(args) != 2:
        print("SIP - Super Installer Package")
    else:
        print("Attempting to uninstall package " + args[1])
        try:
            os.remove(osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
        except:
            print("Failed to uninstall package or package not installed in the first place.")
