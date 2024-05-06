#count the word from the given sentence
#get input sentence from the user
input_sentence=input("Enter the input sentence from the user:")
#split sentence 
sentence=input_sentence.split()
#initialize count variable as 0
count=0
#initialize for loop 
for i in sentence:
    #now count the words
    count+=1
    #now print the total words count
print(count)