#Remove duplicate char from the string
#eg:hellllllo
#output:helo
 #now get the input string from the user
string=input("Enter the input string :")
 #now create a empty string to store the modified string
remove_duplicate=" "
for i in string:
 		#check if the string is not repeated
 		if i not in remove_duplicate:
 			remove_duplicate+=i
print(remove_duplicate)