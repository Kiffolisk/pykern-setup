import os
import urllib.request

def run(osdir, username, curpath, args):
    print("Attempting to uninstall package " + args[1])
    try:
        os.remove(osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
    except:
        print("Failed to uninstall package or package not installed in the first place.")
