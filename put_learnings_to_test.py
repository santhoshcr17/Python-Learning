Highest = None
Lowest = None
count = 0
Total = 0
while True:
    score = input("Enter the Score:")
    if score == "Done":
        break
    try:
        score = int(score)
        if Highest is None or score >= 75:
            Highest = score
            count = count + 1
            Total += Highest 
        elif Lowest is None or score < 75:
            Lowest = score
            count = count + 1
            Total += Lowest
    except ValueError:
        print("Invalid Input")
        break
print("Highest:", Highest)
print("Lowest:", Lowest)
print("Average:", Total/count)