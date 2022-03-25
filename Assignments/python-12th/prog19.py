'''19. Design a Python application that deletes records from the Empl  table of database emp that are from deptno 20. Also display all the  remaining records. '''
import mysql.connector as ms
co=ms.connect(host='localhost',user='root',passwd='Aa1509',database='emp')
cur=co.cursor()
s='delete from empl where deptno=20'
cur.execute(s)
s1='select * from empl'
cur.execute(s1)
r=cur.fetchall()
for i in r:
    print(i)
'''
output

(Decimal('8499'), 'ANYA', 'SALESMAN', Decimal('8698'), datetime.date(1991, 2, 20), Decimal('1600.00'), Decimal('300.00'), Decimal('30'))
(Decimal('8521'), 'SETH', 'SALESMAN', Decimal('8698'), datetime.date(1991, 2, 22), Decimal('1250.00'), Decimal('500.00'), Decimal('30'))
(Decimal('8654'), 'MOMIN', 'SALESMAN', Decimal('8698'), datetime.date(1991, 9, 28), Decimal('1250.00'), Decimal('1400.00'), Decimal('30'))
(Decimal('8698'), 'BINA', 'MANAGER', Decimal('8839'), datetime.date(1991, 5, 1), Decimal('2850.00'), None, Decimal('30'))
(Decimal('8882'), 'SHIAVNSH', 'MANAGER', Decimal('8839'), datetime.date(1991, 6, 9), Decimal('2450.00'), None, Decimal('10'))
(Decimal('8839'), 'AMIR', 'PRESIDENT', None, datetime.date(1991, 11, 18), Decimal('5000.00'), None, Decimal('10'))
(Decimal('8844'), 'KULDEEP', 'SALESMAN', Decimal('8698'), datetime.date(1991, 9, 8), Decimal('1500.00'), Decimal('0.00'), Decimal('30'))
(Decimal('8900'), 'JATIN', 'CLERK', Decimal('8698'), datetime.date(1991, 12, 3), Decimal('950.00'), None, Decimal('30'))
(Decimal('8934'), 'MITA', 'CLERK', Decimal('8882'), datetime.date(1992, 1, 23), Decimal('90.00'), None, Decimal('10'))
'''
