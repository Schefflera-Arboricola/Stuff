'''20.  Design a Python application that increases the charges by 100 of the  doctors of ‘Surgery’ department in the table Doctor of the Hospital  database. Also display all the records. '''
import mysql.connector as ms
co=ms.connect(host='localhost',user='root',passwd='Aa1509',database='doc')
cur=co.cursor()
s='update doctor set charges=charges+100 where department=\'surgery\''
cur.execute(s)
s1='select * from doctor'
cur.execute(s1)
r=cur.fetchall()
for i in r:
    print(i)
'''
output

(Decimal('1'), 'Sandeep', Decimal('65'), 'Surgery', '23/02/07', Decimal('400'), 'M')
(Decimal('2'), 'Ravina', Decimal('24'), 'Orthopedic', '20/01/07', Decimal('200'), 'F')
(Decimal('3'), 'Karan', Decimal('45'), 'Orthopedic', '19/02/07', Decimal('200'), 'M')
(Decimal('4'), 'Tarun', Decimal('12'), 'Surgery', '01/01/07', Decimal('400'), 'M')
(Decimal('5'), 'Zubin', Decimal('36'), 'ENT', '12/01/07', Decimal('250'), 'M')
(Decimal('6'), 'Ketaki', Decimal('16'), 'ENT', '24/02/07', Decimal('300'), 'F')
(Decimal('7'), 'Ankita', Decimal('29'), 'Cardiology', '20/02/07', Decimal('800'), 'F')
(Decimal('8'), 'Zareen', Decimal('45'), 'Gynecology', '22/02/07', Decimal('300'), 'F')
(Decimal('9'), 'Kush', Decimal('19'), 'Cardiology', '13/01/07', Decimal('800'), 'M')
(Decimal('10'), 'Shailya', Decimal('31'), 'Nuclear Medicine', '19/02/07', Decimal('400'), 'F')
'''
