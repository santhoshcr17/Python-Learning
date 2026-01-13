largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":   # exit condition
        break
    
    try:
        num1 = int(num)   # safe conversion
        
        # handle first assignment
        if largest is None or num1 > largest: #num1 > largest would fail (because None cannot be compared to an integer).
            largest = num1
        if smallest is None or num1 < smallest:
            smallest = num1
            
    except ValueError:   # catch invalid input
        print("Invalid input")
        break

print("Maximum", largest)
print("Minimum", smallest)
