'''17. Design a Python application that fetches all the records from the  empl table of the emp database and displays those records who match the  job entered by the user.'''
import mysql.connector as ms
co=ms.connect(host='localhost',user='root',passwd='Aa1509',database='emp')
cur=co.cursor()
j=input('Enter job : ')
jo=j.upper()       
s='select * from empl where job=%s'%(jo,)
try:
    cur.execute(s)
    r=cur.fetchall()
    for i in r:
        print(i)
except:
    print('\nNo job',j,'found')
    
'''outputs

Enter job : 'clerk'
(Decimal('8369'), 'SMITH', 'CLERK', Decimal('8902'), datetime.date(1990, 12, 18), Decimal('800.00'), None, Decimal('20'))
(Decimal('8886'), 'ANOOP', 'CLERK', Decimal('8888'), datetime.date(1993, 1, 12), Decimal('1100.00'), None, Decimal('20'))
(Decimal('8900'), 'JATIN', 'CLERK', Decimal('8698'), datetime.date(1991, 12, 3), Decimal('950.00'), None, Decimal('30'))
(Decimal('8934'), 'MITA', 'CLERK', Decimal('8882'), datetime.date(1992, 1, 23), Decimal('90.00'), None, Decimal('10'))



Enter job : teacher

No job teacher found
'''
