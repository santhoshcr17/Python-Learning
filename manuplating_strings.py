text = "X-DSPAM-Confidence:    0.8475"
# find the colon
pos = text.find(':')
# slice everything after colon, strip spaces
num_str = text[pos+1:].strip()
# convert to float
num_val = float(num_str)
print(num_val)   # 0.8475