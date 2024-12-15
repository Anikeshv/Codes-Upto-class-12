
#WAP to calculate area of a circle
#Solution
r=float(input("Enter the radius of the circle:"))
a=3.14

print("The area of circle is :",r*r*a)


#WAP to calculate the simple interest
#Solution
'''p=float(input("Enter the value of Principle:"))
r=float(input("Enter the value of Rate of interest:"))
t=float(input("Enter the value of Time Period:"))

print("Simple Interest=",p*r*t/100)'''


#WAP to calculate temperature in centigrate if user input temperature in Fahrenheit.
#Solution
'''f=float(input("Enter the temperature in Fahrenheit:"))
print("The Temperature in Centigrate is:",5*f/9-17.77)'''
#You can do this (5*f/9-17.77) , ( (f-32)*5/9) ) , ( (f-32)*0.5556 )   Formula=  C=(5f-160)/9


#WAP to take input in five different subjects and calculate Total,Average,Percentage.
#Solution
'''p=float(input("Enter the marks in Physics out of 40:"))
c=float(input("Enter the marks in Chemistry out of 40:"))
m=float(input("Enter the marks in Mathematics out of 40:"))
cs=float(input("Enter the marks in Computer Science out of 40:"))
e=float(input("Enter the marks in English out of 40:"))
print("Total marks obtained in all subjects is:",p+c+m+cs+e)
print("Average marks for all subjects is:",(p+c+m+cs+e)/5)
print("Percentage obtained=",(p+c+m+cs+e)/2)'''


#WAP to take two numbers and check that the first number is fully divisible by second number or not.
'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if a%b==0:
          print("Completely divisible")
else:
        print("Not completely divisible")'''

#WAP to print the following pattern
# *
# **
# ***
# ****
# *****
'''n=int(input("Enter the limit:"))
for i in range(1,n+1):
    print(i*'*')'''


# Example of endless loop

'''i=-1
while(i<0):
    print(i)
    i-=2'''

    
# WAP to print whether condition

'''whether=input("How is the whether:")
if whether=='sunny':
    print('wear sunblock')
elif whether=='snow':
        print('Going skiing')
else:
            print("None of the above")'''


#WAP that asks your height in centimeters and converts it into foot and inches.

'''h=float(input("Enter the height in centimeters:"))

print("Height in foot is:",h*0.0328084)
print("Height in inch is:",h*0.393701)'''

#WAP to convert Kilometers to Miles.

'''d=float(input("Enter a number into kilometers:"))
print("In miles :",d*0.621371)'''

#WAP to find if a given number (0-999) is 1/2/3 digit number

'''n=int(input("Enter the number:"))

if(n>=0 and n<10):
    print("One digit number")
elif(n>=10 and n<100):
        print("Two digit number")
else:
 print("Three digit")'''


#WAP to enter any number and check it is even or odd (using simple if and if-else both)

'''n=int(input("Enter any number "))
if(n%2==0):
    print("even")
if(n%2!=0):
    print("odd")

n=int(input("Enter any number "))
if(n%2==0):
    print("even")
else:
    print("odd")'''

#WAP to enter 2 number and print the largest number'''
'''n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
large = n1
if (large<n2):
 large=n2
print("Largest number is ", large)'''

#WAP to enter 3 number and print the largest number'''
'''n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
n3 = int(input("Enter third number "))
large = n1
if (large<n2):
   large=n2
if(large<n3):
   large=n3
print("Largest number is ", large)'''


#Input temperature of water and print its physical state

'''t=float(input("Enter the temperature in Degree centigrate:"))
if(t<=0):
    print("Physical state of water is 'SOLID'")
elif(t>=100):
    print("Physical state of water is 'STEAM'")
else:
    print("Physical state of water is 'LIQUID'")'''

#Input 3 side of triangle and print the type of triangle –Equilateral, Scalene, Isosceles

#Solution 1
'''a=float(input("Enter the first side of the Triangle:"))
b=float(input("Enter the second side of the Triangle:"))
c=float(input("Enter the third side of the Triangle:"))

if(a==b==c):
    print("It is an Equilateral Triangle")
    
elif(a==b and a!=c):
    print("It is an isosceles triangle")
elif(a==c and a!=b):
    print("It is an isosceles triangle")
elif(c==b and c!=a):
    print("It is an isosceles triangle")

else:
    print("It is a Scalane triangle")'''

