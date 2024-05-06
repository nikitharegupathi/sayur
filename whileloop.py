#Ask the user input for how many number of marks they want to enter
n=int(input("How many number of marks do you want to enter:"))
#now declare the initialize value of total is 0
total=0
#now delcare the initialize value of i is 1
i=1
#now create the while loop to run until the n value
while(i<=n):
#now ask the input from the user
	mark=int(input("Enter the mark students obtained:"))
#check if the mark is greater than zero and less than or equal to 100
	if(mark>0 and mark<=100):
#now add the mark obtained
	    total+=mark
#increement the i value 
	    i+=1
	else:
		print("Enter valid mark")
#print the total mark obtained by the student
print(f"The total mark obtained is { total}")
#calculate the average 
average=total/n
#print the average
print(f"The average is {average}")