'''
1.check all letters are lowercase
2.word[i] is lexically smaller than word[n-1-i] for all even i from 0 to len(word)/2
3.word[i] is lexically greater than word[n-1+i] for all odd i from 0 to len(word)/2
'''

'''
take user input of sentence
remove: {a,an,and,the,this,is,in,was,that,are,were}
search all magic words
convert non-magic words to magic, remove lexically large letter
determine the minimal length magic word(l)
make matrix of (lxl) from the sentence row-wise
rotate the outermost letters l times anti-clockwise
print list of magic words from each column
'''
import numpy as np
import rotate2 as rot
charD=list('abcdefghijklmnopqrstuvwxyz')
lex = dict(zip(charD,[i for i in range(26)]))

def magicWord2(wd):
    leve=[(wd[i],wd[len(wd)-i-1]) for i in range(len(wd)//2) if i%2==0 and lex[wd[i]]<lex[wd[len(wd)-i-1]]]
    if leve:
        return True

def magicWord(wd,con):
    global magicWds
    eveLex=False
    oddLex=False
    if con==1:
        leve=[(wd[i],wd[len(wd)-i-1]) for i in range(len(wd)//2) if i%2==0 and lex[wd[i]]<lex[wd[len(wd)-i-1]]]
        lodd=[(wd[j],wd[len(wd)-1-j]) for j in range(1,len(wd)//2) if j%2!=0 and lex[wd[j]]>lex[wd[len(wd)-j-1]]]
        if not leve or not lodd:
            return False #not a magical word
        else:
            return True #magical word
    else:
        leve=[(wd[i],wd[len(wd)-i-1]) for i in range(len(wd)//2) if i%2==0 and lex[wd[i]]<lex[wd[len(wd)-i-1]]]
        
        if leve:
            ln=min(list(len(wd[wd.index(leve[i][0]):wd.index(leve[i][1])+1]) for i in range(len(leve))))
            subStr=[]
            for j in range(len(wd)-ln):
                if magicWord2(wd[j:j+ln+1]):
                    magicWds.append(wd[j:j+ln+1])
                    break
        else:
            return False

user = input("Enter sentence:")
temp=user.split(" ")
user=""
for i in temp:
    if i not in['a','an','and','the','this','is','in','was','that','are','were']:
        user+=i+" "
    user.strip()
magicWds=[] #contains all the magic words
for i in user.split():
    if magicWord(i,1):
        magicWds.append(i)
    else:
        magicWord(i,2)

matrix=[]
order = len(min(magicWds,key=len))
for i in range(order):
    matrix.append(list(magicWds[i][0:order]))

matrix=np.array(matrix)
for _ in range(order):
    rot.rotate_matrix(matrix)

sub=[]
for m in range(order):
    col=""
    for n in matrix[:,m:m+1]:
        col+=n[0]
    if magicWord2(col):
        sub.append(col)
        col=""
    else:
        col=""

print(sub)