#Solution 2
'''a=float(input("Enter the first side of the Triangle:"))
b=float(input("Enter the second side of the Triangle:"))
c=float(input("Enter the third side of the Triangle:"))

if(a==b==c):
    print("It is an Equilateral Triangle")
elif(a!=b and b!=c and a!=c):
    print("It is a Scalane triangle")
else:
    print("It is an isosceles triangle")'''


#WAP to read three numbers and print them in acending order

'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the Third number:"))

if(a<b<c):
    print("Numbers in acending order are:",a,',',b,',',c)
elif(a<c<b):
    print("Numbers in acending order are:",a,',',c,',',b)
elif(b<a<c):
    print("Numbers in acending order are:",b,',',a,',',c)
elif(b<c<a):
    print("Numbers in acending order are:",b,',',c,',',a)
elif(c<a<b):
    print("Numbers in acending order are:",c,',',a,',',b)
elif(c<b<a):
    print("Numbers in acending order are:",c,',',b,',',a)'''


'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the Third number:"))

if(a<b<c):
    print("Numbers in acending order are:",a,b,c)
elif(a<c<b):
    print("Numbers in acending order are:",a,c,b)
elif(b<a<c):
    print("Numbers in acending order are:",b,a,c)
elif(b<c<a):
    print("Numbers in acending order are:",b,c,a)
elif(c<a<b):
    print("Numbers in acending order are:",c,a,b)
elif(c<b<a):
    print("Numbers in acending order are:",c,b,a)'''

#Example of endless loop  #LOOKS LIKE HACHING SOMETHING
'''i=0
while (i<100):
    print("YOU ARE HACKED  1001001001oo1o 0013850 002  940 110000100.. 0100203000 01399201990000000 00006230" *15)'''


#WAP to print counting from 1 till limit #using for loop
'''n=int(input("Enter the limit:"))
i=0
for i in range(1,n+1):
    print(i)'''

#WAP to calculate the factorial of a given number. #Using while
'''n=int(input("Enter any number:"))
a=1
for i in range(1,n+1):
    a=a*i
    n=n-1'''

#2nd method wrong
'''n=int(input("Enter any number:"))
a=1
while(a>0):
    a=a*n
    n=n-1   
print("The factorial of given number:",a)'''
    
#WAP to print counting  till limit #using while loop

'''n=int(input("Enter any number:"))
i=1
while (i<=n):
    print(i)
    i+=1'''

#WAP to check a given number is prime or composite
'''i=int(input("Enter any number:"))
if( i%2!=0 and i%3!=0  and i%5!=0  and i%7!=0):
    print(i,"Is a prime number")
elif(i==2 or i==3 or i==5 or i==7):
    print(i,"Is a prime number")
else:
    print(i,"Is a composite number")'''

#WAP to read a number and write it in words ?????????????????

#Wap to read a number and tell how many digits are in it and tell its place


#WAP to calculate simple interest using loop
'''n=int(input("Enter any no.:"))
for i in range(n):
    p=int(input("Enter the principal:"))
    r=int(input("Enter the rate:"))
    t=int(input("Enter the time:"))
    print("SI:",(p*r*t/100))'''


#Calculator

'''n=int(input("Enter any no.:"))
for i in range(n):
    a=eval(input("Enter the first number:"))
    b=eval(input("Enter the second number:"))
    c=eval(input("If you want to add type 1" " if subtract type 2, if multiply type 3" " if divide type 4 :"))

    if(c==1):
        print("Answer=",a+b)
    elif(c==2):
        print("Answer=",a-b)
    elif(c==3):
        print("Answer=",a*b)
    else:
        print("Answer=",a/b)'''

#WAP to check a number is prime or not.
'''n=int(input("Enter any no.:"))

if(n==2 or n==3 or n==5 or n==7):
    print(n,"is a prime no.")
elif(n%2==0 or n%3==0 or n%5==0 or n%7==0):
    print(n,"is not a prime no.")
else:
    print(n,"is a prime no.")'''

#WAP to print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

'''for i in range(1,6,1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


#WAP find length using len()
'''n=input("Enter anything:")
print(len(n))'''

#WAP to find length of a string without using len()
'''n=input("Enter anything:")
a=0
for i in n:
    a+=1
