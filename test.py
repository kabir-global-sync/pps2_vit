import csv

t=1990
with open('testcsv.csv','a',newline="") as f:
    obj = csv.writer(f)
    obj.writerow(["vennela","gargi","anima"])
    obj.writerow(["Total",t])
