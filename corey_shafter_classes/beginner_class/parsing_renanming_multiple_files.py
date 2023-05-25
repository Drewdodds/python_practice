# real world problem: Downloaded a bunch of videos from a  class online. But the titles were formatted in such a way that they would not be formmatted correctly.
# We want to rename the files to make more sense. We want to rename them so that the order in which you want to watch is more clear. 
# We can write a scrip that does that for us. 

import os # access to the operating system so you can rename files, move, etc. 

os.chdir(<path_name>) # change directory to the dir that has the files you want to apply script to.

#print(os.getcwd())  # confirm you are in the correct dir. 

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f) # splits each file name by name and extension. 
    f_title, f_course, f_num = file_name.split('-')
    f_title = f_title.strip()  #strip open space
    f_course = f_course.strip() #strip open space
    f_num = f_num.strip()[1:].zfill(2) # strip open space as well as # symbol as well as pad it with a 0 at the begenning. 
    new_name = '{}-{}{}'.format(f_num, f_title, file_ext) # new varaible with new names
    os.rename(f,new_name)



