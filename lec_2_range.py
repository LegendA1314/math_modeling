""""
По умолчанию: start = 0, step = 1
Диапозон генерирование: [start, stop]
"""
a = range(0, 10, 2)
print (a)
print(type(a))
print(a[3])

a = "Good"
for i in range(0, 10, 1):
  if i < len(a):
    print(a[i] + " - bad")
  else:
    print(f"{i}" + " - good")  