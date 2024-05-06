#ask the user input what things they want to buy
things=input("Enter the things that the customer need to bring:")
#now declare the price of the each things
choc_price=200
cake_price=150
#get the budget as a input from the user
budget=int(input("Enter the amount given by the customer:"))
#now ask that the things are available in the shop
available=input("what did the shop have :")
if(available=="choc and cake"):
	#ask how many choclate that the user want to buy
	choc_count=int(input("Enter how many choc do you want to buy="))
	#ask how many cake the user want to buy
	cake_count=int(input("Enter how many cake do you want to buy="))
	#now calculate the price of the things
	price=((choc_count*choc_price)+(cake_count*cake_price))
	#using if and else condition to find how many choc and cake that the user can buy
	if(budget>=price):
		print("The price of the both choc and cake is",price)
		balance=budget-price
		print(f"You can buy  {choc_count}choc and  {cake_count}cake ,your balance amount is {balance}")
#if the budget is less than price
	else:
		extra_amount=price-budget
		print(f"You have to pay extra {extra_amount} rupees to buy this")
#using elif condition if the shop has only choc
elif(available=="choc"):
	print("Only choc is available")
#ask the choc_count from the user
	choc_count=int(input("Enter the choclate count:"))
#now calculate the price for choc according to their count
	price=(choc_count*choc_price)
#now print the price of the choc
	print("The price of the choc is",price)
#check that the given amount is enough to buy the things
	if(budget>=price):
		balance=budget-price
		print(f"You can buy {choc_count}choc, your balance amount is {balance}")
#if the budget is less than price 
	else:
		extra_amount=price-budget
		print(f"You need to pay extra {extra_amount} rupees to buy these")
#if the shop has only cake
elif(available=="cake"):
	print("Only cake is available")
#now ask the cake count from the user
	cake_count=int(input("Enter how many cake do you want:"))
#calculate the price amount
	price=(cake_count*cake_price)
	print("The price of the cake is",price)
#check that the given amount is enough to buy the cake
	if(budget>=price):
		balance=budget-price
		print(f"you can buy {cake_count}cake ,your balance amount is {balance}")
#if the budget is less than price
	else:
		extra_amount=price-budget
		print(f"You need to pay extra  {extra_amount} rupees to buy these")