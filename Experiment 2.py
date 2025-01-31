1
l = [12, 45, 2, 9, 3,5,45]
n=set(l)
l=list(n)
print(l)
print("Second smallest:", l[1])
print("Second largest:", l[-2]) 

2
e = ['apple', 'banana', 'apple', 'orange','banana','apple']
for i in set(e):
    c = e.count(i)
    print(f'{i}: {c}')
3

c = []
for i in range(2):
    n = input("Enter name: ")
    m = input("Enter mobile number: ")
    c.append((n,m))
print(c)
sn = input("Enter the person name to search: ")
for co in c:
    if co[0] == sn:
        print(f"Mobile Number is {co[1]}")
        break
else:
    print("No contact found for", {sn})
4

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Union :", a | b)
print("Intersection :", a & b)
print("Difference :", a - b)
print("Symmetric difference :", a ^ b)
