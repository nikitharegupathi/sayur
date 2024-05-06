inputsentence=input("Enter the input sentence from the user:")
sentence=inputsentence.split()
keyword="ay"
modified=[]
for i in sentence:
    initial=i[0]
    if(len(i)>1):
        modified=i[1:]+initial+keyword
        print(modified)
    else:
        modified=initial+keyword
        print(modified) 