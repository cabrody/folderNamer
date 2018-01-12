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
		try:
			new_file = os.path.join(dirList[folderCount] + "/", dirName.split('_')[4])
			shutil.move(dirName, new_file)
			numOfSubs += 1
		except IndexError:
			folderCount += 1
			if nextOne == 0:
				nextOne = 1
				pass
			else:
				int_list.append(numOfSubs)
			numOfSubs = 0
			pass

int_list.append(numOfSubs)
for num in int_list:
	with open("list.txt", "a") as myfile:
		myfile.write(str(num))
		myfile.write("\r\n")
