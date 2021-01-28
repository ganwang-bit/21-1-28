#n=eval(input())
#ji=[]
#for i in range(n):
#    temp=input().split()
#    if eval(temp[0])==0:
#        ji.append(temp[1].lower())
#    elif eval(temp[0])==1:
#        if temp[1].lower() not in ji:
#            print("No")
#        else:
#            print("Yes")
n=eval(input())
jiplace={}
for i in range(n):
    temp=input().split()
    if temp[1] not in jiplace.keys():
        jiplace[temp[1]]={}
        jiplace[temp[1]][temp[0]]=eval(temp[2])
    else:
        if temp[0] not in jiplace[temp[1]].keys():
            jiplace[temp[1]][temp[0]]=eval(temp[2])
        else:
            jiplace[temp[1]][temp[0]]+=eval(temp[2])
m=sorted(jiplace.keys())
for j in m:
    print(j)
    l=sorted(jiplace[j].keys())
    for k in l:
        print("    "+"|----"+k+"("+str(jiplace[j][k])+")")
