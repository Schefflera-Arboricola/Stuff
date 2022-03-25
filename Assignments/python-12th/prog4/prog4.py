'''Q4. Write a program to read a text file line by lineand display the words separated by a ‘$’sign.'''
# method 1 : printing all whole file with $ in place of all <space>
print('method 1\n')
file=open("facts.txt",'r')
a=' '
while a:
    a=file.readline()
    a='$'.join(a.split())
    print(a)
file.close()
print('\n\nmethod 2\n')
#method 2: printing words separated by $ in the file
file=open("facts.txt",'r')
r=file.read()
r=r.split('$')
for i in range(0,len(r)-1):
    j=r[i].split()
    j1=r[i+1].split()
    print((j[-1],j1[0]))
    
'''outputs
method 1

Fact$:$Design$of$bullet$train$was$inspired$by$kingfisher$bird.
email$address$1:$aditi$juneja2000@gmail.com
email$address$2:$aditi$j200@gmail.com
email$address$3:$aditi$juneja@gmail.com
email$address$4:$aditi$2000@gmail.com
price$:$$4000
special$character$in$email$id$:$$
'$'$means$dollar



method 2

('aditi', 'juneja2000@gmail.com')
('aditi', 'j200@gmail.com')
('aditi', 'juneja@gmail.com')
('aditi', '2000@gmail.com')
(':', '4000')
(':', "'")
("'", "'")

'''
