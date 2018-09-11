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
# input number of rows from user
n=int(input("Enter Number of Rows :"))

# iterate over number of rows
for i in range(1,n+1):
    # iterate to print spaces and decremeent space after each time
    for j in range(0,n-i):
        # print space
        print(end=" ")
        # iterate to print stars
    for j in range(0,i):
        # print stars
        print(end="*")
        # end and go to new line
    print()
