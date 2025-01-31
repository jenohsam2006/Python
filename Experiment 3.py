#Jenoh Sam J B
#URK24CS1154
#Single string from two given strings, separated by a space, and swap the first characters of each string.
print("URK24CS1154")
s1 = "welcome"
s2 = "good"
ns1 = s2[0] + s1[1:]
ns2 = s1[0] + s2[1:]
r = ns1 + " " + ns2
print(r)

#Jenoh Sam J B
#URK24CS1154
#String from a given string where all occurrences of its first char have been changed to ‘#’ except the first char itself.
print("URK24CS1154")
s = "restart"
fc = s[0]
r = fc + s[1:].replace(fc, '#')
print(r)

#Jenoh Sam J B
#URK24CS1154
#Second most repeated word a given string.
print("URK24CS1154")
t = "I realized my happiness was artificial. I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."
w=t.lower().split()
print(sorted(set(w), key=w.count)[-2])

#Jenoh Sam J B
#URK24CS1154
#Count occurrences of a substring in a string.
print("URK24CS1154")
s = input("Enter string: ")
ss = input("Enter substring: ")
c = s.count(ss)
print(c)
