a=int(input("enter a value"))
b=int(input("enter b value"))
#arithmetic
print(f"sum of two numbers:{a+b}")
print(f"sub of two numbers:{a-b}")
print(f"multiply of two numbers:{a*b}")
print(f"modulo division of two numbers:{a%b}")
print(f"division of two numbers:{a/b}")
print(f"floor division of two numbers:{a//b}")

#assignment
a1=a
print(f"true if a==b:{a==b}")
a1+=b
print(f"a+=b:{a1}")
a1-=b
print(f"a-=b:{a1}")
a1*=b
print(f"a*=b:{a1}")
a1/=b
print(f"a/=b:{a1}")
a1//=b
print(f"a//=b:{a1}")
a1%=b
print(f"a%=b:{a1}")
a1**=b
print(f"a**=b:{a1}")

#comparision
print(f"a==b:{a==b}")
print(f"a!=b:{a!=b}")
print(f"a>b:{a>b}")
print(f"a<b:{a<b}")
print(f"a>=b:{a>=b}")
print(f"a<=b:{a<=b}")

#logical
print(a==b and a>b)
print(a==b or a>b)
print(not(a>b))


c={1,4,6,7}
#membership
print(2 in c)
print(4 in c)
print(1 not in c)

#identity
print(a is not b)
print(a is b)

#bitwise
print(a&b)
print(a|b)
print(a^b)
print(a >> 2)
print(a<<2)

'''
OUTPUT:
enter a value5
enter b value10
sum of two numbers:15
sub of two numbers:-5
multiply of two numbers:50
modulo division of two numbers:5
division of two numbers:0.5
floor division of two numbers:0
true if a==b:False
a+=b:15
a-=b:5
a*=b:50
a/=b:5.0
a//=b:0.0
a%=b:0.0
a**=b:0.0
a==b:False
a!=b:True
a>b:False
a<b:True
a>=b:False
a<=b:True
False
False
True
False
True
False
True
False
0
15
15
1
20
'''


