def nameMerge(varScore,varDict):
    dic={}
    nm=""
    for i in varDict:
        if varScore.count(varDict[i])>1:
            for j in varDict:
                if varDict[j]==varDict[i]:
                    nm=nm+j+","
            nm=nm.rstrip(',')
            dic[nm]=varDict[i]
            nm=""
        else:
            dic[i]=varDict[i]
    dic=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
    return dic


ansKey={1:"A",2:"B",3:"B",4:"A",5:"C"}
t=int(input())
score={}
sortedScore=[]
hold=0
candid=['C1','C2','C3','C4','C5']
j=0
for _ in range(t):
    mark=list(map(str,input().split()))
    for i in range(len(mark)):
        if mark[i]==ansKey[i+1]:
            hold+=2
        elif mark[i]!="X":
            hold-=0.5
        else:
            pass
    score[candid[j]]=format(hold,'.2f');j+=1
    sortedScore.append(hold)
    hold=0
sortedScore.sort(reverse=True)
rankDict=nameMerge(sortedScore,score)

if sortedScore.count(0)==t:
    candid=""
    for i in rankDict:
        candid+=i+","
    candid=candid.rstrip(",")
    print('1'+" "+str(candid)+" "+'0.00')
else:
    hold=0
    for i in rankDict:
        hold+=1
        print(hold," ",i," ",rankDict[i])