print("length of entered thing:",a)'''

#WAP to find frequency in a list using count()
'''L=[1,2,3,4,5,6,7,8,9,1,2,3,5,7,9,1]
n=int(input("Enter a number:"))
print(L.count(n))'''

#WAP to find frequency in a list without using count()
'''L=[1,2,3,4,5,6,7,8,9,1,2,3,5,7,9,1]
n=int(input("Enter a number:"))
a=0
for i in range (len(L)):
    if L[i]==n:
        a+=1
print("Frequency:",a)'''

#WAP to take a string from the user and print another character in the place of all vowels.
'''Str = input("Enter a String: ")
Char = input("Enter a character to replace all vowels with it: ")
newstr = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(len(Str)):
    if Str[i] in vowels:
        newstr = newstr + Char
    else:
        newstr = newstr + Str[i]

print("\nOriginal String =", Str)
print("New String =", newstr)'''


#WAP to input a string and reverse it.
'''n=input("Enter a string:")
b=''
a=len(n)-1
for i in range(a,-1,-1):
   b=b+n[i]
print(b)'''



#To remove even no. from a list
#CODE 1
'''x=eval(input("Enter the list:"))
a=[]
for i in x:
       if(i%2!=0):
              a.append(i)
x=a
print(x)'''

#CODE 2
'''x=eval(input("Enter the list:"))
for i in x:
    if(i%2==0):
           x.remove(i)
for i in x:
    if(i%2==0):
           x.remove(i))
for i in x:
    if(i%2==0):
           x.remove(i)
print(x)'''

#Calculator
'''n=int(input("enter first number:"))
o=input("enter the operator (+,_,*,/,%):")
n1=int(input("Enter the second number:"))

if(o=='+'):
    print("The output is:",n+n1)
elif(o=='-'):
    print("The output is:",n-n1)
elif(o=='*'):
    print("The output is:",n*n1)
elif(o=='/'):
    print("The output is:",n/n1)
elif(o=='%'):
    print("The output is:",n%n1)'''


#Find the prime numbers in a tuple and also find the second lowest value in the tuple 
#1st method
'''x=eval(input("Enter a tuple: "))
y=[]
for i in range(len(x)):
    if(x[i]==2 or x[i]==3 or x[i]==5 or x[i]==7):
        y.append(x[i])
    if(x[i]%2!=0 and x[i]%3!=0  and x[i]%5!=0  and x[i]%7!=0):
        y.append(x[i])
print("Prime numbers in the tuple are:",tuple(y))

b=min(x)
a=list(x)
a.remove(b)
c=min(a)
print("Second lowest value is:",c)'''

#2nd method
'''x=eval(input("Enter a tuple: "))
y=[]
for i in range(len(x)):
    if(x[i]==2 or x[i]==3 or x[i]==5 or x[i]==7):
        y.append(x[i])
    if(x[i]%2!=0 and x[i]%3!=0  and x[i]%5!=0  and x[i]%7!=0):
        y.append(x[i])
print("Prime numbers in the tuple are:",tuple(y))

a=sorted(x)
print("Second lowest value is:",a[1])'''


#Take a list and update it by adding 3 to the multiples of three in the list

'''x=eval(input("Enter a List: "))
b=[]
for i in range(len(x)):
    if(x[i]%3==0):
        a=x[i]+3
        b.append(a)
    else:
        b.append(x[i])
print("Updated list:",b)'''

#Take a list and arrange the negative no. on left side then zero and then positive no.
'''x=eval(input("Enter a List: "))
a=[]
b=[]
c=[]
for i in range(len(x)):
    if(x[i]>0):
        a.append(x[i])
    if(x[i]==0):
        b.append(x[i])
    if(x[i]<0):
        c.append(x[i])
a.extend(b)
a.extend(c)

print(a)'''

#To remove even no. from a list
'''x=eval(input("Enter a list:"))
i=0
a=0
while i<len(x):
    if x[i]%2==0:
        x.remove(x[i])
        a=a+1
    elif a==len(x):
        break
    else:
        i=i+1
