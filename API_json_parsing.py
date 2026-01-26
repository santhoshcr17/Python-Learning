import urllib.request, urllib.parse   # Libraries to fetch data from URLs and encode query parameters
import json, ssl                      # JSON library to parse responses, SSL for secure connections

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'  # Base URL for the geocoding API

# Ignore SSL certificate errors
ctx = ssl.create_default_context()    # Create SSL context
ctx.check_hostname = False            # Disable hostname checking
ctx.verify_mode = ssl.CERT_NONE       # Disable certificate verification

while True:                           # Loop until user quits
    address = input('Enter location: ')   # Ask user for a location
    if len(address) < 1: break            # Exit loop if input is empty

    address = address.strip()             # Remove leading/trailing spaces
    parms = dict()                        # Create dictionary for query parameters
    parms['q'] = address                  # Add location query to parameters

    url = serviceurl + urllib.parse.urlencode(parms)  # Build full URL with encoded parameters

    print('Retrieving', url)              # Show the URL being retrieved
    uh = urllib.request.urlopen(url, context=ctx)     # Open the URL with SSL context
    data = uh.read().decode()             # Read and decode response (bytes → string)
    print('Retrieved', len(data), 'characters')  # Show how many characters were retrieved

    try:
        js = json.loads(data)             # Parse JSON string into Python dictionary
    except:
        js = None                         # If parsing fails, set js to None

    if not js or 'features' not in js:    # Check if JSON is valid and contains "features"
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:          # If no features found, report object not found
        print('==== Object not found ====')
        print(data)
        break

    print(js['features'][0]['properties']['plus_code'])  # Print the Plus Code of the first feature
