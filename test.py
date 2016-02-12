# Author: Ryan Villarreal
# playing around with building wordlists using Python's Reddit API Wraper (praw)
# as well as built-in Python functions such as set 

import praw, os, time
from pprint import pprint
import requests.packages.urllib3

def scrape(user):

    f = open(user + '.txt', 'w')
    
    r = praw.Reddit('User-Agent: testing_praw (by /u/XjCrazy09)')
    xjcrazy = r.get_redditor(user)
    for comments in xjcrazy.get_comments(limit=None):
        f.write(str(comments))
    
    f.close()
    time.sleep(5)
    print "moving on to writing..."
    writing(user)
    
def writing(user):
    
    # import section
    print "Importing exisiting unique words"
    with open('unique.txt', 'r') as inputFile:
        exisiting = inputFile.read().split()
    
    unique_words = set(exisiting)
    print "Exisiting unique words: ", len(unique_words)
    old = len(unique_words)

    # read the new input file and append it to the existing set. 
    with open(user + '.txt') as f:
        words = f.read().split()
        unique_words |= set(words)
    
    with open('unique.txt', 'w') as output:
        for word in unique_words:
            output.write(str(word) + "\n")

    new = len(unique_words)
    print "New words added: ", new-old
    print "Total unique_words: ", len(unique_words)
    
    # clean up files now.  
    print "cleaning up now..."
    os.remove(user + '.txt')
    
    # slow your roll... don't want to step on any toes. 
    print "sleeping, so I don't step on any toes..."
    time.sleep(10)
    print "done sleeping... \n"
    
def usersList(): 
    # import section
    print "Importing exisiting Users."
    with open('user_list.txt', 'r') as inputFile:
        old_users = inputFile.read().split()
    exisiting_users = set(old_users)
    print exisiting_users
    print "Total user list: ", len(exisiting_users)
    
    
    for user in exisiting_users:
        print "Scraping: ", user 
        if user in exisiting_users:
            print "Already Scraped, moving on \n"
        else: 
            scrape(user)
            
def get_new_users():
    print 'adding new users'
    
    
if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    usersList()