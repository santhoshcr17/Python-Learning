import re # importing regex module
file = "regex_sum_2355474.txt"
fh = open(file)
lst = list() #creating a list lst = [] also can be used 
for line in fh:
    num = re.findall('[0-9]+', line) #using regex to find the digit 0-9 with "+"" greedy with line interated
    if not num: continue #condition not num means not digit extracted, continue
    lst.extend(int(n) for n in num) # if digit found extend will add each condition match individually & looping num as it's str with var n
try:
    print(sum(lst))
except:
    print(lst)

