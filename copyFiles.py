# -*- coding: UTF-8 -*-
#----------------sort files when he was created-------------------
 
import os
import glob
import time
import shutil
 
d = raw_input('Select directory: ') # Set dir with only files
newd = raw_input('Select new dir: ') # Set new dir
if not os.path.exists(newd): # if new dir don't exist -> create
    os.makedirs(newd)
d = d + "*.jpg" # set type of file "*txt"
names = glob.glob(d)
print('----------------------PROCESSING--------------------\n ')
for name in names:
 
#-------------------work with file------------------
 
    dataCreate = os.stat(name).st_ctime # function os.stat().ctime return datecreate of file in seconds
	dataCreate = time.localtime(dataCreate) # transform seconds in good date
	year = str(dataCreate.tm_year)# from good date select year
	month = str(dataCreate.tm_mon)
	day = str(dataCreate.tm_mday)
	nameNewDir = year+'-'+month+'-'+day
	(dirname, filename)= os.path.split(name) # split on directory and gile name
	print('>>> '+name+' create on '+nameNewDir)
 
#----------------work with directory-------------
 
	alldf = os.listdir(newd) # list created directory
	if os.listdir(newd): 
		for oned in alldf:
			dtc = newd+oned 
			if os.path.isdir(dtc): # if is dir
				if oned == nameNewDir: # if dir exist
					shutil.copy2(name,dtc) # cope file
					print('    '+filename+' copeyd in '+dtc+'\n')
					break
				else:
					ndtc = newd+nameNewDir
					os.makedirs(ndtc) 
					shutil.copy2(name,ndtc) # copw file
					print('    '+filename+' copeyd in '+ndtc+'\n')
					break
	else: # if list don't exist 
		ndtc = newd+nameNewDir
		os.makedirs(ndtc)
		shutil.copy2(name,ndtc)
		print('    '+filename+' copeyd in '+ndtc+'\n')
