import os
import urllib.request

def run(setpathfunc, osdir, username, curpath, args):
    if len(args) != 2:
        print("SIP - Super Installer Package")
    else:
        print("Attempting to update package " + args[1])
        canDownload = True
        if canDownload == True:
            try:
                os.remove(osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
                url = "https://raw.githubusercontent.com/Kiffolisk/pykern-sip/main/" + args[1] + ".py"
                print("Downloading to " + curpath + "/" + args[1] + ".py")
                urllib.request.urlretrieve(url, osdir + "/user/" + username + "/pkg/" + args[1] + ".py")
            except:
                print("Failed to update package!")
        else:
            print("Please move to /user/YOURUSERNAME/pkg.")
