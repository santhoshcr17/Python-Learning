# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        ff = line.find(":") + 1
        num = float(line[ff:].strip())
        total = total + num
        count = count + 1
print("Average spam confidence:", (total/count))