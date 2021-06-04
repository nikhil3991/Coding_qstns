import string
def Solve(s):
    n=len(s)
    op=[]
    emp_name = s[:-6]
    mod_name=emp_name.lower()
    id = s[-6:]
    print(emp_name)
    print(id)
    if mod_name[0] == mod_name[-1]:
        op.append(len(emp_name))
    val=0
    for i in range(6):
        val+=int(id[i])
    if val%2==0:
        op.append(str(val))
        op.append('E')
    if int(id[-2])==int(id[-1]):
        op.append(id[-1])
    count=0
    for i in range(len(emp_name)):
        if emp_name[i]=='a':
            count+=1
            if count>1:
                break
    if count>1:
        op.append('a')
    if s[0]=='A' and int(s[-1])==9:
        op.append('A9')
    print(op)
    if len(op)==0:
        return 'X'
    else:
        return "".join(str(i) for i in op)


s= "AaYuasha778699"
print(Solve(s))