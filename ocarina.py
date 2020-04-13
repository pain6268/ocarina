import colored as coloured
import sys
import ocarina_api

def getRepo():
    f = open(ocarina_api.getUserDir()+'/repo.txt','r')
    repo = f.read()
    f.close()
    return repo

try:
    if sys.argv[1] == 'get':
        ocarina_api.getAppInfoFromRepo(sys.argv[2],getRepo())
    elif sys.argv[1] == 'set-active-repo':
        if sys.argv[2] == 'official':
            sys.argv[2] = 'https://raw.githubusercontent.com/StonyVista/ocarina-official-repo/master'
        f = open(ocarina_api.getUserDir()+'/repo.txt','w')
        f.write(sys.argv[2])
        f.close()
    else:
        print(coloured.fg('#ff0000')+'ocarina front end error: command: '+sys.argv[1]+'does not exist.'+coloured.attr('reset'))
except IndexError:
    print(coloured.fg('#ff0000')+'ocarina front end error: How about typing a command next time??'+coloured.attr('reset'))
    print('Commands:\nget: gets app with supplied name EG: python ocarina.py get firefox\nset-active-repo sets the active repository EG: python ocarina.py set-active-repo official (also works with repository urls)')