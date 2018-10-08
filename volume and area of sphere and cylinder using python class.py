import math                             # import necessary library

class Sphere:                           # Create a class

    def __init__(self,radius):           # Define a constructor
        self.radius=radius
        self.volume=0                    # Define veriables
        self.area=0

    def Volume(self):                    # Define a method to get volume
        self.volume =    (4/3)*math.pi*(self.radius*
                                        self.radius*
                                        self.radius)
        return self.volume


    def Area(self):                         # define a method to get area
        self.area= 4 * math.pi * (self.radius * self.radius)
        return self.area



class Cylinder(Sphere):                     # Define a class Cylinder


    def __init__(self,radius,height):       # define a constructor
        super().__init__(radius)
        self.height=height

    def Volume(self):                       # define method to get volume
        self.volume= math.pi * (self.radius * self.radius) * self.height
        return self.volume

    def Area(self):                         # define a method to find area
        self.area= (2 * math.pi * self.radius * self.height) + (2 * math.pi* (self.radius* self.radius) )
        return self.area

def main():                                 #Define a main

    sphere=Sphere(2)
    print('Sphere area:',sphere.Area())
    print('Sphere volume:',sphere.Volume())
    cyclinder = Cylinder(1,2) #inputs may change
    print('Cyclinder area:',cyclinder.Area())
    print('Cyclinder volume:',cyclinder.Volume())

if __name__=='__main__':
    main()





