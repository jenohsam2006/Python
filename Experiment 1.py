#Jenoh Sam J B
#URK24CS1154
#Factortial
print("URK24CS1154")
n=int(input("Enter the number:"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("Factorial",fact)



#Jenoh Sam J B
#URK24CS1154
#Prime Number or not
print("URK24CS1154")
n = int(input("Enter the number: "))
if n <= 1:
    print("Not prime")
f = 0 
i = 2
while i <= n -1:
    if n % i == 0:
        f = 1
        break
    i += 1
if f == 0:
    print("Prime")
else:
    print("Not prime")



#Jenoh Sam J B
#URK24CS1154
#Palindrome or not
print("URK24CS1154")
n = int(input("Enter a number: "))
o = n
r = 0
while n > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10
if o == r:
    print(o,"is a palindrome.")
else:
    print(o," is not a palindrome.")




#Jenoh Sam J B
#URK24CS1154
#Armstrong or not
print("URK24CS1154")
n = int(input("Enter a number: "))
o = n
r = 0
d1 = len(str(n))
while o > 0:
    d = o % 10
    r += d ** d1
    o = o // 10
if r == n:
    print(n,"is a armstrong.")
else:
    print(n," is not a armstrong.")
