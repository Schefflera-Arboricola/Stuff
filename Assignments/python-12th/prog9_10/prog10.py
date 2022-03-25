#correction needed
'''Q10. Write a function to update the file ‘Item.dat’ defined in Q9 by updating the itemname and price of items for an itemid. Use this function in a program for updating the file.'''
import os
import pickle as p
def update():
    itemid=int(input('Enter the itemid of the product you want to update the record : '))
    f=open('Item.dat','rb')
    f1=open('Itemnew.dat','wb')
    found=False
    try:
        while True:
            rec=p.load(f)
            if rec['Itemid']==itemid:
                found=True
                name=str(input('Enter the new product name : '))
                price=int(input('Enter the new product price : '))
                rec={'Itemid': itemid, 'Itemname': name, 'Price': price}
                print('\nRecord UPDATED!!!')
            p.dump(rec,f1)
            
    except :
        f.close()
        f1.close()
    if found==False:
        print(itemid,"id not found.")
    os.remove('Item.dat')
    os.rename('Itemnew.dat','Item.dat')

update()

'''OUTPUTS

Enter the itemid of the product you want to update the record : 1121
Enter the new product name : Glass Colours
Enter the new product price : 290

Record UPDATED!!!


Enter the itemid of the product you want to update the record : 4563
4563 id not found.
'''
