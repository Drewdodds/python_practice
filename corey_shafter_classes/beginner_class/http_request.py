# The request library if very popular and it allows us to easily make a http request to get information from webistes. 
# This is fairly easy to use. We will learn how to get info from website as well as post info, download images, send off info, follow redirects, etc.
# Let's look at the basics...the request libary is great gor getting info from a site but it's not menbt to parse that info.
# to parse...we will use something like beautiful soup. 
# you have to install the request library using pip -  "pip install request"

# first, let's grab the contents of a website "https://xkcd.com/353/"

import requests

r = requests.get('https://xkcd.com/353/')

# print(r) # we get a response object. Now let's see if we can get the contents of this page. 

# print(r.text) # this is how you get the source of the webiset. This is literall the same contents if you clicked "view page source" in your browser
# if you wanted to parse out this infomation then you would need an hrml parser

# what if you wanted to download an image? You could past the url to that image. It will print out the bites of an image and you can save it to your machine. 
# r = requests.get('https://xkcd.com/353/')
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# this will save the file in the current dir. But you can specify a path as well.

# we can also print the status of a get request
print(r.status_code)
# a 200 code means it is good
# 300 are redirects
# 400s are client errors
# 500s are server errros

print(r.ok) # will return anything that is not a 400 response. 

