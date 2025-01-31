
s1 = "welcome"
s2 = "good"
ns1 = s2[0] + s1[1:]
ns2 = s1[0] + s2[1:]
r = ns1 + " " + ns2
print(r)


s = "restart"
fc = s[0]
r = fc + s[1:].replace(fc, '#')
print(r)


t = "I realized my happiness was artificial. I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."
w=t.lower().split()
print(sorted(set(w), key=w.count)[-2])


s = input("Enter string: ")
ss = input("Enter substring: ")
c = s.count(ss)
print(c)
