'''17. Design a Python application that fetches all the records from the  empl table of the emp database and displays those records who match the  job entered by the user.'''
import mysql.connector as ms
co=ms.connect(host='localhost',user='root',passwd='Aa1509',database='emp')
cur=co.cursor()
cur.execute('select * from empl')
j=input('Enter job : ')
r=cur.fetchall()
m=False
for i in r:
    if i[2].upper()==j.upper():
        print(i)
        m=True
if m!=True:
    print('\nNo job',j,'found')
    
'''outputs

Enter job : teacher

No job teacher found


Enter job : manager
(Decimal('8566'), 'MAHADEVAN', 'MANAGER', Decimal('8839'), datetime.date(1991, 4, 2), Decimal('2985.00'), None, Decimal('20'))
(Decimal('8698'), 'BINA', 'MANAGER', Decimal('8839'), datetime.date(1991, 5, 1), Decimal('2850.00'), None, Decimal('30'))
(Decimal('8882'), 'SHIAVNSH', 'MANAGER', Decimal('8839'), datetime.date(1991, 6, 9), Decimal('2450.00'), None, Decimal('10'))

'''
