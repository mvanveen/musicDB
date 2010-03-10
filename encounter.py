# Encounter.py
# ==============================================================================
# Michael Van Veen
# 03/08/10
# ==============================================================================
# Checks to see if a file exists in DB.
# ==============================================================================
import sys
import os

import json
import hashlib 

encounterDir	= os.environ['HOME'] + "/.encounter"
encounterFile = "duplicateHashes"

class Encounter():
	def __init__(self):
		# Path to duplicate hash file, determined via global vars above
		self.__filePath 				= "" if (encounterDir[-1] == "/") else "/"
		self.__filePath					= self.__filePath.join((encounterDir,
																										encounterFile))
		self.__duplicateHashes 	= self.__loadHashes()
		
		if (self.__duplicateHashes == {}):
			self.__writeHashes()

	def check(self, fileName):
		return(self.__checkEntity(fileName))

	def __writeHashes(self):
		fileObj = open(self.__filePath, "w")
		fileObj.write(json.dumps(self.__duplicateHashes))
		fileObj.close()
	
	def __loadHashes(self):
		if(not (os.access(encounterDir, os.F_OK))):
			os.mkdir(encounterDir)
			print("Created directory " + encounterDir)

		if(not (os.access(self.__filePath, os.F_OK))):
			print("Created hash dictionary " + self.__filePath)
			return({})

		return(json.loads(open(self.__filePath).read()))

	def __checkEntity(self, fileName):
		if (not os.access(fileName, os.F_OK)):
			print("Error: No such file found")
			return(False)

		hashObj 	= hashlib.sha1()
		hashObj.update(open(fileName).read())
		fileHash 	= hashObj.hexdigest()

		# See if the file has been encountered
		if (self.__duplicateHashes.has_key(fileHash)):
			return(True)

		# File has not been encountered.  Add it to dictionary.
		self.__duplicateHashes[fileHash] = True
		return(False)

	def close(self):
		self.__writeHashes()

if (__name__ == "__main__"):
	encounter = Encounter()
	if (encounter.check(sys.argv[1])):
		print("File has already been encountered")
		sys.exit()
	print("Adding file....")
	encounter.close()
