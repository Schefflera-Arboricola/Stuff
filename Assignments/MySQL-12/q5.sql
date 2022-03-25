mysql> select name,charges,age from doctor where sex=m;
ERROR 1054 (42S22): Unknown column 'm' in 'where clause'
mysql> select name,charges,age from doctor where sex='m';
+---------+---------+------+
| name    | charges | age  |
+---------+---------+------+
| Sandeep |     300 |   65 |
| Karan   |     200 |   45 |
| Tarun   |     300 |   12 |
| Zubin   |     250 |   36 |
| Kush    |     800 |   19 |
+---------+---------+------+
5 rows in set (0.00 sec)

mysql> notee;
