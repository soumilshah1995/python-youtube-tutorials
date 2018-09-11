"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""
# Define Function to return morse code

def morse_code(n):
    # store morse code in keys
    keys=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.",
          "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    # store alphabet in a list
    alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # make a dictionary with alphabet as key and keys as value
    dictionary= dict(zip(alphabet,keys))
    #return the required morse code from dict using get function
    return dictionary.get(n)

# take input from user
answer=input("ENTER Word")
#store input in list
answer=list(answer)

word=""
# iterate over list to extract individual elements using for loop
for x in answer:
    # call function for that req string
    # join the string
    word = word + morse_code(x)

print(word)