import csv
t=int(input()) #no. of customers
m=int(input()) #no. of products
with open('market.csv','a',newline="") as f:
    obj = csv.writer(f)
    totalAmt=0
    for _ in range(t):
        CustId=int(input())
        prod=input()
        qty=int(input())
        rate=int(input())
        totalPrice = qty*rate
        totalAmt+=totalPrice
        block=[CustId,prod,qty,rate,totalPrice]
        obj.writerow(block)
    obj.writerow(["Total Amount",totalAmt])


def func1(varId): #condition 1
    f=open('market.csv')
    obr=csv.reader(f)
    for row in obr:
        if row[0]==varId:
            print(row[4])
    f.close()

def func2(): #condition 2
    f=open('market.csv')
    obr=csv.reader(f)
    qtyList=[]
    for i in obr:
        qtyList.append(i[2])
    for j in obr:
        if j[2]==max(qtyList) or j[2]==min(qtyList):
            print(j[1])
    f.close()

def func3(): #condition 3
    f=open('market.csv')
    obr=csv.reader(f)
    qtyList=[]
    for i in obr:
        qtyList.append(i[2])
    for j in obr:
        if j[2]==max(qtyList):
            print(j[0])

func1(int(input('Enter customerID:')))
func2()
func3()