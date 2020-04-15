import sys
import ocarina_api

def getRepo():
    f = open(ocarina_api.getUserDir()+'/repo.txt','r')
    repo = f.read()
    f.close()
    return repo

try:
    if sys.argv[1] == 'get':
        print(ocarina_api.blue255+'Hang on a sec... getting app info...')
        ocarina_api.getAppInfoFromRepo(sys.argv[2],getRepo()) #Downloads the app-info file from the ocarina repository
        if ocarina_api.functionRanCorrectly != True:
            print(ocarina_api.red255+'Error (2): Could not find "'+sys.argv[2]+'" please make sure that this program actually exists and that you are typing the name correctly'+ocarina_api.endcolour)
            exit()
        print(ocarina_api.green255+'Info found!'+ocarina_api.endcolour)
        appData = ocarina_api.readDataFromInfoFile(sys.argv[2])
        if ocarina_api.functionRanCorrectly != True:
            print(ocarina_api.red255+'Error (3): There is a problem with the repository please contact the repo admin.'+ocarina_api.endcolour)
            exit()
        print(ocarina_api.green255+'Info extracted!'+ocarina_api.endcolour)
        if appData[1] == 'console-out':
            print(ocarina_api.blue255+appData[2]+ocarina_api.endcolour)
            exit()
        else:
            verify = input(ocarina_api.blue255+'Do you want to download '+appData[0]+'? (n/Y):'+ocarina_api.endcolour)
            appExtension = ocarina_api.getAppExecutable(sys.argv[2],appData[0],appData[2])
        print(ocarina_api.blue255+'Data downloaded for '+appData[0]+ocarina_api.endcolour)
        if appData[1] == 'app-ins':
            print(ocarina_api.blue255+'ocarina will now execute the setup file...'+ocarina_api.endcolour)
            ocarina_api.executeSetupFile(sys.argv[2],appExtension)
            verify = input(ocarina_api.blue255+'Do you want to delete the setup file? (n/Y): '+ocarina_api.endcolour)
            if verify.lower != 'n':
                ocarina_api.os.remove(ocarina_api.getUserDir()+'/appdata/'+sys.argv[2]+'/app.'+appExtension)
        elif appData[1] == 'prg-zip':
            print(ocarina_api.blue255+'Extracting...'+ocarina_api.endcolour)
            ocarina_api.unzipZippedFile(sys.argv[2])
            ocarina_api.executeExe(appData[3])

    elif sys.argv[1] == 'set-active-repo':
        if sys.argv[2] == 'official':
            repo = 'https://raw.githubusercontent.com/StonyVista/ocarina-official-repo/master'
        else:
            repo = sys.argv[2]
        f = open(ocarina_api.getUserDir()+'/repo.txt','w')
        f.write(repo)
        f.close()
    elif sys.argv[1] == 'launch':
        print(ocarina_api.blue255+'Launching...'+ocarina_api.endcolour)
        try:
            ocarina_api.executeExe(sys.argv[2],ocarina_api.readDataFromInfoFile(sys.argv[2])[3])
        except IndexError:
            print(ocarina_api.red255+'Error (4): Selected app is most likely nat an exe from a zip folder. Launch it from the start menu')
    else:
        print(ocarina_api.red255+'ocarina front end error: command: '+sys.argv[1]+'does not exist.'+ocarina_api.endcolour)
except IndexError:
    print(ocarina_api.red255+'ocarina front end error: How about typing a command next time??'+ocarina_api.endcolour)
    print('Commands:\nget: gets app with supplied name EG: ocarina get firefox\nset-active-repo sets the active repository EG: ocarina set-active-repo official (also works with repository urls)\nlaunch: Launches app from zipped folder (app must be downloaded with ocarina first) EG: ocarina launch <appnamehere.')