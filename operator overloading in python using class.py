from operator import add                        #   import all library

class Compute:                                  #   Define a class

    def __init__(self,data):                    # Define a constructor
        self.data =data

    def __add__(self, other):                   #   define a method overloading

                                                #   check data for int

        if isinstance(self.data,list) and isinstance(other.data,list):
            return list(map(add,self.data,other.data))

                                                #   check data for tuple

        elif isinstance(self.data,tuple) and isinstance(other.data,tuple):
            return tuple(map(add,self.data,other.data))

                                                # Check for Dict

        elif isinstance(self.data,dict) and isinstance(other.data,dict):
            dict1 = self.data
            dict2 = other.data
            for k in dict2:
                if k in dict1:
                    dict1[k] += dict2[k]
                else:
                    dict1[k] = dict2[k]
            return dict1
        else:
            print('Given data is not List,Tuple, Dictionary or input have different dataTypes ')

def main():                                     #   Define main
    c1 = Compute([1,2,3,4])
    c2 = Compute([3.3,4,5,1.2])
    print(c1+c2)

    c3 = Compute({1:'abc',3:'xyz',5:'test'})
    c4 = Compute({2:'test1',3:'test2',4:'test3'})
    print(c3+c4)


if __name__ == '__main__':
    main()



