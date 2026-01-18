fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for lines in fh:
    line = lines
    if not line.startswith("From:"):
        continue 
    count = count + 1
    t = (line.split())
    print(t[1])
print("There were", count, "lines in the file with From as the first word")
