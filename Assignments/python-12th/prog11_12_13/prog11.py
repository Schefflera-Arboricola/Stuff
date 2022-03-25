'''Q11. Write a program to create a CSV file named “Empl.csv” to store employee data (Employee id, employee name, designation and salary) with the delimiter comma. Obtain the data from the user and write 3 records into the file. Also display the contents of the file'''
import csv
f=open('empl.csv','w')
w=csv.writer(f)
i=0
while i<3:
    id=input('\nEnter Employee id : ')
    m=input('Enter Employee name  : ')
    d=input('Enter designation  : ')
    s=int(input('Enter salary : '))
    w.writerow((id,m,d,s))
    i+=1
f.close()

f=open('empl.csv','r',newline='\r\n')
r=csv.reader(f)
print('\nContents : ')
for i in r:
    print(i)
f.close()

'''
output

Enter Employee id : 0010
Enter Employee name  : ray
Enter designation  : designer
Enter salary : 50000

Enter Employee id : 0020
Enter Employee name  : rashi
Enter designation  : manager
Enter salary : 50000

Enter Employee id : 0030
Enter Employee name  : rajiv
Enter designation  : writer
Enter salary : 40000

Contents : 
['0010', 'ray', 'designer', '50000']
['0020', 'rashi', 'manager', '50000']
['0030', 'rajiv', 'writer', '40000']
'''
