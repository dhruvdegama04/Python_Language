"""3.Try to change the first element of your fav_apps tuple to 'YouTube' 
and observe the error message. Write a comment explaining why this happens
 based on tuple immutability."""

fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

# This will raise a TypeError because tuples are immutable and their elements cannot be modified after creation
fav_apps[0] = "YouTube"