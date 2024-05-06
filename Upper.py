#problem statement
#write a program that converts the first letter of each word in a given sentence in to a upper case(title case)

#now get the input from the user
user_input=input("Enter the input sentence:")
#now split the sentence in to a specific word and store in to a list
sentence=user_input.split()
#now create a empty list to store the modified word
modified=[]

for i in sentence:
	#now change the each word in a given sentence in to a upper case
	modified=i[0].upper()+i[1:]
	#now print the modified word
	print(modified, end=" ")