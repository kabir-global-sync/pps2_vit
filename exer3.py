import re
def isPrime(n):
    prime_flag=0
    if(n > 1):
        for i in range(2, n//2 + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def isPalindrome(s):
    return s == s[::-1]

def complexPattern(com):
    pattern=r".*\d+j"
    if re.match(pattern,com):
        return True
    else:
        return False


lst=eval(input())

temp=[];prime=False;palindrome=False

if lst==[111]:
    print("Invalid Data")
else:
    for i in range(len(lst)):
        if complexPattern(str(lst[i])):
            continue
        elif str(lst[i]).isalpha() and isPalindrome(lst[i].lower()):
            palindrome=True
        elif str(lst[i]).isdigit() and isPrime(int(lst[i])):
            prime=True

    if prime and not palindrome:
        for i in lst:
            if complexPattern(str(i)):
                temp.append(complex(i.imag,i.real))
            elif str(i).isalpha():
                temp.append(i[::-1])
            else:
                temp.append(i)
        print(temp)
    elif palindrome and not prime:
        for i in lst:
            if complexPattern(str(i)):
                temp.append(complex(i.real,-i.imag))
            elif str(i).isdigit():
                temp.append(-int(i))
            elif str(i)=='-1':
                temp.append(1)
            else:
                temp.append(i)
        print(temp)
    elif palindrome and prime:
        print(lst[len(lst)//2])

    elif not palindrome and not prime:
        for i in lst:
            if str(i).isalpha():
                for j in i:
                    temp.append(j)
            else:
                temp.append(i)
        print(temp)
