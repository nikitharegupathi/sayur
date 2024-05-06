#calculate the income tax for an individual
#get the input from the user for the annual income 
income=int(input("Enter the annual income of the user:"))
tax=0.00
#check if the annual income is less than or equal to 3 lakhs
if income<=300000:
    print("you don't need to pay income tax")
#check if the annual income is range from 3 lakhs to 6 lakhs
elif income>300000 and income<=600000:
    tax=float(income-300000)
    print(f"you need to pay {0.5*tax} income tax to the government" )
#check if the annual income is range from 6 lakhs to 9 lakhs
elif income>600000 and income<=900000:
    tax=float(income-600000)
    print(f"you need to pay {15000 + 0.10*tax} income tax to the government")
# check if the  annual income is range from 9 lakhs to 12 lakhs
elif income>900000 and income<=1200000:
    tax=float(income-900000)
    print(f" You need to pay {45000+ 0.15*tax} income tax for the government")
# check if the annual income is range from 12 lakhs to 15 lakhs
elif income>1200000 and income<=1500000:
    tax=float(income-1200000)
    print(f" You need to pay {90000+0.20*tax} income tax for the government")
#check if the annual income is greater than 15 lakhs    
else:
    tax=float(income-1500000)
    print(f" you need to pay {150000 + 0.30*tax} income tax for the government)