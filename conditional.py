#conditional statements
#if statement
#if-else statement
age=int(input("enter age"))
if age>=18:
    print("major")
else:
    print("minor")

'''
OUTPUT
enter age19
major

=========================================================================== RESTART: C:/python/conditional.py ==========================================================================
enter age12
minor
'''

#if-elif-else statement
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print(f"a:{a} is greater")
elif b>c and b>a:
    print(f"b:{b} is greater")
elif c>b and c>a:
    print(f"c:{c} is greater")
else:
    print("invalid number")

'''
OUTPUT
enter a:10
enter b:9
enter c:8
a:10 is greater

enter a:4
enter b:5
enter c:6
c:6 is greater
'''
