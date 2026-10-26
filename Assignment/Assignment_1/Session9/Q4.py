"""4.Remove an app you no longer use from your my_fav_apps list using the remove() 
method, then use the pop() method to remove the last app and print the list after each 
operation."""

my_fav_apps = ["Instagram", "Zomato", "Spotify", "WhatsApp", "YouTube"]

my_fav_apps.remove("Zomato")
print(my_fav_apps)

my_fav_apps.pop()
print(my_fav_apps)