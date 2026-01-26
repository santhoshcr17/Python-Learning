import json                       # Import the built-in JSON library to parse JSON data
import urllib.request             # Import urllib.request to open and read data from URLs

url = input("Enter the URL:")     # Ask the user to enter a URL (string input)

openurl = urllib.request.urlopen(url)  # Open the given URL and create a connection object
data = openurl.read().decode()         # Read the data from the URL and decode bytes into a string

do = json.loads(data)             # Parse the JSON string into a Python dictionary

nums = list()                     # Create an empty list to store numeric values

for info in do['comments']:       # Loop through each dictionary inside the "comments" list
    n = int(info['count'])        # Convert the "count" value from string/number into an integer
    nums.append(n)                # Add the integer to the nums list
    print(n)                      # Print each count value

print('Count:', len(nums))        # Print how many count values were found
print('Sum:', sum(nums))          # Print the sum of all count values
