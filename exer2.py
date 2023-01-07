import re

password=input()
password=tuple(password.split(','))
print(password)
pattern=re.compile('[a-z0-9A-Z]+[$#@]+')
flag=False

for i in password:
    if re.match(pattern,i) and 6<=len(i)<=12:
        print(i)
        flag=True
if not flag:
    print("invalid")

