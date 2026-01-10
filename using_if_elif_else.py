units = (int(input("Units Consumed?")))
if units <= 100:
    total_bill_amount = units*5
elif units <= 200:
    total_bill_amount = units*7
elif units > 200:
    total_bill_amount = units*10
print(total_bill_amount)