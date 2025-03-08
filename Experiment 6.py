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




def read_line(fn, n):
    with open(fn) as f:
        print("".join(f.readlines()[:n]))
fn = "alphabet.txt"
n = int(input("Enter number of lines to read: "))
read_line(fn, n)



from collections import Counter
with open("alphabet.txt") as f:
    print(Counter(f.read().lower().split()))
