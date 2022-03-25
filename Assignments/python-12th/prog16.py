'''Write an interactive menu driven program to implement a Queue  containing membership details (Memno, MemName) of a member in a  sports club. The menu contains the following options: 
1. Insert 
2. Delete 
3. Display Queue 
4. Exit  
'''
q=[]
top=rear=None

print('1. Insert  \n2. Delete  \n3. Display Queue \n4. Exit ')

def isempty():
    global q,rear,top
    if q==[]:
        return 1
    else:
        return 0
def enqueue():
    global q,rear,top
    t=eval(input('Enter membership details (Memno, MemName) of the member of the sports club :  '))
    q.append(t)
    if len(q)==1:
        top=rear=0
    else:
        rear+=1
    print('Queue updated.')
def dequeue():
    global q,rear,top
    if isempty()==1:
        print('Underflow')
    else:
        a=q.pop(0)
        if isempty()!=1:
            rear+=1
            top-=1
        else:
            top=rear=None
        print(a,'is removed')
def display():
    global q,rear,top
    if isempty()==1:
        print('Queue is empty')
    else:
        print(q)

x=int(input('Enter (1,2,3 or 4) : '))
while x!=4:
    if x==1:
        enqueue()
    elif x==2:
        dequeue()
    elif x==3:
        display()
    else:
        print('Wrong entry')
    x=int(input('Enter (1,2,3 or 4) : '))        
print('END')    

'''output

1. Insert  
2. Delete  
3. Display Queue 
4. Exit 
Enter (1,2,3 or 4) : 1
Enter membership details (Memno, MemName) of the member of the sports club :  1,'zakir'
Queue updated.
Enter (1,2,3 or 4) : 1
Enter membership details (Memno, MemName) of the member of the sports club :  2,'zakira'
Queue updated.
Enter (1,2,3 or 4) : 1
Enter membership details (Memno, MemName) of the member of the sports club :  3,'makir'
Queue updated.
Enter (1,2,3 or 4) : 1
Enter membership details (Memno, MemName) of the member of the sports club :  14,'takira'
Queue updated.
Enter (1,2,3 or 4) : 2
(1, 'zakir') is removed
Enter (1,2,3 or 4) : 3
[(2, 'zakira'), (3, 'makir'), (14, 'takira')]
Enter (1,2,3 or 4) : 4
END
'''
    
