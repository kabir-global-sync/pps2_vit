lst="[[1,2],'a','hello']"
temp=[]
if lst.count('[')>=2:
    for i in lst:
        if i!='[' and i!=']' and i!=',' and i!="'":
            temp.append(i)
else:
    print("cannot unpacked")

print(len(temp))