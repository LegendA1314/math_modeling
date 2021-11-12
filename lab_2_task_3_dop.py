b = int(input("Ну вводи "))
a = 0 

while b > 0:

    a = a * 10 + b % 10
    b = b // 10
    
print(a)
