ac = float(input("Please Enter the Actual Cost:"))
sc = float(input("Please Enter the Sales Cost:"))

if (sc > ac):
    profit = sc - ac
    print("Total profit is",profit)

else:
    print("No Profit")   