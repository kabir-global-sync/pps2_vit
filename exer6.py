import re
patter='[A-Z]{5}[0-9]{4}[A-Z]$'

user=input()
if re.match(patter,user):
    print("Valid")
else:
    print("Invalid")
