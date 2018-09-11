"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""
# Define intital text to display on screen
text= """
----------------------------
Welcome to Robot Software 
Please Enter 
l/L for left 
r/R fro Right 
u/U for up
d/D for down
Enter your Input below
-----------------------------
"""

# Define the function for robot

def is_round(i):
    x=0
    y=0
    # set inital position as 0,0
    # whatever strig user enter break it and fetch line by line to software

    for i in i:
        # check for r if yes inc x

        if i == "r":
            x=x+1
        # check for l if yes dec  x
        if i == "l":
            x=x-1
        # check for u if yes inc y
        if i == "u":
            y=y+1
        # check for u if yes dec y
        if i == "d":
            y=y-1
        # return the value of x and y check if its back and return True or False
    return x==0 and y==0

# Take input from userp and convert into lower
user=input(text).lower()
#  pass input to function and return true or false
path = is_round(user)
print(path)
# check condition if its at start or made circle
if path == True:
    print("You Are back at initial position")
    print("True")
else:
    print("You are not back at same position from where you have started ")
    print("False")










