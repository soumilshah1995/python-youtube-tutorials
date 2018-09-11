"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""

text="""
Welcome to 2's compliment software 
please Enter Decimal number
example:- 4

"""



def findComplement(num):

    numWord=bin(num) #converts decimal number to binary representation
    numWord=numWord[2:] #trims initial 2 chars from the string
    length=len(numWord) #calculates the length of the string
    i=0
    res=''
    #Following loop would iterate for every char to convert it.

    while i<length:
        if numWord[i]=='1':
            res+='0'
        else:
            res+='1'
        i+=1
    return res



def find2sComplement(num):
    # call the 1 comp
    num_1=findComplement(num)
    # define 001 to add it
    num_2="0001"
    #perform 2 comp
    c = bin(int(num_1,2) + int(num_2,2))

    z=c[2:]
    # call bin to dec and convert value
    temp=binaryToDecimal(int(z))

    return (c)



# Function calculates the decimal equivalent
# to given binary number

def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    print("2 compliment  Decimal Value ",decimal)



user=int(input(text))
print("Decimal number is {} and Binary is {}".format(user,bin(user)))
print("1's compliment is {}".format(findComplement(user)))
print("2's Compliment {}".format(find2sComplement(user)))