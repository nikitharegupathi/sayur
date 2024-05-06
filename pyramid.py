#get the input string from the user
string=input("Enter the string from the user:")
#now create a empty new string
newstring=" "
#create for loop to run the loop until the length of the input string
for i in range(len(string)):
#now concardinate the current string 
	newstring+=string[i]
#print newstring
	print(newstring)