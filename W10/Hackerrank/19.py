from collections import *
N= input()
d= OrderedDict()
for i in range(N):
    item = raw_input().split()
    itemPrice= int(item[-1])
    itemName= " ".join(item[:-1])
    if d.get(itemName):                      
       d[itemName] += itemPrice
    else:
       d[itemName] = itemPrice
for i in d.keys():
    print i, d[i]