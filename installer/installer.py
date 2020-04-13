import os
print('Installing ocarina')
os.system('mkdir %userprofile%/ocarina-data')
os.system('copy ocarina.py %userprofile%/ocarina-data/ocarina.py')
os.system('copy ocarina_api.py %userprofile%/ocarina-data/ocarina_api.py')
os.system('copy repo.txt %userprofile%/ocarina-data/repo.txt')
os.system('copy ocarina.bat %windir%/system32/ocarina.bat')
os.system('pip install colored')
print('DONE!!!')
