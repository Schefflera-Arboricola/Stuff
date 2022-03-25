'''Listopr.py'''

def display(l):
    '''Displays the the list entered.'''
    print(l)

def read(l):
    ''' Read the list entered'''
    l=eval(input('enter list : '))
    return l

def sort(l):
    '''sorting the list(in increasing order) using bubble sort'''
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def search(l):
    '''searching an element from a list : returns a tuple having positions of the element.'''
    print('enter 1 if element is integer or 2 if element is string')
    f=int(input('enter: '))
    if f==1:
        e=int(input('enter element : '))
    else:
        e=input('enter element : ')  
    c=()
    for i in range(len(l)):
        if l[i]==e:
            c+=(i+1,)
    return c 
            
