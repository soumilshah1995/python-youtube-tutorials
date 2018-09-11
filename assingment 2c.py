"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""

'''
we are asked to print the following pattern
    **
   ****
  ******
 ********
 
'''

# take input of number of rows
n=int(input("Enter Number of Rows :-"))

# iterate over number of rows
for i in range(1,n+1):
    # iterate over to print spaces
    for j in range(0,n-i):
        # print spaces
        print(end=" ")
        # iterate to print star
    for j in range(0,2*i):
        print(end="*")
        # end line
    print()




