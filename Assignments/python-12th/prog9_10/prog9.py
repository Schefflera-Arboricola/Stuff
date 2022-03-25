'''Q9. Write a program to create a file named ‘Item.dat’ having the following dictionary as a record {“Itemid”:value, “Itname”:value, “Price”:value}Also display all the records of the file.'''
import pickle as p
f=open('Item.dat','wb')
l={'Itemid': 1121,'Itemname': 'Ball Pens','Price': 10}
l1={'Itemid': 1122,'Itemname': 'Gel Pens','Price': 20}
l2={'Itemid': 1123,'Itemname': 'Calligraphy Pens','Price': 400}
l3={'Itemid': 1124,'Itemname': 'Brush Pens','Price': 100}
l4={'Itemid': 1125,'Itemname': 'Ink Pens','Price': 200}

p.dump(l,f)
p.dump(l1,f)
p.dump(l2,f)
p.dump(l3,f)
p.dump(l4,f)
f.close()

f=open('Item.dat','rb')
print('Records : \n')
try:
    while True:
        a=p.load(f)
        print(a)
except EOFError:
    f.close()
f.close()
'''
outputs

Records :

{'Itemid': 1121, 'Itemname': 'Ball Pens', 'Price': 10}
{'Itemid': 1122, 'Itemname': 'Gel Pens', 'Price': 20}
{'Itemid': 1123, 'Itemname': 'Calligraphy Pens', 'Price': 400}
{'Itemid': 1124, 'Itemname': 'Brush Pens', 'Price': 100}
{'Itemid': 1125, 'Itemname': 'Ink Pens', 'Price': 200}

'''
