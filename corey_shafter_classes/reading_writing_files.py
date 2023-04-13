# File objects
# Whether you use Python for web apps or desktop apps, etc you will be intereacting with files so it's a good skill to learn.

# open files
# with out a context manager:
#f = open('test_text_file.txt', 'r') # if you are working with files from different dirs than you have to pass the path. In this case, it is in the same dir.
# the open command allows us to specify if we want to open for reading, writing, appending, reading/wriring, etc. Default is read.
# w = write
# r = read
# a = append
# r+ = read and write

# print(f.name) # print the name of the file object

# f.close() # if you don't use a context manager you have to then close the file. It is best practice to use a context manager to avoid mistakes and leaks. 

#context manager: when we exit the block of code it will autop close the file.

# with open('test_text_file.txt', 'r') as f:
#     print(f.name)

# with open('test_text_file.txt', 'r') as f:
#     f_content = f.read()
#     print(f_content)
# this is good for smaller files. 

# what if you had larger files? You don't want to load all of the contents of that file all into memeory. There are other methods for this. 

# instead of f.read() you could do f.readlines() which will then print a list of all of the lines in the file.
# or you could do f.readline which will just read one line at a time.
# How can we read all of the content from an extremely large file. If we read the entire file all in at once we could run out of memory. 
# And we dont' want to do f.readline() 1,000s of times
# so instead, we could iterate over the lines in a file by using a for loop. This reads out all of the lines.
# with open('test_text_file.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

#This is effecient b/c it's not reading out all of the contents all at once. So it's not a memory issue we have to worry about. 

# another thing you can do is pass in a numeric value (representing characters) in the read() method -- of a file using read(100) for example
# what happens if we don't know how large the file is? We can use a for loop again with the read() method. 
# with open('test_text_file.txt', 'r') as f:
#     size_to_read = 100
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
    
# this will grab the 1st 100 characters from the file. But the end will print out an empty string. So we can add a while loop. See below at the new code. 
# with open('test_text_file.txt', 'r') as f:
#     size_to_read = 10

#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)

# let's look at writing to files. See the below mod in the context manager. We changed the mode from 'r' to 'w'. 
# Be careful doing this. If the file does not exist, it will create it. If it does, it will write over it. 
with open('test_2.txt', 'w') as f:
    f.write('Test')