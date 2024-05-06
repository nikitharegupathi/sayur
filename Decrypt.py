#get the input from the user
input=input("Enter the input string from the user:")
temp=""
decrypt=""
for i in input:
	#if the encrypt string has numbers
	if i.isdigit():
		#use for loop to print the chars 
		for i in range(int(i)):
			decrypt=temp
			#print the decrypt strings
			print(decrypt,end="")
		temp=""
	else:
		temp+=i