mysql> delete * from doctor where department='cardiology';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '* from doctor where department='cardiology'' at line 1
mysql> delete doctor where department='cardiology';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where department='cardiology'' at line 1
mysql> delete table doctor where department='cardiology';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table doctor where department='cardiology'' at line 1
mysql> delete from doctor where department='cardiology';
Query OK, 2 rows affected (0.06 sec)

mysql> notee
