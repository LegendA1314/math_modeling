a = int(input())
n = int(input())
ax = a
#c = a**n
#print(c)

def all(a, n):
  s = 1
  for i in range (n):
   s = s * a
 return s

print(all(a,n))