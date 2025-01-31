#Jenoh Sam J B
#URK24CS1154
#Second smallest and Second largest number in a list.
print("URK24CS1154")
l = [12, 45, 2, 9, 3,5,45]
n=set(l)
l=list(n)
print(l)
print("Second smallest:", l[1])
print("Second largest:", l[-2]) 

#Jenoh Sam J B
#URK24CS1154
#Frequency of the elements in a list.
print("URK24CS1154")
e = ['apple', 'banana', 'apple', 'orange','banana','apple']
for i in set(e):
    c = e.count(i)
    print(i," : ",c)

#Jenoh Sam J B
#URK24CS1154
#Provided person names and mobile numbers as tuples in a list and search for mobile numbers based on a given person's name.
print("URK24CS1154")
c = []
for i in range(3):
    n = input("Enter name: ")
    m = input("Enter mobile number: ")
    c.append((n,m))
print(c)
sn = input("Enter the person name to search: ")
for co in c:
    if co[0] == sn:
        print("Mobile Number is : ",co[1])
        break
else:
    print("No contact found for ", sn)

#Jenoh Sam J B
#URK24CS1154
#Demonstrate all the methods in set.
print("URK24CS1154")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Union :", a | b)
print("Intersection :", a & b)
print("Difference :", a - b)
print("Symmetric difference :", a ^ b)
