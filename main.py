# Author: Ryan Villarreal
# playing around with building wordlists using Python's Reddit API Wraper (praw)
# as well as built-in Python functions such as set 

import praw, os
from pprint import pprint

def scrape(user):
    f = open(user + '.txt', 'w')
    
    r = praw.Reddit('User-Agent: testing_praw (by /u/XjCrazy09)')
    xjcrazy = r.get_redditor(user)
    for comments in xjcrazy.get_comments(limit=None):
        f.write(str(comments))
    
    f.close()
    writing(user)
    
def writing(subreddit):

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
    #print "cleaning up now..."
    #os.remove(user + '.txt')
    

if __name__ == "__main__":
    user = raw_input("What User to Scrape? ")
    scrape(user)
    
    #r = praw.Reddit('User-Agent: testing_praw (by /u/XjCrazy09)')