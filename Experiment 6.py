#Jenoh Sam J B
#URK24CS1154
#create a file where all letters of the English alphabet are listed
print("URK24CS1154")
import string
def alphabet_file(fn, n):
    al = string.ascii_uppercase
    with open(fn, "w") as f:
        for i in range(0, len(al), n):
            f.write(al[i:i+n] + "\n")
n = int(input("Enter the number of letters per line: "))
fn = "alphabet.txt"
alphabet_file(fn, n)
print(f"File '{fn}' has been created with {n} letters per line.")


#Jenoh Sam J B
#URK24CS1154
#read the first n lines of a file
print("URK24CS1154")
def read_line(fn, n):
    with open(fn) as f:
        print("".join(f.readlines()[:n]))
fn = "alphabet.txt"
n = int(input("Enter number of lines to read: "))
read_line(fn, n)


#Jenoh Sam J B
#URK24CS1154
#count the frequency of words in a file
print("URK24CS1154")
from collections import Counter
with open("alphabet.txt") as f:
    print(Counter(f.read().lower().split()))
