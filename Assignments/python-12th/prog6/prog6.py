'''Q6. Write a program to read a text file ‘letters.txt’containing many lines of text to find the most commonly occurring word(s).'''
file=open('lettersprog6.txt','r')
str=file.readlines()        #reading the file
d={}
str=(''.join(str)).split()    #joining all lines and then separating all words .

for i in str:                #creating a dictionary having key:value pairs as <word>:<number of times it occured>
    i=i.lower()
    if i.isalpha()==True:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

val=list(d.values())
val1=[]
for i in val:              #making a list of all values with no repition
    if i not in val1:
        val1+=[i]
d1={}
for i in val1:        #grouping words that occur same number of times in a dictionary in the form <tuple of words>:<number of times they occured> 
    t=()
    for j in d:
        if d[j]==i:
            t+=(j,)
    d1[t]=i

val2=tuple(d1.values())
max=max(val2)             #finding the maximum value in dictionary .
for i in d1:
    if d1[i]==max:
        print(i,'occur',d1[i],'times (and also the maximum number of times) in the textfile.')
        break
        
'''output

('the', 'and', 'i') occur 9 times (and also the maximum number of times) in the textfile.

'''
