#ask the user input what the customer want
things=input("Enter what things do you want to buy:")
#ask the money input from the user
money=int(input("How much money the user gave:"))
#declare the things cost
vada_cost=30
soda_cost=10
sandwich_cost=100
#check if the customer bought three things
if(things=="vada soda sandwich"):
#ask the vada count input from the user
	vada_count=int(input("Enter how many vada do you want:"))
#ask the soda count from the user
	soda_count=int(input("Enter how many soda do you want:"))
#ask the sandwich count from the user
	sandwich_count=int(input("Enter how many sandwich do you want:"))
#now calcate the bill 
	bill=float((vada_count*vada_cost)+(soda_count*soda_cost)+(sandwich_count*sandwich_cost))
#if money is greater than bill
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")
#check if the customer ask only vada and soda
elif(things=="vada soda"):
#ask the vada count from the user
	vada_count=int(input("Enter how many vada do you want:"))
#ask the soda count from the user
	soda_count=int(input("Enter how many soda do you want:"))
#now calculate the bill amount
	bill=float((vada_count*vada_cost)+(soda_count*soda_cost))
#check if money is greater than bill
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")
#check if the user only want vada and sandwich
elif(things=="vada sandwich"):
#ask the vada count
	vada_count=int(input("Enter how many vada do you want:"))
#ask the sandwich count
	sandwich_count=int(input("Enter how many sandwich do you want:"))
#now calculate the bill amount
	bill=float((vada_count*vada_cost)+(sandwich_count*sandwich_cost))
#check if the money is greater than bill amount
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")
#check if the user ask only soda and sandwich
elif(things=="soda sandwich"):
#ask the soda count
	soda_count=int(input("Enter how many soda do you want:"))
#ask the sandwich count
	sandwich_count=int(input("Enter how many sandwich do you want:"))
#now calculate the bill amount
	bill=float((soda_count*soda_cost)+(sandwich_count*sandwich_cost))
#check if the users money is greater than the bill amount
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")
#if the user ask only vada
elif(things=="vada"):
#ask only vada count
	vada_count=int(input("Enter how many vada do you want:"))
#calculate the bill amount
	bill=float((vada_count*vada_cost))
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")	
#if the user only ask soda	
elif(things=="soda"):
#ask the soda count
	soda_count=int(input("Enter how many soda do you want:"))
#calculate the bill amount
	bill=float((soda_count*soda_cost))
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")	
#if the user only ask sandwich	
if(things=="sandwich"):
#ask the sandwich count
	sandwich_count=int(input("Enter how many sandwich do you want:"))
#calculate the bill amount
	bill=float((sandwich_count*sandwich_cost))
	if(money>bill):
		print(f"your bill amount is {bill}, your balance amount is {money-bill}")
	else:
		balance=float(bill-money)
		print(f"you have to pay extra {balance} rupees to buy these")