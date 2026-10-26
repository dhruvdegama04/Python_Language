"""3.Write a function display_friends() that takes a dictionary of Instagram usernames as 
keys and their follower counts as values, and prints each username with their followers 
in the format: 'username: 2.3K followers'."""

def display_friends(friends_dict):
    for username, followers in friends_dict.items():
        print(f"{username}: {followers} followers")