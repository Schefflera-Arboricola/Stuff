'''Q12. Write a program to display the employee’s data whose employee id has been given by the user from the file “Empl.csv” created in Q11.'''
import csv
f=open('empl.csv','r',newline='\r\n')
r=csv.reader(f)
s=0
id=input('Enter Employee id : ')
for i in r:
    if id==i[0]:
        print('required record',i)
        s=1
        break
if s==0:
    print('id not found')
f.close()

'''outputs

Enter Employee id : 0020
required record ['0020', 'rashi', 'manager', '50000']

Enter Employee id : 0010
required record ['0010', 'ray', 'designer', '50000']

Enter Employee id : 4000
id not found
'''
