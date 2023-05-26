# In this vid we will learn how to scrape websites using the buetiful soup library.
# we will use one of corey schafer's pages from his website for practice. We will also create a csv outfile. 

# html is structured in a way that all data in instide of tags

from bs4 import BeautifulSoup
import requests

# let's pass our html into beautiful soup so we can get an html object

r = requests.get('https://coreyms.com/').text # first we get teh html

soup = BeautifulSoup(r, 'lxml') # run beautiful soup on it

#print(soup.prettify()) # then prent the prettified version

# now lets grab the first article on the page

article = soup.find('article')

#print(article.prettify()) # this will give us a clean version of that first article

headline = article.h2.a.text # just printing the headlne of the latest post
#print(headline)

# with open('test_file.txt', 'w') as f: # here I created an outfile with that info
#     f.write(headline)

# now lets get the summary text

summary = soup.find('div' , class_='entry-content').p.text

#print(summary)

# now lets get the link to the vid. The vids are embedded. It should be in an iframe

vid_scr = soup.find('iframe', class_='youtube-player')['src'] # here we are accessing an attribute (specifically src) within the iframe tag
#print(vid_scr)

vid_id = vid_scr.split('/')[4] # then we get the full url split by /

vid_id = vid_id.split('?')[0] # then we get the actual ID of the video
print(vid_id)

# so what if we wanted to create an out file for the header, summary, and the you tube video?
# you would initiate an open file belowthe soup variable, then create a write object variable then use writerow([]) and pass in the headers first for the csv
# then at the bottom of the code write the code for so that each iteration will write the values to the csv. 
# So i could do this a a version of this to get pricing data from competitors PLPs