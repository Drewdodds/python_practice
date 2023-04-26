# We will be looking at how to read, parse, and write csv files. 
# Csv files standard for comma separated values. They allow us to store tabulated data in a plain text file (which is smaller)
# the data looks like a mess but it's not really meant to be read like that. Just how it is stored.
# The top line will have the fields and everything after that will be the accociated values.
# we will work with a test csv file I made in this current dir
# vid: https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=15

import csv

# in order to read this file we will use the context manager just like any other file.

# with open('csv_mod_prac.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file) # by default this is expecting values to be separated by a comma so as is now, we don't need to pass any additonal args.
#     # this is something we will need to iterate over
#     # print(csv_reader) if we just print it like so we see that it is just a reader object in memory. So we need to loop over all these lines in the reader.
#     for line in csv_reader:
#         #print(line) #here we print out each line in the list. the first line being the field names. This is where we can play and print our whatever index we want
#         print(line[2]) #here we are printing index 2 which is the emails

# lets now create a new file that has dashes as the delimeter.

# with open('csv_mod_prac.csv', 'r') as csv_file: # opening the original file and reading it
#     csv_reader = csv.reader(csv_file) #created a csv reader var

#     with open('new_names.csv', 'w') as new_file: # opening a new file for writing
#         csv_writer = csv.writer(new_file, delimiter='\t') # create a new writer var and using a writer method to write new file with dash as delimiter. Then did a dash

#         for line in csv_reader: # for each line in the original we are writing out to the new file each line of the original
#             csv_writer.writerow(line) # and you can see it created a new file. 

# another way to deal with csv files is using a dicttionary reader and writer

# with open('csv_mod_prac.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line) # this does not contain the field names b/c they are now the keys of each of the values. So it just prints the value below. 
# # this actually makes it easier to parse out the data. 
# # with the dict writer we now need to specify the keys.

with open('csv_mod_prac.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names_2.csv', 'w') as new_file:
        fieldnames = ['first_name','last_name','email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)