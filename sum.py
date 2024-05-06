#problem statement
#given list numbers calculate the sum of all numbers in the list
#now initialize the empty list to store all numbers
list=[]
#now ask the user how many numbers to store in to the list
n=int(input("Enter the number of values do you want to store in the list:"))
#now initialize the sum variable as 0
sum=0
for i in range(n):
    #now get the input from the user
    numbers=int(input("Enter the numbers:"))
    #now store the numbers in to the list
    list.append(numbers)
    #now sum all the numbers in the list
    sum+=numbers
#now print the sum
print(sum)
#now print the list
print(list)