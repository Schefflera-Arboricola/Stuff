'''Q 3 . Create a module named ‘Listopr.py’which has functions to:
•Display the list
•Read the list
•Sort the list using bubble sort method
•Search for an element in the list
Write a program to import the module and call these functions in the program using a menu driven program.Note:Don’t use built-in functions of Python library
'''

from listopr import *
l=eval(input('enter list : '))
print('Enter 0 to exit\nEnter 1 to display the list\nEnter 2 to enter the list\nEnter 3 to sort the list\nEnter 4 to search an element in the list')
n=int(input('Enter : '))
while n!=0:
    if n==1:
        display(l)
    elif n==2:
        l=read(l)
        print(l)
    elif n==3:
        l1=sort(l)
        print(l1)
    elif n==4:
        c=search(l)
        print(c)    
    n=int(input('Enter : '))
'''
outputs

enter list : [1,2,2,56,341,98]
Enter 0 to exit
Enter 1 to display the list
Enter 2 to enter the list
Enter 3 to sort the list
Enter 4 to search an element in the list
Enter : 1
[1, 2, 2, 56, 341, 98]
Enter : 2
enter list : [3,5,21,54,31]
[3, 5, 21, 54, 31]
Enter : 3
[3, 5, 21, 31, 54]
Enter : 4
enter 1 if element is integer or 2 if element is string
enter: 1
enter element : 5
(2,)
Enter : 0
'''











