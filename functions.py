import os
import sys
import pathlib
import tempfile
import os.path, time
import requests

def httpPost(source, ploads, target):
	r = requests.post(source, params=ploads)
	print("code: ",r.status_code)
	#print("headers: ",r.headers)
	print("Content-Type: ",r.headers['Content-Type'])	
	with open(target,'wb') as f:
		f.write(r.content)	
		
def httpGet(source, ploads, target):
	r = requests.get(source, params=ploads)
	print("code: ",r.status_code)
	#print("headers: ",r.headers)
	print("Content-Type: ",r.headers['Content-Type'])	
	with open(target,'wb') as f:
		f.write(r.content)		
	
def fileInfo(path):
	print("Filename: %s" % os.path.basename(path))
	print("Size: %s" % os.path.getsize(path))
	print("Last modified: %s" % time.ctime(os.path.getmtime(path)))
	print("Created: %s" % time.ctime(os.path.getctime(path)))

def createTempFolder():
	with tempfile.TemporaryDirectory() as directory:
		print('The created temporary directory is %s' % directory)
		
def createFolder(path):
	try:
		os.mkdir(path)
	except OSError:
		print ("Creation of the directory %s failed" % path)
	else:
		print ("Successfully created the directory %s " % path)

def deleteFolder(path):
	try:
		os.rmdir(path)
	except OSError:
		print ("Deletion of the directory %s failed" % path)
	else:
		print ("Successfully deleted the directory %s" % path)
		
def existFile(path):
	file = pathlib.Path(path)
	if ( file.is_file() ) :
		if file.exists() :
			return True	
	else : 
		print("This is not a file: " + path )
		return False		

def existFolder(path):
	file = pathlib.Path(path)
	if ( file.is_dir() ) :
		if file.exists() :
			return True	
	else :
		print("This is not a folder: " + path )
		return False
		
def copyFile(source, target):
	with open(target, 'w') as outfile:
		with open(source) as infile:
			for line in infile:
				outfile.write(line)
				
def replaceFileContent(source, target, old, new):
	with open(target, 'w') as outfile:
		with open(source) as infile:
			for line in infile:
				pos = line.find(old)
				if ( pos>0 ) :
					newline = line.replace(old, new)
					outfile.write(newline)
				else :
					outfile.write(line)					
			
def listFolders(path):
	folders = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for folder in d:			
			folders.append(os.path.join(r, folder))		
	return folders;
	
def listFiles(path):
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:			
			files.append(os.path.join(r, file))		
	return files;
	
def listFiles(path, pattern):
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:
			if pattern in file:
				files.append(os.path.join(r, file))		
	return files;


def main(): 
	
	source = sys.argv[1]
	param = sys.argv[2]
	target = sys.argv[3]
	#old = sys.argv[3]
	#new = sys.argv[4]
	
	#https://www.datacamp.com/community/tutorials/making-http-requests-in-python
	#httpPost(source, param, target)	
	#httpGet(source, param, target)
	
	#fileInfo(source)
	
	#createTempFolder()
	
	#createFolder(source)
		
	#deleteFolder(source)

	#if ( existFile(source) ) :
	#	print("File exist")
	#else :
	#	print("File not exist")
		
	#if ( existFolder(source) ) :
	#	print("Folder exist")
	#else :
	#	print("Folder not exist")
	
	#filename = shortFilename(source)
	#print("filename: '" + filename + "'")
	
	#replaceFileContent(source, target, old, new)
	
	#copyFile(source, target)
	#print("source:'" + source + "'")
	#print(f'source:\'{source.lstrip()}\'')
	#print("source:'",source.strip(),"'")
	#print("target:'",target.strip(),"'")
	
	#folders = listFolders("c:\\soft\\")
	#for d in folders:
	#	print(d)	
	
	#files = listFiles("c:\\soft\\")
	#files = listFiles("c:\\soft\\","codec")
	#for f in files:
	#	print(f)
		
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)
		sys.exit(1)








