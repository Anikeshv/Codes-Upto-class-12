#Armstrong no.
'''def isarmstorng(n):
    sm=0
    a=str(n)
    list(a)
    for i in a:
        sm=sm+int(i)**3
    if sm==n:
        return (n,"Is an Armstrong number")
    else:
        return (n,"Is not an Armstrong number")

n1=int(input("Enter the no."))
b=isarmstorng(n1)
print(b)'''

#Factorial
'''def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case _:
            return n*factorial(n-1)

n=int(input("Enter the no."))
a=factorial(n)
print(a)'''

#Percentage of five subjects
'''def percentage(a,b):
    return (a/b)*100
t1=eval(input("Enter the no of every sub.:"))
t2=eval(input("Enter the Max marks of each sub.:"))
a,b=sum(t1),sum(t2)
print(a,b)
c=percentage(a,b)
print("percentage:",c)'''

#Match case
'''# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 :
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)'''


#Global and local question
'''def EXP(N2):
    global N1
    N1,N2=N1+5,N2+10
    print(N1,N2,end=' ')
N1=10
EXP(N1)
print(N1)'''


'''def Call(P=40, Q=20):
    P=P+Q
    Q=P-Q
    print (P, '@', Q)
    return P

R= 200
S= 100
R=Call(R,S)
print (R, '@', S)
S= Call(S)
print (R, '@', S)'''


'''X = 50
def Alpha(num1):
    global X
    num1+=X
    X+=20
    num1=Beta(num1)
    return num1

def Beta(num1):
    global X
    num1+=X
    X+=10
    num1=Gamma(num1)
    return num1

def Gamma(num1):
    X=200
    num1+=X
    return num1

num=100
num=Alpha(num)
print(num,X)'''


'''#21
def countNow(PLACES):
    for i in PLACES.keys():
        if len(PLACES[i])>5:
            print(PLACES[i].upper())

PLACES={1:"Delhi",2:"London",3:"Paris",4:"New York",5:"Doha"}
countNow(PLACES)'''

'''#21 or 
def lenWords(STRING):
    tup=tuple()
    for i in STRING.split():
        tup+=(len(i),)
    print(tup)

STRING="Come let us have some fun"
lenWords(STRING)'''




'''L1=[500,800,600,200,900]
START=1
SUM=0
for c in range(START,4):
    SUM+=L1[c]
    print(c,":",SUM)
    SUM+=L1[0]*10
    print(SUM)'''


'''s='LOST'
l=[10,21,33,4]
d={}
for i in range(len(s)):
    if i % 2 ==0:
        d[l.pop()]=s[i]
    else:
        d[l.pop()]=i+3
for k,v in d.items():
    print(k,v,sep='*')'''


'''def FUN(A):
    L=[]
    for i in range(2,A):
        if (A%i==0):
            L.append(i)
    print(L)
    print(N)
N=10
FUN(N)'''



'''def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end='')
            print()

print_pattern(4)'''

#WAP to make a pattern
# *********
#  *******
#   *****
#    ***
#     *

'''n=int(input("Enter the number of * in first line:"))
a=''
for i in range(n,0,-2):
    print(a,i*'*')
    a+=' ' '''


'''# Rough for i in range(1,200):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 :
        l.append(i)
n=int(input("Enter the number of line:"))
a=n*''
for i in range(1,n):
    print(a,i*'*')
    a-=' ' '''





'''a=0
for i in range(9,0,-2):
    a=a+1
    print(" "*a,end='')
    for j in range(i):
        print("*",end='')
    print()'''


'''a=' '
print(a,len(a))
a+=' '
print(a,len(a))'''


#WAP to print
#*********
#*******
#*****
#***
#*

'''for i in range(1,10,2):
    for j in range(10,i,-1):
        print("*",end='')
    print()'''

