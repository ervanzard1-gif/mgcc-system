#2048(samope 4 dulu aja)
import random
a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'
j='j'
k='k'
l='l'
m='m'
n='n'
o='o'
p='p'
first2=random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])
if first2==a:
    a='\x1b[32m2\x1b[0m'
elif first2==b:
    b='\x1b[32m2\x1b[0m'
elif first2==c:
    c='\x1b[32m2\x1b[0m'
elif first2==d:
    d='\x1b[32m2\x1b[0m'
elif first2==e:
    e='\x1b[32m2\x1b[0m'
elif first2==f:
    f='\x1b[32m2\x1b[0m'
elif first2==g:
    g='\x1b[32m2\x1b[0m'
elif first2==h:
    h='\x1b[32m2\x1b[0m'
elif first2==i:
    i='\x1b[32m2\x1b[0m'
elif first2==j:
    j='\x1b[32m2\x1b[0m'
elif first2==k:
    k='\x1b[32m2\x1b[0m'
elif first2==l:
    l='\x1b[32m2\x1b[0m'
elif first2==m:
    m='\x1b[32m2\x1b[0m'
elif first2==n:
    n='\x1b[32m2\x1b[0m'
elif first2==o:
    o='\x1b[32m2\x1b[0m'
elif first2==p:
    p='\x1b[32m2\x1b[0m'

second2=random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])
while True:
    if second2==first2:
         second2=random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])
         continue
         
    elif second2!=first2:
        break

if second2==a:
    a='\x1b[32m2\x1b[0m'
elif second2==b:
    b='\x1b[32m2\x1b[0m'
elif second2==c:
    c='\x1b[32m2\x1b[0m'
elif second2==d:
    d='\x1b[32m2\x1b[0m'
elif second2==e:
    e='\x1b[32m2\x1b[0m'
elif second2==f:
    f='\x1b[32m2\x1b[0m'
elif second2==g:
    g='\x1b[32m2\x1b[0m'
elif second2==h:
    h='\x1b[32m2\x1b[0m'
elif second2==i:
    i='\x1b[32m2\x1b[0m'
elif second2==j:
    j='\x1b[32m2\x1b[0m'
elif second2==k:
    k='\x1b[32m2\x1b[0m'
elif second2==l:
    l='\x1b[32m2\x1b[0m'
elif second2==m:
    m='\x1b[32m2\x1b[0m'
elif second2==n:
    n='\x1b[32m2\x1b[0m'
elif second2==o:
    o='\x1b[32m2\x1b[0m'
elif second2==p:
    p='\x1b[32m2\x1b[0m'

board=f'''
 {a} | {b} | {c} | {d}
---------------
 {e} | {f} | {g} | {h}
---------------
 {i} | {j} | {k} | {l}
---------------
 {m} | {n} | {o} | {p}
'''
print(board)


while True:
    #geser
    datagerakan=input('masukan gerakan (w,a,s,d) = ')

