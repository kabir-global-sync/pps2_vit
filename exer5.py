def number(letter):
    if letter in set1:
        return 1
    elif letter in set2:
        return 2
    elif letter in set3:
        return 3
    elif letter in set4:
        return 4
    elif letter in set5:
        return 5
    elif letter in set6:
        return 6
    elif letter in set7:
        return 7
    elif letter in set8:
        return 8
    elif letter in set9:
        return 9
def splitter(num):
    num=str(num)
    Sum=0
    for i in num:
        Sum+=int(i)
    return Sum
set1={'A','J','S'}
set2={'B','K','T'}
set3={'C','L','U'}
set4={'D','M','V'}
set5={'E','N','W'}
set6={'F','O','X'}
set7={'G','P','Y'}
set8={'H','Q','Z'}
set9={'I','R'}
destiny=0
soul=0
dream=0
vowel={'A','E','I','O','U'}
name=input()
name=name.replace(" ","").upper()

for i in name:
    destiny+=number(i)

destiny=splitter(destiny)
for i in name:
    if i in vowel:
        soul+=number(i)
soul=splitter(soul)

for i in name:
    if i not in vowel:
        dream+=number(i)
dream=splitter(dream)
print(destiny)
print(soul)
print(dream)