#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

r=5 #adalah assignment
print('nilai r= ',r)

r=r+2
print('nilai r= ',r)

r+=2 #artinya r=r+2
print('nilai r= ',r)

r-=2 #artinya r=r-2
print('nilai r= ',r)

r*=2 #artinya r=r*2
print('nilai r= ',r)

r/=2 #artinya r=r/2
print('nilai r= ',r)

r%=2 #artinya r=r-2
print('nilai r= ',r)

r//=2 #artinya r=r//2
print('nilai r= ',r)

p=5

p**=2 #artinya p=p**2
print('nilai p= ',p)


#operasi bitwise
c= True 
print('nilai c=',c)

c|=False
print('nilai c=',c)


v= False
print('nilai v=',v)

v|=True
print('nilai v=',v)



o= True 
print('nilai o=',o)

o&=False
print('nilai o=',o)

f= True 
print('nilai f=',f)

f^=True
print('nilai f=',f)


c= 0b00011
print('nilai c=',c)

c>>=1
print('nilai c=',c, "menjadi=",format(c,"08b"))
f=30
f>>=2
print(format(f,'08b'))
k=40
print(format(k,'08b'))


a=3
b=5
data=a^b
print(data)

x=8
print(x,'binary=',format(x,'08b'))

x=0b0000011
print(x)
