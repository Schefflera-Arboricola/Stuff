mysql> select department,sum(charges) as 'total charges' from doctor group by department; 
+------------------+---------------+
| department       | total charges |
+------------------+---------------+
| ENT              |           550 |
| Gynecology       |           300 |
| Nuclear Medicine |           400 |
| Orthopedic       |           400 |
| Surgery          |          1400 |
+------------------+---------------+
5 rows in set (0.00 sec)

mysql> notee
