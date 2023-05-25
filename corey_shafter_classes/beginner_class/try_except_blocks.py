# In this vid we will go over how to handle erros and exceptions in Python by learning how these try except blaocks work.
# why would we need a try and except block in the first place? If we get an error then we wouldn't want the system displayed error to necessarily be display to the user
# So if we can anticipate sections of our code that might throw an error or an exception then we can use these try and accept blocks to handle them in the way that we
# want so let's look at an example. 

# f = open('testfile.txt')  this code will throw an error b/c the file doesn't exist...so if we move that to the block below like so...

try:
    f = open('testfile.txt')

except Exception:
    print('Sorry. This file does not exist') # this throws a custom error that is more helpful.
# you can put as many exceptions in here as youwant

# else: this will then run if it doesn't catch any exceptions
#     pass
# finally: # this block will then run no matter what.
#     pass