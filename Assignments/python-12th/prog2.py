'''QUESTION:
Q2. Write a program to generate a random number in the range m-n where m and n are entered by the user.'''

import random as r
a,b=input("Enter the values of m and n : ").split(",")
a,b=int(a),int(b)
print("\nRandom number between",a,"and",b,"is",r.randint(a,b))

'''outputs

Enter the values of m and n : 34,789

Random number between 34 and 789 is 347



Enter the values of m and n : -50,0

Random number between -50 and 0 is -36

'''
