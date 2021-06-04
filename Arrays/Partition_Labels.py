def partitionLabels(s):
    temp={c:i for i, c in enumerate(s)}
    # for i in temp.keys():
    #     print(i,temp[i])
    res=[]
    start,end=0,0
    for i,c in enumerate(s):
        print(i,c)
        end=max(end,temp[c])
        if i==end:
            res.append(end-start+1)
            start =i+1
    return res


a="ababcbacadefegdehijhklij"
ans=partitionLabels(a)
start =0
for i in ans:
    print(start)
    print(a[start:start+i])
    print("--"*20)
    start=start+i