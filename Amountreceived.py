#Ask the n value input from the user
n=int(input("Enter the value of n:"))
count=0
amount=0
for i in range(n):
	#Ask the input from the user to receive money from the parents
	money_received=int(input("Enter the money you received from the parents="))
	#now count how many times we receive ampunt from the user
	count+=1
	#now add all the money receive from the user
	amount+=money_received
	# check if the received money greater than or equal to 10 
	if(money_received>=10):
		print("Thank You")
		continue
	#check if the received money is equal to 1000
	if(money_received==1000):
		break
		#now print how many times we ask for total amount
print(count)
#print the total amount wr receive from the parents
print(amount)