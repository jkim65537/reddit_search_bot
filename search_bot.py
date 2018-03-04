import praw
import sys
import pandas as pd
import time
import inspect
import os
sys.path.append(os.getcwd())
try:
    import configure
except ImportError:
    print("Initialize your reddit connection using `initialize_connection' method")
import UTILS

class reddit_search_bot(object):
    def __init__(self, run_time=1):
        """
        inputs: run_time(int) in minutes
        """
        self.comments = None
        self.comment_urls = None
        self.comment_table = pd.DataFrame(columns=["comments", "url"])
        self.run_time = run_time * 60
        
    def update_connection(self, filepath, username, password, 
                           client_id, client_secret, user_agent):
        """
        initialize/update reddit connection by 
        writing a configure file with your credentials
        
        inputs: filepath(str), username(str), password(str),
                client_id(str), client_secret(str), user_agent(str)
        outputs: configure.py
        """
        file = open(os.path.join(filepath, "configure.py"),"w") 
        file.write("client_id = '{}'\n".format(client_id)) 
        file.write("client_secret = '{}'\n".format(client_secret))
        file.write("user_agent = '{}'\n".format(user_agent))
        file.write("username = '{}'\n".format(username))
        file.write("password = '{}'\n".format(password))
        file.close() 
        print("{}/configure.py updated".format(filepath))
        
    def run(self, subreddit, key_word, days=7):
        print("reddit bot searching for your keyword in {} from the past {} days."\
            .format(subreddit, days))
        days = days * 87840
        if isinstance(key_word, str):
            key_word = [key_word]
        comments = []
        comment_urls = []
        r = UTILS.login_to_reddit()     
        # go through every new comment in self.subreddit from the past n days
        for submission in r.subreddit(subreddit)\
                .submissions(int(time.time())-days, int(time.time())):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                if UTILS.key_word_exists(comment.body, key_word):
                    comments.append(comment.body)
                    comment_url = "https://reddit.com" + comment.permalink
                    comment_urls.append(comment_url)
        if len(comments) > 0:
            self.comments = comments
            self.comment_urls = comment_urls
            self.comment_table = pd.DataFrame(
                                                {"comments": comments,
                                                 "url": comment_urls
                                                })
            
        print("""
            Look at `reddit_search_bot.comments` for comments \n
            & `reddit_search_bot.comment_urls` for 
            permalink urls of the comments \n
            % `reddit_search_bot.comment_table for
            comments and urls in a pandas dataframe format.
            """)