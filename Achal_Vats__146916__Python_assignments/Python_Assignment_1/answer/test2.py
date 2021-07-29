f=open("data1.txt","r")
items=[]
duplicate= []
unique=[]
items=f.read().split()
items=[word.replace("#"," ") for word in items]
items=items[1:]
print("LIST")
for i in items:
    print(i)
for item in items:
    count=0
    for i in range (1,len(items)):
        if(item == items[i]):
            count=count+1
    if(count>1):
        duplicate.append(item)
    #print(items[4])

print("#############")
print("DUPLICATE")
mydup=set(duplicate)    
for ele in mydup:
    print(ele)

print("##############")

print("UNIQUE")

for item in items:
    count=0
    for i in range (1,len(items)):
        if(item == items[i]):
            count=count+1
    if(count<2):
        unique.append(item)
#myset=set(items)
#for elements in myset:
 #   print(elements)
for u in unique:
    print(u)

print("################")
      
      
      
print("SORTED")
mysorted=items
mysorted1=[]
for ele in mysorted:
    ele=ele[-5:]
    mysorted1.append(ele)
    

mysorted1.sort()
for i in mysorted1:
    print(i)    
