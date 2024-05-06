#To find max and min of the given numbers
#Ask the input numbers from the user
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number 2:"))
num3=int(input("Enter the number 3:"))
#Ask the user choice
choice =input("Ask the user to find the min value or max value:")
#now print the user choice 
print("The user choice is",choice)
#if the choice was max using if condition to find the maximum value of the given numbers
if(choice == "max"):
	if(num1>num2 and num1>num3):
		print("Maximum value is",num1)
	elif(num2>num3 and num2>num1):
		print("Maximum value is",num2)
	elif(num3>num1 and num3>num2):
		print("Maximum value is ",num3)
#if the choice was min then usjng elif condition to find the minimum value of the given numbers
elif(choice == "min"):
	if(num1<num2 and num1<num3):
		print("Minimum value is",num1)
	elif(num2<num3 and num2 <num1):
		print("Minimum value is",num2)
	elif(num3 <num1 and num3<num2):
		print("Minimum value is ",num3)