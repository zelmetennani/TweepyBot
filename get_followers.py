# import the module
import tweepy
from config import create_api
  

# calling the api 
api = create_api()
  
# the screen_name of the targeted user
screen_name = "geeksforgeeks"
  
# printing the latest 20 followers of the user
for followers in api.get_followers(screen_name=screen_name):
    print(followers.screen_name)