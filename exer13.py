import csv
nullCount=0
lineCount=0
with open('diabetes.csv') as f:
    obr=csv.reader(f)
    for i in obr:
        nullCount+=i.count('0')
        lineCount+=1

with open('exer13_output.txt','a') as of:
    of.write(str(nullCount)+'\n')
    of.write(str(lineCount))