#WAP to make a basic calculator
'''def add(n1,n2):
    print('Sum is:',n1+n2)
def sub(n1,n2):
    print('Difference is:',n1-n2)
def multiply(n1,n2):
    print('Product is:',n1*n2)
def divide(n1,n2):
    print('Division is:',n1/n2)

print("$$$-Hello Welcome to my basic calculator-$$$ \n It can do:- \n Addition \n Subtraction \n Multiply \n Division")
n1=eval(input("Enter the first no:"))
op=input("Enter the operator (+,-,*,/) :")
n2=eval(input("Enter the second number:"))
if op=='+' :
    add(n1,n2)
if op=='-' :
    sub(n1,n2)
if op=='*' :
    multiply(n1,n2)
if op=='/' :
    divide(n1,n2)
if op!= '+' or '-' or '*' or '/' :
    print("Please enter one of the operator(+,-,*,/)!!")'''


'''def prime_detector(n):
    l=[2,3,5,7]
    for i in l:
        for j in range(1,101):
            if n%i!=0:
                print(n,"is a prime number")
            else:
                print(n,"is not a prime number")
            if j%i!=0:
                print("Prime numbars are:",j,end='')
            
        
n=int(input("Enter a number:"))
prime_detector(n)'''


'''def ch(s):
    m=''
    for i in range(0,len(s)):
        if s[i].isupper():
            m=m+s[i].lower()
        elif s[i].islower():
            m=s[i].upper()+m
        else:
            if i%2==0:
                m=m+s[i-1]
            else:
                m='%'+m
    print(m)
ch('Try2Solve@')'''

'''p=4
def checkdata(y):
    global p
    print(p+2)
    r=y
    p=r+8
print(p)
checkdata(12)
print(p)'''


'''def add(a,b):
    d=a+b
    e=a-b
    #return (d,e)

c=add(2,3)
print(c)'''



'''help(list)

x=[1,2,3,4,5]
print(x.__getitem__(2))'''

'''def print_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "|")

def main():
    tree_height = int(input("Enter the height of the Christmas tree: "))
    print_christmas_tree(tree_height)
    print("Merry Christmas!")

if __name__ == "__main__":
    main()'''

#a=str('[1,2,3]')
#print(a,type(a))

#l=[1,1,2,3,4,5,1]
'''l2=[1,1,2,3,4,5,1]
l.remove(1)
print(l)
#print(l2.remove())
#l2.remove(6)
print(l2)
del l[5]
print(l)
l.pop(4)
print(l)'''

'''print(sorted(l))
print(l)
print(l.sort(reverse=True))
print(l)'''


s='welcome2cs'
#s=[1,2,3,4,5,6,7,8,9,10,11]
#print(s[-10:-5:1])
#print(s[-10:-4:1])
#print(s[-10:-3:-1])
#print(s[-4:-12:1])
'''n_s=''
l=list(s)
for i in sorted(l):
    if i not in n_s:
        n_s+=i
print(n_s)'''
#print(s[-7:-4:1])
'''n=len(s)
m=''
for i in range(0,n):
    if (s[i]>='a' and s[i]<='m'):
        m=m+s[i].upper()
    elif (s[i]>='n' and s[i]<='z'):
        m=m+s[i-1]
    elif (s[i].isupper()):
        m=m+s[i].lower()
    else:
        m=m+'&'
print(m)'''

#a=[1,2,3,4]
#print(a[-1:-4:-1])

'''print(10*20%3)
print((10*20)%3)
print(10*(20%3))'''


'''print(10/10*2)
print((10/10)*2)
print(10/(10*2))

print(10*89/3)
print((10*89)/3)
print(10*(89/3))'''

'''d={}
d[1.0]=1
d[2]=2
print(d)
d[1]=2

print(d)'''


#s='kendriya'
#print(s[-7:-8:-1])


#help()

'''l=['a','b','c']
print(l[::-1])'''

'''a=[1,2,4,3]
a.sort()
print(a)'''


'''#l=['ani','an','h','ab']
l=["apple","banana","pear","mango"]
l1=sorted(strings, key=len)
print(l1)'''


#recursion

#Fibonacci series

'''def fib(t):
    if (t==0):
        return 0
    elif (t==1):
        return 1
    else:
        return fib(t-1) + fib(t-2)


for t in range(int(input("enter number : "))):
    print(fib(t))'''


'''try:
    a=int(input("Enter value:"))

except ValueError:
    if a=="quit" :
        print("Enter a numeric value")
    else:
        raise ValueError("value should be numeric or quit")'''
























    

















































     


























