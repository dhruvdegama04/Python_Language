"""
3.Given a list of song durations in minutes, use a lambda function with the map() 
function to convert all durations to seconds and print the resulting list."""

durations_minutes = [3.5, 4.0, 2.8, 3.2]

durations_seconds = list(map(lambda m: m * 60, durations_minutes))

print(durations_seconds)