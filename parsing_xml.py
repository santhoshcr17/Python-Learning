import urllib.request              # Import module to open and read data from URLs
import xml.etree.ElementTree as ET # Import module to parse XML data

url = input('Enter location: ')    # Ask user to enter a URL
if len(url) < 1 :                  # If user presses Enter without typing anything
    url = 'http://py4e-data.dr-chuck.net/comments_2355478.xml'  # Use default URL

print('Retrieving', url)           # Show which URL is being retrieved
uh = urllib.request.urlopen(url)   # Open the URL
data = uh.read()                   # Read the entire contents of the URL
print('Retrieved', len(data), 'characters')  # Print how many characters were retrieved

tree = ET.fromstring(data)         # Parse the XML data into a tree structure

counts = tree.findall('.//count')  # Find all <count> elements anywhere in the XML
nums = list()                      # Create an empty list to store numbers

for result in counts:              # Loop through each <count> element found
    n = int(result.text)           # Convert the text inside <count> to an integer
    nums.append(n)                 # Add the integer to the list
    print(n)                       # Print the number

print('Count:', len(nums))         # Print how many numbers were found
print('Sum:', sum(nums))           # Print the sum of all numbers
