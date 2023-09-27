# The OS module allows us to interact with underlying operating system in several different ways.
# For example, we can navigate the file system, get file info, look up and change the environement variables, move files around, ect.
import os
# print out all of the methods avaiable.
#print(dir(os))

# print out current dir
print(os.getcwd())

# What if you wanted to navigate?
os.chdir('/Users')
print(os.getcwd())

os.chdir('/Users\ddodds\OneDrive - Fresh Water Systems, Inc\Atom')
print(os.getcwd())

# see what items are on the current dir

print(os.listdir())

#create a new folder
#os.mkdir('test-folder')
# create a sub dir underneath a parent or more than one parent dirs
#os.mkdirs('test-parent-dir/test-folder')

#delete dir
#os.rmdir('test-folder')

# rename a file or folder
#os.rename('test-folder','demo-folder')
# get stats on files
print(os.stat('demo-folder\demo.txt'))

# access home environment varaibles
#print(os.environ.get('HOME'))

