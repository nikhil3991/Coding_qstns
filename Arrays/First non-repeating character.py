MAX = 256

def firstnonrepeating():
    repeated =[False]*256
    DLL =[]
    str = "geeksforgeeks"
    for i in range(len(str)):
        x =str[i]
        print("reading char",x)
        if not repeated[ord(x)]:
            if x  not in DLL:
                DLL.append(x)
            else:
                DLL.remove(x)
                repeated[ord(x)] =True
        if len(DLL)!=0:
            print("First non repeating char is:")
            print(DLL[0])

firstnonrepeating()




