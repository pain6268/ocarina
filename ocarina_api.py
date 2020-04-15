#ocarina-api by SVista
import os
import colored as coloured
import urllib.request
import sys
import zipfile

global verifiedSystem
global functionRanCorrectly
verifiedSystem = False

endcolour = coloured.attr('reset') #resets string colour. Example below --------------------------------V
red255 = coloured.fg('#ff0000') #red255 before a string in a print makes the rext #ff0000 (255 red) EG: print(red255+'insert text here'+endcolour)
blue255 = coloured.fg('#3969fa') #ditto but for 255 blue
green255 = coloured.fg('#39b336') #ditto but for 255 green

def baseSystemCheck(): #Checks if ocarina is running on Windows or not
    if os.name != 'nt':
        print(red255+'Error (1): ocarina has detected you are not running Windows.\nIf you are wanting to test ocarina, please use Windows.'+endcolour) #Stops non-windows systems from working
    else:
        global verifiedSystem
        verifiedSystem = True

baseSystemCheck() #other functions won't run on any other OS from here

def dlFile(remoteAddress, localAddress):
    if verifiedSystem == True:
        try:
            urllib.request.urlretrieve(remoteAddress, localAddress) #downloads file from remoteAddress (location on web) to localAddress (location on this computer) eg: remote: https://svista.ddns.net/ocarina.py local: C:/Users/Administrator/ocarina.py
            return True #Download success
        except urllib.error.HTTPError:
            return False #Download fail
    else:
        print(red255+'Error (1): ocarina has detected you are not running Windows.\nIf you are wanting to test ocarina, please use Windows.'+endcolour)

def getUserDir():
    baseUserDir = sys.executable.split('\\')[0]+'/Users/'+os.getlogin()
    if os.path.exists(baseUserDir+'/ocarina-data') == False: #/ocarina-data rather than just /ocarina because otherwise it would be likely to conflict with the git repo if it was in the users home folder
        os.mkdir(baseUserDir+'/ocarina-data') #creates C:/Users/*your-user-here*/ocarina-data
    return baseUserDir+'/ocarina-data'

def genFolder(path):
    if os.path.exists(getUserDir()+'/'+path) == False:
        os.mkdir(getUserDir()+'/'+path)
    return path

def getAppExecutable(basename, name, url):
    global functionRanCorrectly
    appDLLocation = getUserDir()+'/'+genFolder('appdata/'+basename)+'/app.'+url.split('.')[-1]
    functionRanCorrectly = dlFile(url,appDLLocation)
    return url.split('.')[-1]

def executeSetupFile(appName,extension):
    os.system(getUserDir()+'/appdata/'+appName+'/app.'+extension)

def executeExe(appName,exeLocation):
    os.system(getUserDir()+'/appdata/'+appName+'/'+exeLocation)

def unzipZippedFile(appName):
    archive = zipfile.ZipFile(getUserDir()+'/appdata/'+appName+'/app.zip')
    archive.extractall()
    archive.close()

def getAppInfoFromRepo(appName,repository):
    global functionRanCorrectly
    appDLLocation = getUserDir()+'/'+genFolder('appdata/'+appName)+'/app.ocarina-info'
    functionRanCorrectly = dlFile(repository+'/apps/'+appName+'/app.ocarina-info',appDLLocation) #this line downloads the app info file for the selected app on the active repository

def readDataFromInfoFile(appName): 
    global functionRanCorrectly
    f = open(getUserDir()+'/appdata/'+appName+'/app.ocarina-info','r')
    appData = f.readlines()
    f.close()
    for line in range(0,len(appData)):
                appData[line] = appData[line].rstrip().split('*') #splits the data into a list containing each line broken down into a list where the colon seperated them
    exeInZip = 'none'
    for entry in appData:
        if entry[0] == 'name':
            appFullName = entry[1]
        elif entry[0] == 'type':
            dlType = entry[1]
        elif entry[0] == 'url': #URL shouldn't be used in info files anymore... kept here for backwards compatibility
            dlData = entry[1]
        elif entry[0] == 'data':
            dlData = entry[1]
        elif entry[0] == 'zip-exe':
            exeInZip = entry[1]
        else:
            functionRanCorrectly = False
    return [appFullName, dlType, dlData, exeInZip]

print(green255+'Thanks for using ocarina!! (alpha 1.1 progress version)'+endcolour)
genFolder('appdata')