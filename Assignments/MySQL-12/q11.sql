mysql> select sex,avg(age) as 'avg age',avg(charges) as 'avg charges' from doctor;
+------+---------+-------------+
| sex  | avg age | avg charges |
+------+---------+-------------+
| M    | 34.2500 |    381.2500 |
+------+---------+-------------+
1 row in set (0.00 sec)

mysql> select sex,avg(age) as 'avg age',avg(charges) as 'avg charges' from doctor group by sex;
+------+---------+-------------+
| sex  | avg age | avg charges |
+------+---------+-------------+
| F    | 29.0000 |    300.0000 |
| M    | 39.5000 |    462.5000 |
+------+---------+-------------+
2 rows in set (0.00 sec)

mysql> notee
