"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""

'''
we are asked to print the following pattern
*
**
***
****
*****
'''
# Take input from user how many rows we require
n=int(input("Enter No of Rows to Print "))

# iterate over that number of rows
for i in range(1,n+1):
    # iterate  for stars
    for j in range(0,i):
        print(end="*")
        # after printing star go new line
    print()



