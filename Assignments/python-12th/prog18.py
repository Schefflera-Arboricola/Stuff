'''18. Design a Python application that fetches only those records from the  Doctor table (created in MySQL for practical queries) of the Hospital  database whose department is cardiology and displays them. '''
import mysql.connector as ms
co=ms.connect(host='localhost',user='root',passwd='Aa1509',database='doc')
cur=co.cursor()
s='select * from doctor where department=\'cardiology\''
cur.execute(s)
r=cur.fetchall()
for i in r:
    print(i)
'''
output

(Decimal('7'), 'Ankita', Decimal('29'), 'Cardiology', '20/02/07', Decimal('800'), 'F')
(Decimal('9'), 'Kush', Decimal('19'), 'Cardiology', '13/01/07', Decimal('800'), 'M')

'''
