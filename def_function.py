# def function is used to store a code & execute when needed instead of writing the code again wherever needed
def computepay(h, r):
    if h <= 40:
        multiply = r*h
    elif h > 40:
        multiply = 40*r+((h-40)*r*1.50)
    return multiply # this will return the operation performed to arguements above aka h,r

h = (float(input("Enter Hours:")))
r = (float(input("Enter rate:")))
p = computepay(h,r) # this is where function is called
print("Pay", p)