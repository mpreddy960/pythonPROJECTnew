#chage current path  using : chdir()

import os

# Functio to Get the current
# working directory
def current_path():
	#print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
print("current working directory before")
current_path()
# Changing the CWD
os.chdir('../')

# Printing CWD after
print("current working directory after")
current_path()

#create a path using : mkdir()

import os

cwd = os.getcwd()
print("print cwd:",cwd)

#using : makedirs()

directory_new_path = "venkataravana"
bn = os.getcwd()
print("print now path :",bn)
d = bn+ "/reddy/lugs/klm/"
concatenate = os.path.join(d,directory_new_path)
print("print concatenate new path :",concatenate)

#os.makedirs(concatenate)
print("created new path  venkataravana :",directory_new_path)

## Python program to explain os.mkdir() method

# importing os module
# import os
#
# Directory
try:
	directory = "GeeksforGeeks34"
	parent_dir = os.getcwd()
	print("print getcwd:",parent_dir)

# Parent Directory path
#parent_dir = "D:/Pycharm projects/"

# Path
	path = os.path.join(parent_dir, directory)
	print("print path :",path)
	os.mkdir(path)
# print("Directory '% s' created" % directory)
	print("created directory:",directory)
except FileExistsError:
	pass


#mkdir(created new path
import os
try:
	directory = "reddymalapati"
	vc = os.getcwd()
	print(vc)
	n = os.path.join(vc,directory)
	print("print join vc path :",n)
	os.mkdir(n)
	print(print("created directory :",directory))
except FileExistsError:
	print("file already exist")
#second directory

# # Directory
# directory = "Geeks"
#
# # Parent Directory path
# parent_dir = "D:/Pycharm projects"
#
# # mode
# mode = 0o666
#
# # Path
# path = os.path.join(parent_dir, directory)
#
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# # with mode 0o666
# os.mkdir(path, mode)
# print("Directory '% s' created" % directory)

#using listdir
import os
cx = "/"
cv = os.listdir(cx)
print("print listdir  :",cx," :")
print("print cv  :",cv)
import os

# Get the list of all files and directories
# in the root directory
path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)

#using remove

file = "a.txt"
nm = os.getcwd()
print("file location :",nm)
xc = os.path.join(nm,file)
#os.remove(xc)

# exmple

# file = 'file1.txt'
# # File location
# location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
# # Path
# path = os.path.join(location, file)
# # Remove the file
# # 'file.txt'
# os.remove(path)