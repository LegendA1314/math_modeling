a = int(input())
b = int(input())

if a % b == 0:
    print("%d делится на %d" % (a,b))
else:
    print("%d не делится на %d" % (a,b))
    print("Остаток: %d" % (a%b))
    
print("Частное: %d" % (a//b))