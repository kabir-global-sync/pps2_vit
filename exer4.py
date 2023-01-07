def dictionaryConvert(var):
    dic={}
    for i in var:
        for j in i:
            dic[j]=i[j]
    return dic
sameAge=False
sameName=False
wrongFmt=False
lst=eval(input())

record=dictionaryConvert(lst)
recordKeys=[i for i in record]
recordVal=[record[i] for i in record]
hold=0
for i in record:
    if recordVal.count(record[i])>1: #for age repetition
        sameAge=True
        hold=record[i]
        break
    elif recordKeys.count(i)>1:
        sameName=True
        break
    elif str(i).isdigit():
        wrongFmt=True
newRecord=[]
if sameAge:
    k=""
    for i in recordKeys:
        if record[i]==hold:
            k+=i
    newRecord.append({k:int(hold**(1/3))})
    for j in recordKeys:
        if j not in k:
            newRecord.append({j:record[j]})
    print(newRecord)
elif wrongFmt:
    for i in record:
        if str(i).isdigit():
            newRecord.append({record[i]:i})
        else:
            newRecord.append({i:record[i]})
    print(newRecord)
else:
    ar=""
    recordKeys=[]
    recordVal=[]
    for i in lst:
        for _ in i:
            recordKeys.append(_)
            recordVal.append(i[_])
    for j in range(len(recordKeys)):
        if recordKeys.count(recordKeys[j])>1:
            ar+=str(recordVal[j])
    for i in record:
        if recordKeys.count(i)>1:
            newRecord.append({i:int(ar)})
        else:
            newRecord.append({i:record[i]})
    print(newRecord)