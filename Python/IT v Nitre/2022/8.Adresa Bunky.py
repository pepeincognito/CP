# napiste svoj kod
import math
import string
abc = [str(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

n = [str(x) for x in input()]

c = int("".join(n[1:n.index("C")]))
r = int("".join(n[n.index("C") + 1:len(n)]))  # pismenka
zvsk = []

def n2a(n,b=string.ascii_uppercase):
   d, m = divmod(n,len(b))
   return n2a(d-1,b)+b[m] if d else b[m]

print(f"{n2a(r-1)}{c}")
