'''Q7. Write a program to create a binary file named ‘student.dat’ containing (rollno,name,marks)and write a function search() to search for a rollno in the file and display the details .Call the function in the program.'''
import pickle as p
def search():
    f=open('student.dat','rb')
    l=[]
    try:
        while True:
            rec=p.load(f)
            l+=[rec]
    except:
        f.close()
        
    print('Enter 0 to end')
    r=int(input('\nEnter the rollno to see the record : '))
    while r!=0:
        for i in l:
            if i[0]==r:
                print('Record : ',i)
                break
        else:
            print(r,"Rollno not found")
        r=int(input('\nEnter the rollno to see the record : '))
    print('End')

#<_main_>                
f=open('student.dat','wb')
l1,l2,l3,l4,l5=(1,'ram',99),(2,'raja',90),(3,'rahul',78),(4,'rajesh',88),(5,'Ram',69)
for i in [l1,l2,l3,l4,l5]:
    p.dump(i,f)
f.close()
search()

'''outputs

Enter 0 to end

Enter the rollno to see the record : 1
Record :  (1, 'ram', 99)

Enter the rollno to see the record : 7
7 Rollno not found

Enter the rollno to see the record : 2
Record :  (2, 'raja', 90)

Enter the rollno to see the record : 6
6 Rollno not found

Enter the rollno to see the record : 0
End

'''
