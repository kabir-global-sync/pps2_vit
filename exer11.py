import math
'''
50% = [1-400] + percentage
>50% = [(500+percentage)-1000]
    <>ramanujan number: number equals sum of two cubes
    <>perfect square
'''
# newLst=[513, 520, 730, 737] #ramanujan numbers between 500-1000
#perfectLst=[6,28] #perfect numbers
lst=[]
for i in range(1,101):
    x=int(math.sqrt(i))
    if x*x==i:
        lst.append(i)

print(lst)
for i in range(1,101):
    print(i**2,end=" ")