import praw, time
from pprint import pprint

f = open('user_list.txt', 'a')

# let's try and get a list of users some how.  
r = praw.Reddit('User-Agent: user_list (by /u/XjCrazy09)')
user_list = dict()

submissions = r.get_subreddit('all').get_top(limit=100)
for i in submissions: 
    f.write(str(i.author.name) + "\n")
    
# check to see if user already exists.  Because if so they have already been scraped.  
