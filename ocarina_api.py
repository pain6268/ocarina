#ocarina-api by SVista
import os
import colored as coloured
import urllib.request
import sys

global verifiedSystem
verifiedSystem = False

endcolour = coloured.attr('reset') #resets string colour. Example below --------------------------------V
red255 = coloured.fg('#ff0000') #red255 before a string in a print makes the rext #ff0000 (255 red) EG: print(red255+'insert text here'+endcolour)
blue255 = coloured.fg('#0000ff') #ditto but for 255 blue
green255 = coloured.fg('#00ff00') #ditto but for 255 green

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
            return 1 #Download success
        except urllib.error.HTTPError:
            return 0 #Download fail
    else:
        print(red255+'Error (1): ocarina has detected you are not running Windows.\nIf you are wanting to test ocarina, please use Windows.'+endcolour)

def getUserDir(removeDataString = False):
    baseUserDir = sys.executable.split('\\')[0]+'/Users/'+os.getlogin()
    if os.path.exists(baseUserDir+'/ocarina-data') == False: #/ocarina-data rather than just /ocarina because otherwise it would be likely to conflict with the git repo if it was in the users home folder
        os.mkdir(baseUserDir+'/ocarina-data') #creates C:/Users/*your-user-here*/ocarina-data
    if removeDataString == True:
        return baseUserDir
    else:
        return baseUserDir+'/ocarina-data'

def genFolder(path):
    if os.path.exists(getUserDir()+'/'+path) == False:
        os.mkdir(getUserDir()+'/'+path)
    return path

def getAppExecutable(basename, name, type, url): #type is unused for now
    if verifiedSystem == True:
        verify = input(blue255+'Would you like to download '+name+'? (n/Y): '+endcolour)
        if verify.lower() != 'n':
            appDLLocation = getUserDir()+'/'+genFolder(basename)+'/app.'+url.split('.')[-1]
            print(blue255+'Now downloading '+name+' from its defined source ('+url+')...'+endcolour)
            dlStatus = dlFile(url,appDLLocation)
            if dlStatus == 1:
                print(green255+'Data downloaded successfully...'+endcolour)
                print(blue255+'ocarina will now execute the setup file...')
                os.system(appDLLocation)
                verify = input(blue255+'Do you want to delete the setup files? (n/Y): '+endcolour)
                if verify.lower() != 'n':
                    os.remove(appDLLocation)
                    print(green255+'Done!'+endcolour)  
            else:
                print(red255+'Error (4): Could not find the files at the defined source'+endcolour)
                p
    else:
        print(red255+'Error (1): ocarina has detected you are not running Windows.\nIf you are wanting to test ocarina, please use Windows.'+endcolour)

def getAppInfoFromRepo(appName,repository):
    if verifiedSystem == True:
        appDLLocation = getUserDir()+'/'+genFolder(appName)+'/app.ocarina-info'
        print(blue255+'Getting info for '+appName+' from the repository...'+endcolour)
        dlStatus = dlFile(repository+'/apps/'+appName+'/app.ocarina-info',appDLLocation) #this line downloads the app info file for the selected app on the active repository
        if dlStatus == 1:
            print(green255+'Info successfully downloaded from the repository!'+endcolour)
            print(blue255+'Decoding info file...'+endcolour)
            f = open(appDLLocation,'r') #opening data file
            appData = f.readlines() # reading data file to var
            f.close() #closing data file
            for line in range(0,3): #formatting file into somrthing readable by the program
                appData[line] = appData[line].rstrip().split('*') #splits the data into a list containing each line broken down into a list where the colon seperated them
            dlFileProblematic = False
            for entry in appData:
                if entry[0] == 'name':
                    appFullName = entry[1]
                elif entry[0] == 'type':
                    dlType = entry[1]
                elif entry[0] == 'url':
                    dlUrl = entry[1]
                else:
                    print(red255+'Error (3): There is something wrong with the repository, it might be broken or be designed for a newer version of ocarina. Please check your version or contact the Repository Admin.'+endcolour)
                    print(appData)
                    if repository != 'https://raw.githubusercontent.com/StonyVista/ocarina-official-repo/master':
                        print(red255+'Note: you are not using the official repository. Therefore the anly support that can be given is to contact the Repository Admin since this cannot be an issue with ocarina itself.'+endcolour)
                    else:
                        print(red255+'If you believe this is an issue with the official repository, please post an issue here: https://github.com/StonyVista/ocarina-official-repo/issues'+endcolour)
                    dlFileProblematic = True #Raises to the program that there's a problem with the info file
            if dlFileProblematic == False:
                print(green255+'Yay! The info file was successfully decoded! ocarina is now able to download the data for '+appFullName+'.')
                getAppExecutable(appName,appFullName, dlType, dlUrl)  
        else:
            print(red255+'Error (2): Could not find data for "'+appName+'" on the repository. Please make sure the name is typed correctly and that the program you are trying to get is ACTUALLY on the repository.'+endcolour)
            if repository != 'https://raw.githubusercontent.com/StonyVista/ocarina-official-repo/master':
                print(red255+'Furthermore, it has been detected that you are not using the official ocarina repository. Please make sure that the repository you are using is configured correctly. If not, contact the Repository Admin.\n(Note: you will not be able to recive support for unnofficial repositories as SVista has no control over them.)'+endcolour)
            else:
                print('If you believe this is an issue with the official repository, please post an issue here: https://github.com/StonyVista/ocarina-official-repo/issues')
    else:
        print(red255+'Error (1): ocarina has detected you are not running Windows.\nIf you are wanting to test ocarina, please use Windows.'+endcolour)

print(green255+'Thanks for using ocarina!!'+endcolour)