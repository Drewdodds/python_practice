# this file corresponds to import_mods_ex_fun. That file contains the function that we import here and use. 

import import_mods_ex_fun

# let's say we wanted to use that find index function we built in the other file. 

#Right now that files lives in the same directory so we can import it right over.

#When we import a file it runs all the code on the module.

courses = ['History', 'Math','Physics', 'CompSci']

# Now, in order to call and use the function you have to call it first.

index  = import_mods_ex_fun.find_index(courses, 'Math')

print(index) # which equals 1

# you can also shorten the module name so you don'thave to type it out everywhere.

# import import_mods_ex_fun as mm
# index  = mm.find_index(courses, 'Math')

#btw, when we import a module how does it know where to find this module...since we didn't pass a file path?
# The way this works is that when we import a module it checks multiple locations. And the locatiosn it checks is within a list called sys.path
import sys
print(sys.path)

# you'see the current directory is first on the list. That is where it checks first. What else is added? Directories added the py path vairable, 
# standard library directy dir which means we are able to use it with out installs separately. This is very useful. 
# If you are performing a common task then most likely someone has already written it.
# lastly the site packages (3rd party dirs)

