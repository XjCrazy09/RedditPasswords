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
    
    # Need to work on this so that it doesn't have to spend extra time and processing to read this file
    # every single time.  List is getting large and will eventually cripple the I/O
    # could make it a global and just append the new words to it.  Then it would only load once per execution, not per loop
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

    print "Total user list: ", len(exisiting_users)
    

    for index, user in enumerate(exisiting_users):
        print "Scraping: %s Number %d of %d" % (user,index + 1, len(exisiting_users)) 
        scrape(user)
        
def get_users():
    # Used to add more users to the list
    
    f = open('user_list.txt', 'a')

    # let's try and get a list of users some how.  
    r = praw.Reddit('User-Agent: user_list (by /u/XjCrazy09)')
    
    # check to see if user already exists.  Because if so they have already been scraped.  
    submissions = r.get_random_subreddit().get_top(limit=100)
    print "Running..."
    for i in submissions: 
        print i.author.name
        with open('user_list.txt', 'a') as output:
            output.write(i.author.name + "\n")
    print "Finished..."
    
if __name__ == "__main__":
    # disable warnings to make it look prettier 
    # The reason this is needed is because Reddit wants to move to OAuth
    requests.packages.urllib3.disable_warnings()
    
    
    # Let's import the already exisiting user list as a set so we don't over work. 
    # import section
    print "Importing exisiting Users"
    with open('user_list.txt', 'r') as inputFile:
        exisiting_users = inputFile.read().split()
    
    old_users = set(exisiting_users)
    print "Exisiting Users: ", len(old_users)
    old_user_count = len(old_users)
    
    usersList()
