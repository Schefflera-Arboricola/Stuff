'''Q13. Write a program to read the file “Empl.csv” and creates another file “newemp.csv” with the delimiter as semi colon ‘;’. Also display the contents of the new file.'''
import csv
f=open('empl.csv','r',newline='\r\n')
f1=open('newemp.csv','w')
r=csv.reader(f)
w=csv.writer(f1,delimiter=';')
for i in r:
    w.writerow(i)
f.close()
f1.close()

f=open('newemp.csv','r',newline='\r\n')
r=csv.reader(f)
print('Contents : ')
for i in r:
    print(i)
f.close()

'''outputs

Contents : 
['0010;ray;designer;50000']
['0020;rashi;manager;50000']
['0030;rajiv;writer;40000']
'''
