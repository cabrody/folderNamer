import os
import fnmatch
import shutil

folderCount = -1
numOfSubs = 0
nextOne = 0
int_list = []

for dirName, subdirList, fileList in os.walk("."):
	if dirName is '.':
		dirList = subdirList
		for sub in dirList:
			with open("list.txt", "a") as myfile:
				myfile.write(sub+'\r\n')
		with open("list.txt", "a") as myfile:
			myfile.write('\r\n')
		pass
	else:
		if dirName[2:] in dirList:
			folderCount += 1
			if(nextOne != 0):
				int_list.append(numOfSubs)
				numOfSubs = 0
			else:
				nextOne = 1;
		else:
			numOfSubs += 1
			try:
				new_file = os.path.join(dirList[folderCount] + "/", dirName.split('_')[6])
				shutil.move(dirName, new_file)
			except IndexError:
				pass	

int_list.append(numOfSubs)
for num in int_list:
	with open("list.txt", "a") as myfile:
		myfile.write(str(num))
		myfile.write("\r\n")
