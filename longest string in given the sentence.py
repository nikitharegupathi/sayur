#Longest word in a sentence
#input:python is a powerful programming language
#output:programming
#get the input string from the user
inputsentence=input("Enter the input sentence:")
#now split the sentence in to a seperate string and store it 
sentence=inputsentence.split()
#now create a empty string 
longest_string=" "
for i in sentence:
	#now check each string in the sentence to get the longest string
	if(len(i)>len(longest_string)):
		#now store the longest string in a empty set variable
		longest_string=i
#now print the longest_string 
print(longest_string)