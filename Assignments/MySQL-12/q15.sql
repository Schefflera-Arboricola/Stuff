mysql> select name,department,charges*7 as 'charges per week' from doctor;
+---------+------------------+------------------+
| name    | department       | charges per week |
+---------+------------------+------------------+
| Sandeep | Surgery          |             4900 |
| Ravina  | Orthopedic       |             1400 |
| Karan   | Orthopedic       |             1400 |
| Tarun   | Surgery          |             4900 |
| Zubin   | ENT              |             1750 |
| Ketaki  | ENT              |             2100 |
| Zareen  | Gynecology       |             2100 |
| Shailya | Nuclear Medicine |             2800 |
+---------+------------------+------------------+
8 rows in set (0.00 sec)

mysql> notee
