import logging

data=[]
clean_data=[]
clean_data_1=[]


try:
    with open('soumil.txt','r') as fname:
        data=fname.readlines()
        print(data)
        for x in data:
            print(x.strip())
            val=x.strip()
            clean_data.append(val)
            clean_data_1=list(filter(''.__ne__,clean_data))
            
except FileNotFoundError:
    print("File Not Found")



    print(data)
    print(len(data))
    print(clean_data)
    print(len(clean_data))
    print(clean_data_1)
    print(len(clean_data_1))