print(x)'''

#Input three numbers and display the largest / smallest number.
'''a=int(input("Enter the message:"))
b=int(input("Enter the message:"))
c=int(input("Enter the message:"))
if(a>b and a>c):
    print("LAR:",a)
if(b>a and b>c):
    print("LAR:",b)
if(c>a and c>b):
    print("LAR:",c)'''

#Input three numbers and display the largest / smallest number.
'''x=[]
for i in range(3):
    a=int(input("Enter the message:"))
    x.append(a)
print(max(x))
print(min(x))'''

#Sum of series (a)#Series was in the image
'''x=int(input("Enter the no.:"))
n=int(input("Enter the no.:"))
a=1
for i in range(1,n+1):
    a=a+x**i
print(a)'''

#Sum of series (b)#Series was in the image
'''x=int(input("Enter the no.:"))
n=int(input("Enter the no.:"))
a=1
b=0
for i in range(2,n+1,2):
    a=a+x**i
for i in range(1,n+1,2):
    b=b+x**i
print(a-b)'''

#Sum of series (c)#Series was in the image
'''x=int(input("Enter the no.:"))
n=int(input("Enter the no.:"))
a=0
for i in range(1,n+1):
    a=a+(x**i)/i
print(a)'''

#Sum of series (d)#Series was in the image
'''x=int(input("Enter the no.:"))
n=int(input("Enter the no.:"))
s=x
f=1
for i in range(1,n):
    z=i+1
    f=f*z
    s=s+((x**z)/f)
print("Sum :",s)'''

#Determine whether a number is a perfect number, an Armstrong number or a palindrome.

'''num_str=input("Enter a no.:")
num=int(num_str)
num_List=list(num_str)
c,s=0,0
for i in num_List:
    c+=int(i)**3
e=num_List[::-1]
for i in range(1, num):
    if(num % i == 0):
        s+= i
if c==num:
    print(num,"is an armstrong number")
if (s==num):
    print(num,"is a perfect number")
if num_List==e:
    print(num,"is a palindrome")
elif(c!=num and s!=num and num_List!=e):
    print(num,"is neither a perfect number nor an armstrong number and a palindrome ")'''

#Input a number and check if the number is a prime or composite number

'''num=int(input("Enter any number:"))
if( num%2!=0 and num%3!=0  and num%5!=0  and num%7!=0):
    print(num,"Is a prime number")
elif( num==1 or num==2 or num==3 or num==5 or num==7):
    print(num,"Is a prime number")
else:
    print(num,"Is a composite number")'''

#Display the terms of a Fibonacci series.

'''n = int(input("Enter the no. of terms: "))
n1, n2 = 0, 1
count = 0
if n == 1:
   print("Fibonacci sequence upto",n,"term :",n1)
else:
    print("Fibonacci sequence:")
    while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1'''

#Compute the greatest common divisor and least common multiple of two integers

'''n1=int(input("Enter the first number:"))
n2=int(input("Enter the first number:"))
a=1
for i in range(1, n1):
    if(n1 % i == 0 and n2 % i == 0):
        a*=i
print("Highest common factor is:",a)
print("Lowest common factor is:",(n1*n2)/a)'''

#Count and display the number of vowels, consonants, uppercase, lowercase characters in string.


'''s=input("Enter a string:")
nv,nc,nu,nl,ns=0,0,0,0,0
v=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in s:
    if(i.isspace()):
        ns+=1
    if(i in v):
        nv+=1
    elif(i not in v and i.isalpha()):
        nc+=1
    if(i.isupper()):
        nu+=1
    elif(i.isalpha() and i.islower()):
        nl+=1
print("Number of vowels:",nv)
print("Number of consonents:",nc)
print("Number of uppercase characters:",nu)
print("Number of lowercase characters:",nl)'''

#Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.

'''s=input("Enter a string:")
s1=''
a,b=list(s),list(s)
a.reverse()
if(a==b):
    print(s,"is a palindrome")
for i in s:
    if(i.isupper()):
        s1=s1+i.lower()
    else:
        s1=s1+i.upper()
print(s1)'''

 #Find the largest/smallest number in a list/tuple

'''a=eval(input("Enter a list or a tuple:"))
lar,sml=a[0],a[0]
for i in a:
    if lar<i:
        lar=i
    if sml>i:
        sml=i
