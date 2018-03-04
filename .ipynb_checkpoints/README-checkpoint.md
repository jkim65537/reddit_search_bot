# reddit_search_bot

# Introduction
reddit bot that searches for keywords in reddit comments

## Example Usage

### Start the bot run

```python
from search_bot import reddit_search_bot

reddit = reddit_search_bot()

# initialize reddit connection with your own credentials
reddit.update_connection(filepath="/filepath/to/where/you/cloned/this/repo",
                        username=configure.username, 
                        password=configure.password, 
                        client_id=configure.client_id, 
                        client_secret=configure.client_secret, 
                        user_agent=configure.user_agent)

# Search for any mentions of Lebron James in subreddit NBA in the past year
reddit.run(subreddit="nba",key_words="Lebron James",days=365)

# you can also pass in a list of key words instead of a single string & key words are not case sensitive
reddit.run(subreddit="nba",key_words= ["Lebron James", "tObY FLeNderSon"],days=365)


```