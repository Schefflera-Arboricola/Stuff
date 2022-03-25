'''QUESTION :
Write functions to delete a record in the binary file ‘student.dat’
created in Q7 using:
 Name of student
 Rollno of student
Call these functions in the __main__ program to delete the records
depending upon user’s choice and display the remaining records.'''

import pickle as p
import os
def deletename():
    l=[]
    name=input('Enter the name of the student whose record you want to delete: ')
    f=open('student.dat','rb')
    f1=open('newstudent.dat','wb')
    found=False

    try:
        while True:
            rec=p.load(f)
            if name==rec[1]:
                found=True
            else:
                p.dump(rec,f1)
                l+=[rec,]
    except:
        f.close()
        f1.close()
    if found==False:
        print(name,'not found.')
    else:
        print('\nRemaining Records : \n')
        for i in l:
            print(i)
    os.remove('student.dat')
    os.rename('newstudent.dat','student.dat')

def deleterollno():
    l=[]
    rollno=int(input('Enter the rollno of the student whose record you want to delete: '))
    f=open('student.dat','rb')
    f1=open('newstudent.dat','wb')
    found=False

    try:
        while True:
            rec=p.load(f)
            if rec[0]==rollno:
                found=True
            else:
                p.dump(rec,f1)
                l+=[rec,]
    except:
        f.close()
        f1.close()
    if found==False:
        print(rollno,'rollno not found.')
    else:
        print('\nRemaining Records : \n')
        for i in l:
            print(i)
    os.remove('student.dat')
    os.rename('newstudent.dat','student.dat')
                
opt=input('Enter n or r if you want to delete records by name or rollno : ')
if opt.lower()=='n':
    deletename()
elif opt.lower()=='r':
    deleterollno()
else:
    print("wrong entry")
'''
OUTPUTS

output 1

Enter n or r if you want to delete records by name or rollno : n
Enter the name of the student whose record you want to delete: ram

Remaining Records : 

(2, 'raja', 90)
(3, 'rahul', 78)
(4, 'rajesh', 88)
(5, 'Ram', 69)


output 2

Enter n or r if you want to delete records by name or rollno : r
Enter the rollno of the student whose record you want to delete: 4

Remaining Records : 

(2, 'raja', 90)
(3, 'rahul', 78)
(5, 'Ram', 69)


output 3

Enter n or r if you want to delete records by name or rollno : r
Enter the rollno of the student whose record you want to delete: 1
1 rollno not found.


output 4

Enter n or r if you want to delete records by name or rollno : n
Enter the name of the student whose record you want to delete: aditi
aditi not found.


output 5

Enter n or r if you want to delete records by name or rollno : l
wrong entry
'''
