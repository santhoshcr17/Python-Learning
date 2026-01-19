# Ask for file name
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file
handle = open(name)

# Create dictionary to store counts
counts = dict()

# Loop through each line
for line in handle:
    # Only look at lines that start with "From "
    if line.startswith("From "):
        parts = line.split()
        time = parts[5]          # The time field, e.g. "09:14:16"
        hour = time.split(":")[0]  # Split by ":" and take the hour
        counts[hour] = counts.get(hour, 0) + 1

# Print results sorted by hour
for hour, count in sorted(counts.items()):
    print(hour, count)
