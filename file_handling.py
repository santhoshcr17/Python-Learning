# Use words.txt as the file name, example file availabe in http://www.py4e.com/code3/words.txt
fname = input("Enter file name: ") #using input fucntion
fh = open(fname) #creating file handle to open a file, mode is not mentioned so default is read-only
for line in fh: #each line is a string in sequence
    line = line.rstrip() # removing the whitespace from right side
    line = line.upper() # converting lines to all upper case
    print(line)