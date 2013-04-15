# -*- coding: UTF-8 -*-
#----------------sort files when he was created-------------------

import os
import time
import shutil

d = raw_input('Select directory: ') # Set dir with only files
newd = raw_input('Select new dir: ') # Set new dir
ext = raw_input('Select extension: ')

#-------------------work with file------------------

print ('\n-----------------------[PROCESSING]----------------\n')
for root, dirs, files in os.walk(d):
	for name in files:
		fullname = os.path.join(root, name)
		(dirname, filename) = os.path.split(fullname)
		(shortname, extension) = os.path.splitext(filename)
		if extension == ext: #set extension
			dataCreate = os.stat(fullname).st_ctime # function os.stat().ctime return datecreate of file in seconds
			dataCreate = time.localtime(dataCreate) # transform seconds in good date
			year = str(dataCreate.tm_year)# from good date select year
			month = str(dataCreate.tm_mon)
			day = str(dataCreate.tm_mday)
			nameNewDir = year+'-'+month+'-'+day
			print('>>> '+fullname+' created on '+nameNewDir)

#----------------work with directory-------------

			ndc = newd+nameNewDir
			if os.path.exists(ndc):
				shutil.copy2(fullname,ndc) # copy file
				print('    '+name+' copy in '+ndc+'\n')
			else:
				os.makedirs(ndc)
				shutil.copy2(fullname,ndc) # copy file
				print('    '+name+' copy in '+ndc+'\n')