print("Largest no.:",lar)
print("Smallest no.:",sml)'''

#Input a list of numbers and swap elements at the even location with the elements at the odd location.

'''a=eval(input("Enter a list "))
for i in range(0,len(a),2):
    a[i],a[i+1]=a[i+1],a[i]
print("List after swapping :",a)'''

#Input a list/tuple of elements, search for a given element in the list/tuple.

'''a=eval(input("Enter a list or tuple:"))
b=eval(input("Enter a element to search:"))
for i in range(len(a)):
    if(b==a[i]):
        d=1
        c=i
if(d==1):
    print("Element Found at index:",c)
else:
    print("Not Found")'''


#Write a program to find the sum and average of numbers stored in a list.
'''l=eval(input("Enter a list:"))
s=0
for i in l:
    s=s+i
print("Sum of numbers in the list:",s)
print("Average of the numbers in the list:",s/len(l))'''

#Write a program to read a list of n integers. (positive as well as negative).
#Create two new lists, one having all positive numbers and the other have all negative numbers from the given list. Print all three lists.

'''l=eval(input("Enter the list of integers:"))
a,b,c=[],[],[]
for i in l:
    if i==0:
        a.append(i)
    if i>0:
        b.append(i)
    if i<0:
        c.append(i)
print("Original List:",l)
if len(a)>0:
    print("List having Zero:",a)
print("List with positive numbers:",b)
print("List with negative numbers:",c)'''

#Write a program to peform the following operation on list
#a. Delete element at the desired position
'''l=eval(input("Enter a list:"))
a='y'
while a=='y':
    p=int(input("Enter the index from which value to be removed:"))
    l.pop(p)
    a=input("Enter y if you want to remove one more value otherwise enter n:")
print("New list:",l)'''

#b. Delete element by its name

'''l=eval(input("Enter a list:"))
a='y'
while a=='y':
    p=int(input("Enter the value which is to be removed:"))
    l.remove(p)
    a=input("Enter y if you want to remove one more value otherwise enter n:")
print("New list:",l)'''


#Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have marks above 75.

'''n=int(input("Enter the no. of students:"))
d={}
for i in range(n):
    Nm=input("Enter the name:")
    Rn=int(input("Enter the roll no.:"))
    M=int(input("Enter the marks:"))
    d[Rn]=[Nm,M]
print(d)
for i in d:
    if d[i][1]>75:
        print("Student having marks above 75 is:",d[i][0])'''


#Create a dictionary using a string
#Example:- 'Hello' so dictionary will be {'H':1,'e':1,'l':2,'o':1}

'''a=input("Enter the string:")
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print("Dictionary:",b)'''

#WAP to remove duplicate items from a list

'''a=eval(input("Enter the list:"))
b=[]
for i in a:
    if i in b:
        continue
    else:
        b.append(i)
print(b)'''

#Using dict.items() function

'''d={1:'ani',2:'tan'}
for k,v in d.items():
       print(k,':',v)'''



'''l=[]
n=int(input("Enter your choice (1,2,3,4):"))
for i in range(1,200):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 :
        l.append(i)
        print("Prime no are:",i)

while n:
    if n==1:
        print("Sum is:",sum(l[0:5]))
        break
    elif n==2:
        print("Sum is:",sum(l[-1:-5:-1]))
        break
    elif n==3:
        print("Sum is:",sum(l))
        break
    elif n==4:
        print('Thank you$')
        break'''


'''st=input("Enter the dtring:")
l=st.split()
w=len(l)
a,c,d,s=0,0,0,0
for i in st:
    c+=1
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    elif i!=' ':
        s+=1
print('Total no of characters are:',c)
print('Total no of words are:',w)
print('Total no of alphabeds are:',a)
print('Total no of digits are:',d)
print('Total no of special characters are:',s)'''


'''num={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
n=int(input("Enter the number:"))
s=''
for i in str(n):
    s+=num[int(i)]
    s+=' '
print("string:",s)'''


'''n=int(input("Enter the no of entries you want:"))
d={}
for i in range(n):
    name=input("Enter employee name:")
    salary=int(input("Enter his salary:"))
    d[name]=salary

for i in d:
    if d[i]>65000:
        print('Employee with salary greater than 65000 :',i)'''



















































    
 

        
              

























































































































































           


















































              



























































































    
    










