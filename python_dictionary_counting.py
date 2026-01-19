name = input("Enter file:") #input function to ask the file name
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name) # file handle to open a file
sender = dict() # creating a dictionary from nothing
for names in handle: # for loop to iterate all line as string
    email = names.split() # splitting line into strings
    for user in email: # for loop to interate each lines
        if user.startswith("From:"): # starts with From:
            user = email[1] # calling the 2nd string
            sender[user] = sender.get(user,0) + 1 # checking if that string/key exist in dictionary if not add it & add the value
highsender = None
highcount = None
for word, count in sender.items(): # double iteration using .items to get key & value
    if highcount is None or count > highcount: # stating higcount is None
        highsender = word
        highcount = count
print(highsender, highcount)

        