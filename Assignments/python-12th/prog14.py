'''Q14. Write an interactive menu driven program to implement Stack as list containing integer values. The menu contains the following options:
1.Push
2.Pop
3.Display stack
4.Exit'''


stack1=[]
top=None
def isempty ():
    global stack1
    global top
    if stack1==[]:
        return 1
    else:
        return 0
def Push ():
    global top
    global stack1
    data=int(input('Enter the data to be pushed : '))
    stack1.append (data)
    top=len(stack1)-1
    print('Stack updated !')

def Pop ():
    global top
    global stack1
    if isempty () ==1:
        print('Underflow\nEmpty stack')
    else:
        data=stack1.pop()
        if len(stack1)==0:
            top=None
        else:
            top=len(stack1) -1
        print(data,'removed !')
    
def Display ():
    global top
    global stack1
    if isempty ()==1:
        print ('Empty Stack')
    else:
        print (stack1)

print('Menu :\n1.Push\n2.Pop\n3.Display stack\n4.Exit')
a=int(input('Enter 1,2,3,4: '))
while a!=4:
    if a==1:
        Push()
    elif a==2:
        Pop ()
    elif a==3:
        Display()
    else:
        print('Wrong entry')
    a=int(input('Enter 1,2,3,4: '))
print('END')

'''output

Menu :
1.Push
2.Pop
3.Display stack
4.Exit
Enter 1,2,3,4: 1
Enter the data to be pushed : 45
Stack updated !
Enter 1,2,3,4: 1
Enter the data to be pushed : 822
Stack updated !
Enter 1,2,3,4: 1
Enter the data to be pushed : 98
Stack updated !
Enter 1,2,3,4: 2
98 removed !
Enter 1,2,3,4: 3
[45, 822]
Enter 1,2,3,4: 4
END
'''
    
