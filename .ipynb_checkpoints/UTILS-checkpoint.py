import praw
import sys
import pandas as pd
import os
from os import path
sys.path.append(os.getcwd())
import configure

# log in to reddit using your reddit bot credentials
def login_to_reddit():
    r = praw.Reddit(username = configure.username,
                    password = configure.password,
                    client_id = configure.client_id,
                    client_secret = configure.client_secret,
                    user_agent = configure.user_agent)
    return r

# search for keywords and if there are any, return True
def key_word_exists(comment, key_word):
    comment = comment.lower()
    key_word = [word.lower() for word in key_word]
    if any([word for word in key_word if word in comment]):
        return True
    else:
        return False
