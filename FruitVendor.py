#ask what the customer want to buy
cust_input=input("Enter what do you want to buy ?:").lower()
#now split the input sentence from the user in to individual string
cust_need=cust_input.split()
#now store the fruits in the list
fruits=['apple','orange','banana']
count=0
fruit=""
quantity=0
for i in cust_need:
    if i .isdigit():
        count=i
    elif i in fruits:
        fruit=i
#if the customer include both fruit and the quantity of the fruit
if fruit and count:
# print the fruit and quantity
    print(f"you  need to buy {count} {i} ")
    #if the customer did not mention the quantity of the fruit ask them how many fruits they want to buy
elif fruit:
    quantity=int(input("How many fruits do you need to buy:"))
    print(f"you need to buy {quantity} {fruit}")