'''QUESTION:
Write a program to make functions to find the number of uppercase letters, lowercase letters and digits in a string passed as an argument to these functions. Name the functions as noofupper(), nooflower(), noofdigits() and call them in the program to generate a statistical table of the above.'''


def noofupper(x):
    c=0
    for i in x:
        if i.isupper()==True:
            c+=1
    return c

def nooflower(x):
    c=0
    for i in x:
        if i.islower()==True:
            c+=1
    return c

def noofdigit(x):
    c=0
    for i in x:
        if i.isdigit()==True:
            c+=1
    return c

n=input("Enter a string : ")
a,b,c=(noofupper(n),nooflower(n),noofdigit(n))
print("\nNumber of UPPERCASE letters : ",a,"\nNumber of LOWERCASE letters : ",b,"\nNumber of DIGITS : ",c)

'''
OUTPUTS

Enter a string : We ALL can SAVE the World from coronavirus in 2020.

Number of UPPERCASE letters :  9 
Number of LOWERCASE letters :  28 
Number of DIGITS :  4


Enter a string : I was born on 15th September,2003.

Number of UPPERCASE letters :  2 
Number of LOWERCASE letters :  19 
Number of DIGITS :  6

'''
