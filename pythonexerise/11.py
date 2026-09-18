#operasi logika atau boolean
#not, or(\), and, xor

a=True
c= not a
print('data a=',a)
print('data c=',c)

a=True
d= False
c= a or d
print(a,'or',d,'=',c)

a= False
d= False
c= a or d
print(a,'or',d,'=',c)

a=True
d= True
c= a or d
print(a,'or',d,'=',c)


a=True
d= False
c= a and d
print(a,'and',d,'=',c)

a=True
d= False
c= a ^ d
print(a,'xor',d,'=',c)

a=True
d= True
c= a ^ d
print(a,'xor',d,'=',c)


a=False
b=False
c=a ^ b
print(a,'^',b,"=", c)


a=False
c=not a
print('c=',c)


umur=20
print(type(umur))