'''15 . Write an interactive menu driven program to implement a Stack  containing travel details (PNo, PName) of a passenger. The menu  contains the following options: 
1. Push 
2. Pop 
3. Display stack 
4. Exit 
'''
print('1. Push \n2. Pop \n3. Display stack\n4. Exit ')

stk=[]
top=None

def isempty():
    global stk,top
    if stk==[]:
        return 1
    else:
        return 0
def push():
    global stk,top
    t=eval(input('Enter travel details (PNo, PName) of the passenger :  '))
    stk.append(t)
    if len(stk)==1:
        top=1
    else:
        top+=1
    print('Stack updated.')
def pop():
    global stk,top
    if isempty()==1:
        print('Underflow')
    else:
        a=stk.pop()
        if isempty()!=1:
            top-=1
        else:
            top=None
        print(a,'is removed')
def display():
    global stk,top
    if isempty()==1:
        print('Stack is empty')
    else:
        print(stk)

x=int(input('Enter (1,2,3 or 4) : '))
while x!=4:
    if x==1:
        push()
    elif x==2:
        pop()
    elif x==3:
        display()
    else:
        print('Wrong entry')
    x=int(input('Enter (1,2,3 or 4) : '))        
print('END')    
    
'''OUTPUT

1. Push 
2. Pop 
3. Display stack
4. Exit 
Enter (1,2,3 or 4) : 1
Enter travel details (PNo, PName) of the passenger :  1,'Zahira'
Stack updated.
Enter (1,2,3 or 4) : 1
Enter travel details (PNo, PName) of the passenger :  2,'Zahir'
Stack updated.
Enter (1,2,3 or 4) : 1
Enter travel details (PNo, PName) of the passenger :  3,'mahira'
Stack updated.
Enter (1,2,3 or 4) : 1
Enter travel details (PNo, PName) of the passenger :  4,'mahir'
Stack updated.
Enter (1,2,3 or 4) : 3
[(1, 'Zahira'), (2, 'Zahir'), (3, 'mahira'), (4, 'mahir')]
Enter (1,2,3 or 4) : 2
(4, 'mahir') is removed
Enter (1,2,3 or 4) : 3
[(1, 'Zahira'), (2, 'Zahir'), (3, 'mahira')]
Enter (1,2,3 or 4) : 4
END
'''
