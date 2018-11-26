import pandas as pd

url=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(url[0][1])
states=[]

for x in url[0][1][1:]:
    states.append(x)

print(states)
