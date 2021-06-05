from collections import defaultdict

a = defaultdict(list)
res=[]
projects = ['a','b','c','d','e','f','g','h']
dep = [['c','a'],['d','a'],['f','a'],['f','b'],['f','c'],['a','e'],['b','e'],['d','g']]
for i in projects:
    a[i] = []
for mem in dep:
    a[mem[1]].append(mem[0])
output = []

for i in a.keys():
    if a[i]==[]:
        res.append(i)
print(res)

if res[0]==None:
    print("Not possible")
else:
    while res:
        temp = res.pop(0)
        for i in a.keys():
            if temp in a[i]:
                a[i].remove(temp)
                if a[i]==[]:
                    res.append(i)

        output.append(temp)
if len(output)==len(projects):
    print(output)
else:
    print("Not possible")




