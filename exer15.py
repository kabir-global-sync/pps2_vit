def calculateFare(destination,l):
    if destination=="Hosur":
        fare=75
    elif destination == "Vaniyambadi":
        fare=250
    elif destination == "Vellore":
        fare=500
    elif destination == "Walaja":
        fare=600
    elif destination == "Chennai":
        fare=750
    t=0
    for i in l:
        if i[1]<60:
            t+=fare
        elif i[1]>=60:
            t+=(fare-(fare*(10/100)))
    return t

def refund(fare,d):
    if d>=20:
        r=fare
    elif d<20 and d>=14:
        r=fare*(90/100)
    elif d<14 and d>=7:
        r=fare*(80/100)
    elif d<7 and d>=4:
        r=fare*(50/100)
    elif d<4:
        r="No refund"
    return r
reservation=open("reservation.txt","w")
regular=12
tatkal=3
f1=[]
f=open("credentials.txt","r")
for each in f:
    f1.append(each)
a=f1[0]
b=f1[1]
username=input()+'\n'
password=input()
if username==a and password==b:
    while True:
        mainMenu=int(input())
        if mainMenu==1:
            booking=input().upper()
            if booking=="A":
                no_of_passenger_A = int(input())
                l=[]
                for i in range(no_of_passenger_A):
                    details=input().split(",")
                    name=details[0]
                    age=int(details[1].lstrip())
                    l1=[name,age]
                    l.append(l1)
                destination_A=input()
                dateOfJourney_A=input()
                tf_A=int(calculateFare(destination_A,l))
                regular = regular-no_of_passenger_A
                
                if regular>=0:
                    print("remaining seats:",file=reservation)
                    print("Regular= "+str(regular),file=reservation)
                    print("Tatkal= "+str(tatkal),file=reservation)
                    print("Passenger Name - Age - Source - Destination - Seat No",file=reservation)
                    searNo=15
                    for i in l:
                        print(i[0]+" - "+str(i[1])+" - "+"Bengaluru"+" - "+destination_A+" - "
                        +str(seatNo),file=reservation)
                        seatNo-=1
                    print("Date of Journey: "+dateOfJourney_A,file=reservation)
                    print("Total fare = Rs. "+str(tf_A),file=reservation)
                else:
                    print("Insufficient seats!! Try for other dates...",file=reservation)
                print("\n",file=reservation)
            elif booking=="B":
                no_of_passenger_B = int(input())
                m=[]
                for i in range(no_of_passenger_B):
                    details = input().split(",")
                    name=details[0]
                    age = int(details[1].lstrip())
                    m1=[name,age]
                    m.append(m1)
                destination_B=input()
                dateOfJourney_B=input()
                tf_B=int(calculateFare(destination_B,m))+no_of_passenger_B*100
                tatkal = tatkal-no_of_passenger_B
                if tatkal>=0:
                    print("Remaining seats:",file=reservation)
                    print("Regular = "+str(regular),file=reservation)
                    print("Tatkal = "+str(tatkal),file=reservation)
                    print("Passenger Name - Age - Source - Destination - Seat No",file=reservation)
                    seatNo=12
                    for i in m:
                        print(i[0]+" - "+str(i[1])+" - "+"Bengaluru"+" - "+destination_B+" - "
                        +str(seatNo),file=reservation)
                        seatNo-=1
                    print("Date of Journey: "+dateOfJourney_B,file=reservation)
                    print("Total fare = Rs. "+str(tf_B),file=reservation)
                else:
                    print("Insufficient seats!! Try for other dates...",file=reservation)
                print("\n",file=reservation)
        elif mainMenu==2:
            noOfCancellation = 0
            name=input()
            age=int(input())
            dateOfCancellation = input()
            n = [name,age]
            n1=[n]
            if n in l:
                d=int(dateOfJourney_A[:1]-int(dateOfCancellation[:1]))
                fare=calculateFare(destination_A,n1)
                r=refund(fare,d)
                regular+=1
                noOfCancellation+=1
                print("Remaining seats:",file=reservation)
                print("Regular = "+str(regular),file=reservation)
                print("Tatkal = ",str(tatkal),file=reservation)
                print("No. of passengers to cancel = "+str(noOfCancellation),file=reservation)
                print("Cancelled passenger Name = "+name,file=reservation)
                print("Cancelled passenger Age = "+str(age),file=reservation)
                print("Refund Amount = Rs. "+str(r),file=reservation)
                print("Cancellation Charge = Rs. "+str(fare-r),file=reservation)
                print('\n',file=reservation)
            if n in m:
                d=int(dateOfJourney_B[:2])-int(dateOfCancellation[:2])
                fare=calculateFare(destination_B,n1)+100
                r=refund(fare,d)
                if r!="No refund":
                    cancellation_charge = fare-r
                else:
                    cancellation_charge = "No cancellation charge"
                tatkal+=1
                noOfCancellation+=1
                print("Remaining seats:",file=reservation)
                print("Regular = "+str(regular),file=reservation)
                print("Tatkal = ",str(tatkal),file=reservation)
                print("No. of passengers to cancel = "+str(noOfCancellation),file=reservation)
                print("Cancelled passenger Name = "+name,file=reservation)
                print("Cancelled passenger Age = "+str(age),file=reservation)
                print("Refund Amount = Rs. "+str(r),file=reservation)
                print("Cancellation Charge = Rs. "+str(fare-r),file=reservation)
                print('\n',file=reservation)
        else:
            break
else:
    print("Invalid Credentials",file=reservation)