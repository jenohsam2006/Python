#Jenoh Sam J B
#URK24CS1154
#A number is perfect Number or not using a function.
print("URK24CS1154")
def perfect (n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False
nu = int(input("Enter a number: "))
if perfect(nu):
    print(nu,"is a perfect number.")
else:
    print(nu,"is not a perfect number.")


#Jenoh Sam J B
#URK24CS1154
#A number is a Happy Number or not using a function.
print("URK24CS1154")
def happy (n):
    s = set()
    while n != 1 and n not in s:
        s.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
n = int(input("Enter a number: "))
if happy(n):
    print(n," is a Happy Number.")
else:
    (n," is not a Happy Number.")

#Jenoh Sam J B
#URK24CS1154
#Print the divisors of the last input from the passing numbers.
print("URK24CS1154")
def fun1(*args):
    l = args[-1]
    d = []
    for i in range(1, l + 1):
        if l % i == 0:
            d.append(i)
    print(l,":", end=" ")
    for ds in d:
        print(ds, end=" ")
    print()
fun1(6, 7, 8)
fun1(1, 2, 5, 7, 9)
fun1(1, 3, 5, 7, 9, 12)
