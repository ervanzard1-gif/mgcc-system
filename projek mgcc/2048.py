#2048
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

    if datagerakan=='w':
        #if a=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or a=='x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
        #    a='\x1b[32m2\x1b[0m'
        #    e='e'
        #    i='i'
        #    m='m'
        if a=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m':
            if a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                e='\x1b[32m8\x1b[0m'
                i='i'
                m='m'

            elif a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                e='\x1b[32m4\x1b[0m'
                i='i'
                m='m'
                 
            elif a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                e='e'
                i='i'
                m='m'
        elif a=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m':
            
            if a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                e='\x1b[32m4\x1b[0m'
                i='i'
                m='m'

            elif a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                e='\x1b[32m2\x1b[0m'
                i='i'
                m='m'
                 
            elif a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                e='e'
                i='i'
                m='m'

            
        if f=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m':
            if f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m':
                b='\x1b[32m8\x1b[0m'
                f='\x1b[32m8\x1b[0m'
                j='j'
                n='n'
            elif f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m':
                b='\x1b[32m8\x1b[0m'
                f='\x1b[32m4\x1b[0m'
                j='j'
                n='n'
            elif f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m':
                b='\x1b[32m8\x1b[0m'
                f='f'
                j='j'
                n='n'
        elif f=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m':
    
            if f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m':
                b='\x1b[32m4\x1b[0m'
                f='\x1b[32m4\x1b[0m'
                j='j'
                n='n'
            elif f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m':
                b='\x1b[32m4\x1b[0m'
                f='\x1b[32m2\x1b[0m'
                j='j'
                n='n'
            elif f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m':
                b='\x1b[32m4\x1b[0m'
                f='f'
                j='j'
                n='n'
    
            
        if g=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m':
            if g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                c='\x1b[32m8\x1b[0m'
                g='\x1b[32m4\x1b[0m'
                k='k'
                o='o'
            elif g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                c='\x1b[32m8\x1b[0m'
                g='\x1b[32m4\x1b[0m'
                k='k'
                o='o'
            elif g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                c='\x1b[32m8\x1b[0m'
                g='g'
                k='k'
                o='o'
        elif g=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m':
            if g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                c='\x1b[32m4\x1b[0m'
                g='\x1b[32m4\x1b[0m'
                k='k'
                o='o'
            elif g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                c='\x1b[32m4\x1b[0m'
                g='\x1b[32m2\x1b[0m'
                k='k'
                o='o'
            elif g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                c='\x1b[32m4\x1b[0m'
                g='g'
                k='k'
                o='o'
     
           
            
        if h=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' or p=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m':
            if h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                h='\x1b[32m8\x1b[0m'
                l='l'
                p='p'
            elif h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                h='\x1b[32m4\x1b[0m'
                l='l'
                p='p'
            elif h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m' or p=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                h='h'
                l='l'
                p='p'
        elif h=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' or p=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m':
            if h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                h='\x1b[32m4\x1b[0m'
                l='l'
                p='p'
            elif h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                h='\x1b[32m2\x1b[0m'
                l='l'
                p='p'
            elif h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' or p=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                h='h'
                l='l'
                p='p'
      
        while True:
            next2=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
            if next2=='a' and a=='a':
                a='\x1b[32m2\x1b[0m'
                break
            elif next2=='b' and b=='b':
                b='\x1b[32m2\x1b[0m'
                break
            elif next2=='c' and c=='c':
                c='\x1b[32m2\x1b[0m'
                break
            elif next2=='d' and d=='d':
                d='\x1b[32m2\x1b[0m'
                break
            elif next2=='e' and e=='e':
                e='\x1b[32m2\x1b[0m'
                break
            elif next2=='f' and f=='f':
                f='\x1b[32m2\x1b[0m'
                break
            elif next2=='g' and g=='g':
                g='\x1b[32m2\x1b[0m'
                break
            elif next2=='h' and h=='h':
                h='\x1b[32m2\x1b[0m'
                break
            elif next2=='i' and i=='i':
                i='\x1b[32m2\x1b[0m'
                break
            elif next2=='j' and j=='j':
                j='\x1b[32m2\x1b[0m'
                break
            elif next2=='k' and k=='k':
                k='\x1b[32m2\x1b[0m'
                break
            elif next2=='l' and l=='l':
                l='\x1b[32m2\x1b[0m'
                break
            elif next2=='m' and m=='m':
                m='\x1b[32m2\x1b[0m'
                break
            elif next2=='n' and n=='n':
                n='\x1b[32m2\x1b[0m'
                break
            elif next2=='o' and o=='o':
                o='\x1b[32m2\x1b[0m'
                break
            elif next2=='p' and p=='p':
                p='\x1b[32m2\x1b[0m'
                break
            

  
        board1=f'''
         {a} | {b} | {c} | {d}
        ---------------
         {e} | {f} | {g} | {h}
        ---------------
         {i} | {j} | {k} | {l}
        ---------------
         {m} | {n} | {o} | {p}
        '''
        print(board1)

    if datagerakan=='s':
        if a=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m':
           if a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                i='\x1b[32m8\x1b[0m'
                a='a'
                e='e'
            
           elif a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                i='\x1b[32m4\x1b[0m'
                a='a'
                e='e'
           elif a=='\x1b[32m4\x1b[0m' and e=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and m=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                a='a'
                e='e'
                i='i'
        elif a=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m':
            
           if a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                i='\x1b[32m4\x1b[0m'
                a='a'
                e='e'
            
           elif a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                i='\x1b[32m2\x1b[0m'
                a='a'
                e='e'
           elif a=='\x1b[32m2\x1b[0m' and e=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and m=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                a='a'
                e='e'
                i='i'
            
        if b=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m':
            if b=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m':
                n='\x1b[32m8\x1b[0m'
                j='\x1b[32m8\x1b[0m'
                b='b'
                f='f'
                       
            elif b=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m':
                n='\x1b[32m8\x1b[0m'
                j='\x1b[32m4\x1b[0m'
                b='b'
                f='f'
            elif b=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m':
                n='\x1b[32m8\x1b[0m'
                b='b'
                f='f'
                j='j' 
        elif b=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m':
            if b=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m':
                n='\x1b[32m4\x1b[0m'
                j='\x1b[32m4\x1b[0m'
                b='b'
                f='f'
                       
            elif b=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m':
                n='\x1b[32m4\x1b[0m'
                j='\x1b[32m2\x1b[0m'
                b='b'
                f='f'
            elif b=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m':
                n='\x1b[32m4\x1b[0m'
                b='b'
                f='f'
                j='j' 
            
        if c=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m':
           if c=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m':
                k='\x1b[32m8\x1b[0m'
                o='\x1b[32m8\x1b[0m'
                c='c'
                g='g'
            
           elif c=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m':
                o='\x1b[32m8\x1b[0m'
                k='\x1b[32m4\x1b[0m'
                c='c'
                g='g'
           elif c=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m':
                o='\x1b[32m8\x1b[0m'
                c='c'
                g='g'
                k='k'
        elif c=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m':
           if c=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m':
                k='\x1b[32m4\x1b[0m'
                o='\x1b[32m4\x1b[0m'
                c='c'
                g='g'
            
           elif c=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m':
                o='\x1b[32m4\x1b[0m'
                k='\x1b[32m2\x1b[0m'
                c='c'
                g='g'
           elif c=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m':
                o='\x1b[32m4\x1b[0m'
                c='c'
                g='g'
                k='k'
           
        if h=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' or p=='\x1b[32m4\x1b[0m':
           if d=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                l='\x1b[32m8\x1b[0m'
                d='d'
                h='h'
            
           elif d=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                l='\x1b[32m4\x1b[0m'
                d='d'
                h='h'
           elif d=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                d='d'
                h='h'
                l='l'
        elif h=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' or p=='\x1b[32m2\x1b[0m':
           if d=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                l='\x1b[32m4\x1b[0m'
                d='d'
                h='h'
            
           elif d=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                l='\x1b[32m2\x1b[0m'
                d='d'
                h='h'
           elif d=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                d='d'
                h='h'
                l='l'
       
        while True:
            next2=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
            if next2=='a' and a=='a':
                a='\x1b[32m2\x1b[0m'
                break
            elif next2=='b' and b=='b':
                b='\x1b[32m2\x1b[0m'
                break
            elif next2=='c' and c=='c':
                c='\x1b[32m2\x1b[0m'
                break
            elif next2=='d' and d=='d':
                d='\x1b[32m2\x1b[0m'
                break
            elif next2=='e' and e=='e':
                e='\x1b[32m2\x1b[0m'
                break
            elif next2=='f' and f=='f':
                f='\x1b[32m2\x1b[0m'
                break
            elif next2=='g' and g=='g':
                g='\x1b[32m2\x1b[0m'
                break
            elif next2=='h' and h=='h':
                h='\x1b[32m2\x1b[0m'
                break
            elif next2=='i' and i=='i':
                i='\x1b[32m2\x1b[0m'
                break
            elif next2=='j' and j=='j':
                j='\x1b[32m2\x1b[0m'
                break
            elif next2=='k' and k=='k':
                k='\x1b[32m2\x1b[0m'
                break
            elif next2=='l' and l=='l':
                l='\x1b[32m2\x1b[0m'
                break
            elif next2=='m' and m=='m':
                m='\x1b[32m2\x1b[0m'
                break
            elif next2=='n' and n=='n':
                n='\x1b[32m2\x1b[0m'
                break
            elif next2=='o' and o=='o':
                o='\x1b[32m2\x1b[0m'
                break
            elif next2=='p' and p=='p':
                p='\x1b[32m2\x1b[0m'
                break
            

  
        board1=f'''
         {a} | {b} | {c} | {d}
        ---------------
         {e} | {f} | {g} | {h}
        ---------------
         {i} | {j} | {k} | {l}
        ---------------
         {m} | {n} | {o} | {p}
        '''
        print(board1)

    if datagerakan=='d':
        if a=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m':
           if d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                c='\x1b[32m8\x1b[0m'
                a='a'
                b='b'
            
           elif d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                c='\x1b[32m4\x1b[0m'
                a='a'
                b='b'
           elif d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m':
                d='\x1b[32m8\x1b[0m'
                a='a'
                b='b'
                c='c'
        elif a=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m':
           if d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                c='\x1b[32m4\x1b[0m'
                a='a'
                b='b'
            
           elif d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                c='\x1b[32m2\x1b[0m'
                a='a'
                b='b'
           elif d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
                d='\x1b[32m4\x1b[0m'
                a='a'
                b='b'
                c='c'
            
            
        if e=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m':
           if e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                h='\x1b[32m8\x1b[0m'
                g='\x1b[32m8\x1b[0m'
                e='e'
                f='f'
            
           elif e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                h='\x1b[32m8\x1b[0m'
                g='\x1b[32m4\x1b[0m'
                e='e'
                f='f'
           elif e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                h='\x1b[32m8\x1b[0m'
                g='g'
                e='e'
                f='f'
        elif e=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m':
           if e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                h='\x1b[32m4\x1b[0m'
                g='\x1b[32m4\x1b[0m'
                e='e'
                f='f'
            
           elif e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                h='\x1b[32m4\x1b[0m'
                g='\x1b[32m2\x1b[0m'
                e='e'
                f='f'
           elif e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                h='\x1b[32m4\x1b[0m'
                g='g'
                e='e'
                f='f'
           
            
        if i=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' or l=='\x1b[32m4\x1b[0m':
           if i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                l='\x1b[32m8\x1b[0m'
                k='\x1b[32m8\x1b[0m'
                i='i'
                j='j'
            
           elif i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                l='\x1b[32m8\x1b[0m'
                k='\x1b[32m4\x1b[0m'
                i='i'
                j='j'
           elif j=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                l='\x1b[32m8\x1b[0m'
                k='k'
                i='i'
                j='j'
        elif i=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' or l=='\x1b[32m2\x1b[0m':
           if i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                l='\x1b[32m4\x1b[0m'
                k='\x1b[32m4\x1b[0m'
                i='i'
                j='j'
            
           elif i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                l='\x1b[32m4\x1b[0m'
                k='\x1b[32m2\x1b[0m'
                i='i'
                j='j'
           elif j=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                l='\x1b[32m4\x1b[0m'
                k='k'
                i='i'
                j='j'
           
        if m=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m' or p=='\x1b[32m4\x1b[0m':
           if m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                o='\x1b[32m8\x1b[0m'
                n='n'
                m='m'
            
           elif m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                o='\x1b[32m4\x1b[0m'
                n='n'
                m='m'
           elif m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                p='\x1b[32m8\x1b[0m'
                o='o'
                n='n'
                m='m'
        elif m=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m' or p=='\x1b[32m2\x1b[0m':
           if m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                o='\x1b[32m4\x1b[0m'
                n='n'
                m='m'
            
           elif m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                o='\x1b[32m2\x1b[0m'
                n='n'
                m='m'
           elif m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                p='\x1b[32m4\x1b[0m'
                o='o'
                n='n'
                m='m'
        while True:
            next2=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
            if next2=='a' and a=='a':
                a='\x1b[32m2\x1b[0m'
                break
            elif next2=='b' and b=='b':
                b='\x1b[32m2\x1b[0m'
                break
            elif next2=='c' and c=='c':
                c='\x1b[32m2\x1b[0m'
                break
            elif next2=='d' and d=='d':
                d='\x1b[32m2\x1b[0m'
                break
            elif next2=='e' and e=='e':
                e='\x1b[32m2\x1b[0m'
                break
            elif next2=='f' and f=='f':
                f='\x1b[32m2\x1b[0m'
                break
            elif next2=='g' and g=='g':
                g='\x1b[32m2\x1b[0m'
                break
            elif next2=='h' and h=='h':
                h='\x1b[32m2\x1b[0m'
                break
            elif next2=='i' and i=='i':
                i='\x1b[32m2\x1b[0m'
                break
            elif next2=='j' and j=='j':
                j='\x1b[32m2\x1b[0m'
                break
            elif next2=='k' and k=='k':
                k='\x1b[32m2\x1b[0m'
                break
            elif next2=='l' and l=='l':
                l='\x1b[32m2\x1b[0m'
                break
            elif next2=='m' and m=='m':
                m='\x1b[32m2\x1b[0m'
                break
            elif next2=='n' and n=='n':
                n='\x1b[32m2\x1b[0m'
                break
            elif next2=='o' and o=='o':
                o='\x1b[32m2\x1b[0m'
                break
            elif next2=='p' and p=='p':
                p='\x1b[32m2\x1b[0m'
                break
         
            

  
        board1=f'''
         {a} | {b} | {c} | {d}
        ---------------
         {e} | {f} | {g} | {h}
        ---------------
         {i} | {j} | {k} | {l}
        ---------------
         {m} | {n} | {o} | {p}
        '''
        print(board1)

    if datagerakan=='a':
        if a=='\x1b[32m4\x1b[0m' or b=='\x1b[32m4\x1b[0m' or c=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m':
           if a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                b='\x1b[32m8\x1b[0m'
                c='c'
                d='d'
            
           elif d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                b='\x1b[32m4\x1b[0m'
                c='c'
                d='d'
           elif d=='\x1b[32m4\x1b[0m' and a=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or d=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and b=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and c=='\x1b[32m4\x1b[0m' or a=='\x1b[32m4\x1b[0m' and d=='\x1b[32m4\x1b[0m':
                a='\x1b[32m8\x1b[0m'
                b='b'
                c='c'
                d='d'
        elif a=='\x1b[32m2\x1b[0m' or b=='\x1b[32m2\x1b[0m' or c=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m':
           if a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                b='\x1b[32m4\x1b[0m'
                c='c'
                d='d'
            
           elif d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                b='\x1b[32m2\x1b[0m'
                c='c'
                d='d'
           elif d=='\x1b[32m2\x1b[0m' and a=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or d=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and b=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and c=='\x1b[32m2\x1b[0m' or a=='\x1b[32m2\x1b[0m' and d=='\x1b[32m2\x1b[0m':
                a='\x1b[32m4\x1b[0m'
                b='b'
                c='c'
                d='d'
           

            
        if e=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' or h=='\x1b[32m4\x1b[0m':
           if e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                e='\x1b[32m8\x1b[0m'
                f='\x1b[32m8\x1b[0m'
                g='g'
                h='h'
            
           elif e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                e='\x1b[32m8\x1b[0m'
                f='\x1b[32m4\x1b[0m'
                g='g'
                h='h'
           elif e=='\x1b[32m4\x1b[0m' and f=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or e=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and g=='\x1b[32m4\x1b[0m' or f=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m' or g=='\x1b[32m4\x1b[0m' and h=='\x1b[32m4\x1b[0m':
                e='\x1b[32m8\x1b[0m'
                f='f'
                g='g'
                h='h'
        elif e=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' or h=='\x1b[32m2\x1b[0m':
           if e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                e='\x1b[32m4\x1b[0m'
                f='\x1b[32m4\x1b[0m'
                g='g'
                h='h'
            
           elif e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                e='\x1b[32m4\x1b[0m'
                f='\x1b[32m2\x1b[0m'
                g='g'
                h='h'
           elif e=='\x1b[32m2\x1b[0m' and f=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or e=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and g=='\x1b[32m2\x1b[0m' or f=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m' or g=='\x1b[32m2\x1b[0m' and h=='\x1b[32m2\x1b[0m':
                e='\x1b[32m4\x1b[0m'
                f='f'
                g='g'
                h='h'
           
        if i=='\x1b[32m4\x1b[0m' or  l=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m':
           if i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                i='\x1b[32m8\x1b[0m'
                j='\x1b[32m8\x1b[0m'
                k='k'
                l='l'
            
           elif i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and j=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                i='\x1b[32m8\x1b[0m'
                j='\x1b[32m4\x1b[0m'
                k='k'
                l='l'
           elif j=='\x1b[32m4\x1b[0m' and i=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or j=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and k=='\x1b[32m4\x1b[0m' or k=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m' or i=='\x1b[32m4\x1b[0m' and l=='\x1b[32m4\x1b[0m':
                i='\x1b[32m8\x1b[0m'
                j='a'
                k='k'
                l='l'
        elif i=='\x1b[32m2\x1b[0m' or  l=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m':
           if i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                i='\x1b[32m4\x1b[0m'
                j='\x1b[32m4\x1b[0m'
                k='k'
                l='l'
            
           elif i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and j=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                i='\x1b[32m4\x1b[0m'
                j='\x1b[32m2\x1b[0m'
                k='k'
                l='l'
           elif j=='\x1b[32m2\x1b[0m' and i=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or j=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and k=='\x1b[32m2\x1b[0m' or k=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m' or i=='\x1b[32m2\x1b[0m' and l=='\x1b[32m2\x1b[0m':
                i='\x1b[32m4\x1b[0m'
                j='a'
                k='k'
                l='l'
            
            
        if  m=='\x1b[32m4\x1b[0m' or  p=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m':
           if m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                n='\x1b[32m8\x1b[0m'
                o='o'
                p='p'
            
           elif m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                n='\x1b[32m4\x1b[0m'
                o='o'
                p='p'
           elif m=='\x1b[32m4\x1b[0m' and n=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or m=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and o=='\x1b[32m4\x1b[0m' or n=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m' or o=='\x1b[32m4\x1b[0m' and p=='\x1b[32m4\x1b[0m':
                m='\x1b[32m8\x1b[0m'
                n='n'
                o='o'
                p='p'
        elif  m=='\x1b[32m2\x1b[0m' or  p=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m':
           if m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                n='\x1b[32m4\x1b[0m'
                o='o'
                p='p'
            
           elif m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                n='\x1b[32m2\x1b[0m'
                o='o'
                p='p'
           elif m=='\x1b[32m2\x1b[0m' and n=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or m=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and o=='\x1b[32m2\x1b[0m' or n=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m' or o=='\x1b[32m2\x1b[0m' and p=='\x1b[32m2\x1b[0m':
                m='\x1b[32m4\x1b[0m'
                n='n'
                o='o'
                p='p'
        while True: 
            next2=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
            if next2=='a' and a=='a':
                a='\x1b[32m2\x1b[0m'
                break
            elif next2=='b' and b=='b':
                b='\x1b[32m2\x1b[0m'
                break
            elif next2=='c' and c=='c':
                c='\x1b[32m2\x1b[0m'
                break
            elif next2=='d' and d=='d':
                d='\x1b[32m2\x1b[0m'
                break
            elif next2=='e' and e=='e':
                e='\x1b[32m2\x1b[0m'
                break
            elif next2=='f' and f=='f':
                f='\x1b[32m2\x1b[0m'
                break
            elif next2=='g' and g=='g':
                g='\x1b[32m2\x1b[0m'
                break
            elif next2=='h' and h=='h':
                h='\x1b[32m2\x1b[0m'
                break
            elif next2=='i' and i=='i':
                i='\x1b[32m2\x1b[0m'
                break
            elif next2=='j' and j=='j':
                j='\x1b[32m2\x1b[0m'
                break
            elif next2=='k' and k=='k':
                k='\x1b[32m2\x1b[0m'
                break
            elif next2=='l' and l=='l':
                l='\x1b[32m2\x1b[0m'
                break
            elif next2=='m' and m=='m':
                m='\x1b[32m2\x1b[0m'
                break
            elif next2=='n' and n=='n':
                n='\x1b[32m2\x1b[0m'
                break
            elif next2=='o' and o=='o':
                o='\x1b[32m2\x1b[0m'
                break
            elif next2=='p' and p=='p':
                p='\x1b[32m2\x1b[0m'
                break
        

  
        board1=f'''
         {a} | {b} | {c} | {d}
        ---------------
         {e} | {f} | {g} | {h}
        ---------------
         {i} | {j} | {k} | {l}
        ---------------
         {m} | {n} | {o} | {p}
        '''
        print(board1)




    