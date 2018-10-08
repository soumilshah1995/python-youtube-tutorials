# import The necessary Library
import ast
import logging


class Stack(object):                # Define a class STACK

    def __init__(self):             # Define a Constructor
        #Debugging
        #print('stack')
        self.items = []
        self.temp=[]

    def isEmpty(self):              # Check if list is empty
        return self.items == []

    def push(self, item=0):          # Define a push dont use append i did that
        self.temp=self.items + [item]
        self.items=self.temp

    def pop(self):                    # Define a pop dont use POP i did it
        n = self.items[0]
        del self.items[0]
        return n

    def peek(self):
        return self.items[len(self.items)-1]

    def size_stack(self):              # Size of Stack
        return len(self.items)

    def val_print(self):                # Values inside Stack for Debugging
        print(self.items)
        return self.items

#--------------------------------------------------------------------------------

class Node(object):                     # Define a class Node

    def __init__ (self, d, n = None):   # include Constructor
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

#----------------------------------------------------
class LinkedList (object):              # Define a class Link Node

    def __init__(self, r = None):
        self.root = r
        self.size = 0
        print('Linklist init')

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

#----------------------------------------------------------

class Structure(Stack,LinkedList):      # Define a class Structure

    def __init__(self):
        Stack.__init__(self)
        LinkedList.__init__(self)

    def compute(self):                    # Define a method  to check String or int or float
        if isinstance(self, int):
            return int

        if isinstance(self,str):
            return str

        if isinstance(self,float):
            return float
# ----------------------------------------------------------------

def main():
    data=[]                     # data that comes from File
    clean_data=[]               # data removing blank lines or spaces
    clean_data_1=[]             # After removing any blank line or space

    # Open File
    try:                         # Check if File if its there
        with open('soumil.txt','r') as fname:
            data=fname.readlines()
            print("Data From File",data)        # print data you rread from File

            for x in data:                       # Remove all blank lines and spaces
                val=x.strip()
                clean_data.append(val)
                clean_data_1=list(filter(''.__ne__,clean_data))

        print("After removing White space and new lines Data",clean_data_1)


        # Start Logic
        s=Structure()
        #d=LinkedList()
        for x in clean_data_1:          # Iterate over clean data
            #print(x)
            #print(type(x))
            try:
                value=ast.literal_eval(x)    # TRY AND SEE if its int or float
                # print(type(value))         # push
                s.push(x)
                print("Push Numeric Data",x)
            except:
                # print('This is string ')

                if isinstance(x,str):       #Check for string
                    # print(type(x))
                    s.add(x)                 # ADD TO LINK NODE
                    print("Link Node Add Data add",x)

        print("size="+str(s.get_size()))
        s.val_print()
        print("Pop")
        s.pop()
        s.val_print()
        s.remove(1)
        print("size of lINK Node ="+str(s.get_size()))

    except FileNotFoundError:           # IF FILE NOT THERE PRINT MESSAGE
        print('File Not Found')

if __name__ == '__main__':
    main()