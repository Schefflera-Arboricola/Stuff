'''Q5. Write a program to create a copy a textfile‘Old.txt’by changing all instances of digits with a ‘#’signin the new file named as ‘New.txt’.'''

file=open('Old.txt','r')
file1=open('New.txt','w')
str=file.readlines()
for i in str:
    for j in i:
        if j.isdigit()==True:
            file1.write('#')
        else:
            file1.write(j)
file1.close()
file.close()

file=open('Old.txt','r')
s=file.read()
print('Old.txt\n',s)
file1=open('New.txt','r')
s=file1.read()
print('\nNew.txt\n',s)
file1.close()
'''outputs

Old.txt
 Pascle's triangle :
                    1
                  1 2 1
                 1 3 3 1
                1 4 6 4 1
              1 5 10 10 5 1
             1 6 15 20 15 6 1

New.txt
 Pascle's triangle :
                    #
                  # # #
                 # # # #
                # # # # #
              # # ## ## # #
             # # ## ## ## # #
             '''
