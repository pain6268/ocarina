import os
print('Installing ocarina')
os.system('mkdir %userprofile%/ocarina')
os.system('copy ocarina.py %userprofile%/ocarina-data')
os.system('copy ocarina_api.py %userprofile%/ocarina-data')
os.system('copy repo.txt %userprofile%/ocarina-data')
os.system('pip install colored')
print('DONE!!!')
