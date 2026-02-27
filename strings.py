#string slicing
s="madhu lekha"
a=s[0:7]#[start:stop]
print(a)
b=s[1:4:2]#[start:stop:step]
print(b)
print(s[::-1])
print(s[:4])
print(s[0:])
#string indexing
print(s[-1])#negative indexing
print(s[0])#positive indexing
print(s[5])
#string concatenation
s1="sompalli"
b=s+s1
print(b)
#string length
length=len(s)
print(length)
#string methods
print("s.upper:",s.upper())#upper case:it makes all the letters capital
print("s.capitalize:",s.capitalize())#it makes the first letter capital and remaining lower
print("s:title:",s.title())#it makes all the starting letters capital
print("s.lower:",s.lower())#lower case
print("s.split:",s.split(','))# splitting by using something
print("s.replace:",s.replace('h','s'))#replacing
print("s.count:",s.count('a'))#count
print(s.count('k'))
print(s.count('r'))
print(s1.count('l'))
print("s.strip:",s.strip('a'))
print("s.lstrip:",s.lstrip())
print(s1.lstrip())
print("s.rstrip:",s.rstrip('m'))
print(s1.rstrip(a))
print("s.startswith and start is from 7:",s.startswith("lekha",7))
print("s.endswith:",s.endswith('lekha'))
words=['madhu','lekha','sompalli']
#print("s.join:",words.join('-'))
print("s.join:","-".join(words))
print("s.find:",s.find("madhu"))
print(s.find("l",4,11))#searches from l->r and if string not found returns -1
s2="madhu lekha madhu"
print("s.rfind:",s.rfind("madhu"))
print(s.find("krsna"))
print("s.index:",s.index("madhu"))#same as find but throws an error if string not found
print("s2.rindex:",s.rindex("madhu"))#same as rfind but throws an error if string not found
#print(s.index("krishna")) it throws an error
print("s.isalnum:",s.isalnum())
print("s.isalpha:",s.isalpha())
print("s.isdigit:",s.isdigit())
print("s.islower:",s.islower())
print("s.isupper:",s.isupper())
print("s.istitle:",s.istitle())
print("s.isspace:",s.isspace())
print("s.isnumeric:",s.isnumeric())
print("s.isdecimal:",s.isdecimal())


'''
output
============================================================================= RESTART: C:/python/strings.py ============================================================================
madhu l
ah
ahkel uhdam
madh
madhu lekha
a
m
 
madhu lekhasompalli
11
s.upper: MADHU LEKHA
s.capitalize: Madhu lekha
s:title: Madhu Lekha
s.lower: madhu lekha
s.split: ['madhu lekha']
s.replace: madsu leksa
s.count: 2
1
0
2
s.strip: madhu lekh
s.lstrip: madhu lekha
sompalli
s.rstrip: madhu lekha
sompalli
s.startswith and start is from 7: False
s.endswith: True
s.join: madhu-lekha-sompalli
s.find: 0
6
s.rfind: 0
-1
s.index: 0
s2.rindex: 0
s.isalnum: False
s.isalpha: False
s.isdigit: False
s.islower: True
s.isupper: False
s.istitle: False
s.isspace: False
s.isnumeric: False
s.isdecimal: False
'''



