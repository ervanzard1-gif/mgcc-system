import random
a1='a1'
a2='a2'
a3='a3'
a4='a4'
a5='a5'
a6='a6'
a7='a7'
a8='a8'
a9='a9'

b1='b1'
b2='b2'
b3='b3'
b4='b4'
b5='b5'
b6='b6'
b7='b7'
b8='b8'
b9='b9'

c1='c1'
c2='c2'
c3='c3'
c4='c4'
c5='c5'
c6='c6'
c7='c7'
c8='c8'
c9='c9'

d1='d1'
d2='d2'
d3='d3'
d4='d4'
d5='d5'
d6='d6'
d7='d7'
d8='d8'
d9='d9'

e1='e1'
e2='e2'
e3='e3'
e4='e4'
e5='e5'
e6='e6'
e7='e7'
e8='e8'
e9='e9'

f1='f1'
f2='f2'
f3='f3'
f4='f4'
f5='f5'
f6='f6'
f7='f7'
f8='f8'
f9='f9'

g1='g1'
g2='g2'
g3='g3'
g4='g4'
g5='g5'
g6='g6'
g7='g7'
g8='g8'
g9='g9'

dataa=[1,2,3,4,5,6,7,8,9]
a1=random.choice(dataa)
dataa.remove(a1)


a2=random.choice(dataa)
dataa.remove(a2)


a3=random.choice(dataa)
dataa.remove(a3)


a4=random.choice(dataa)
dataa.remove(a4)


a5=random.choice(dataa)
dataa.remove(a5)


a6=random.choice(dataa)
dataa.remove(a6)


a7=random.choice(dataa)
dataa.remove(a7)


a8=random.choice(dataa)
dataa.remove(a8)


a9=random.choice(dataa)
dataa.remove(a9)


datab=[1,2,3,4,5,6,7,8,9]
# B
while True:
    b1=random.choice(datab)
    if b1==a1:
        continue
    elif b1!=a1:
        datab.remove(b1)
        break

while True:
    b2=random.choice(datab)
    if b2==a2:
        continue
    elif b2!=a2:
        datab.remove(b2)
        break

while True:
    b3=random.choice(datab)
    if b3==a3:
        continue
    elif b3!=a3:
        datab.remove(b3)
        break

while True:
    b4=random.choice(datab)
    if b4==a4:
        continue
    elif b4!=a4:
        datab.remove(b4)
        break

while True:
    b5=random.choice(datab)
    if b5==a5:
        continue
    elif b5!=a5:
        datab.remove(b5)
        break

while True:
    b6=random.choice(datab)
    if b6==a6:
        continue
    elif b6!=a6:
        datab.remove(b6)
        break

while True:
    b7=random.choice(datab)
    if b7==a7:
        continue
    elif b7!=a7:
        datab.remove(b7)
        break

while True:
    b8=random.choice(datab)
    if b8==a8:
        continue
    elif b8!=a8:
        datab.remove(b8)
        break

while True:
    b9=random.choice(datab)
    if b9==a9:
        continue
    elif b9!=a9:
        datab.remove(b9)
        break


datac=[1,2,3,4,5,6,7,8,9]
# C
while True:
    c1=random.choice(datac)
    if c1==a1 or c1==b1:
        continue
    elif c1!=a1 and c1!=b1:
        datac.remove(c1)
        break

while True:
    c2=random.choice(datac)
    if c2==a2 or c2==b2:
        continue
    elif c2!=a2 and c2!=b2:
        datac.remove(c2)
        break

while True:
    c3=random.choice(datac)
    if c3==a3 or c3==b3:
        continue
    elif c3!=a3 and c3!=b3:
        datac.remove(c3)
        break

while True:
    c4=random.choice(datac)
    if c4==a4 or c4==b4:
        continue
    elif c4!=a4 and c4!=b4:
        datac.remove(c4)
        break

while True:
    c5=random.choice(datac)
    if c5==a5 or c5==b5:
        continue
    elif c5!=a5 and c5!=b5:
        datac.remove(c5)
        break

while True:
    c6=random.choice(datac)
    if c6==a6 or c6==b6:
        continue
    elif c6!=a6 and c6!=b6:
        datac.remove(c6)
        break

while True:
    c7=random.choice(datac)
    if c7==a7 or c7==b7:
        continue
    elif c7!=a7 and c7!=b7:
        datac.remove(c7)
        break

while True:
    c8=random.choice(datac)
    if c8==a8 or c8==b8:
        continue
    elif c8!=a8 and c8!=b8:
        datac.remove(c8)
        break

while True:
    c9=random.choice(datac)
    if c9==a9 or c9==b9:
        continue
    elif c9!=a9 and c9!=b9:
        datac.remove(c9)
        break


datad=[1,2,3,4,5,6,7,8,9]
# D
while True:
    d1=random.choice(datad)
    if d1==a1 or d1==b1 or d1==c1:
        continue
    elif d1!=a1 and d1!=b1 and d1!=c1:
        datad.remove(d1)
        break

while True:
    d2=random.choice(datad)
    if d2==a2 or d2==b2 or d2==c2:
        continue
    elif d2!=a2 and d2!=b2 and d2!=c2:
        datad.remove(d2)
        break

while True:
    d3=random.choice(datad)
    if d3==a3 or d3==b3 or d3==c3:
        continue
    elif d3!=a3 and d3!=b3 and d3!=c3:
        datad.remove(d3)
        break

while True:
    d4=random.choice(datad)
    if d4==a4 or d4==b4 or d4==c4:
        continue
    elif d4!=a4 and d4!=b4 and d4!=c4:
        datad.remove(d4)
        break

while True:
    d5=random.choice(datad)
    if d5==a5 or d5==b5 or d5==c5:
        continue
    elif d5!=a5 and d5!=b5 and d5!=c5:
        datad.remove(d5)
        break

while True:
    d6=random.choice(datad)
    if d6==a6 or d6==b6 or d6==c6:
        continue
    elif d6!=a6 and d6!=b6 and d6!=c6:
        datad.remove(d6)
        break

while True:
    d7=random.choice(datad)
    if d7==a7 or d7==b7 or d7==c7:
        continue
    elif d7!=a7 and d7!=b7 and d7!=c7:
        datad.remove(d7)
        break

while True:
    d8=random.choice(datad)
    if d8==a8 or d8==b8 or d8==c8:
        continue
    elif d8!=a8 and d8!=b8 and d8!=c8:
        datad.remove(d8)
        break

while True:
    d9=random.choice(datad)
    if d9==a9 or d9==b9 or d9==c9:
        continue
    elif d9!=a9 and d9!=b9 and d9!=c9:
        datad.remove(d9)
        break


datae=[1,2,3,4,5,6,7,8,9]
# E
while True:
    e1=random.choice(datae)
    if e1==a1 or e1==b1 or e1==c1 or e1==d1:
        continue
    elif e1!=a1 and e1!=b1 and e1!=c1 and e1!=d1:
        datae.remove(e1)
        break

while True:
    e2=random.choice(datae)
    if e2==a2 or e2==b2 or e2==c2 or e2==d2:
        continue
    elif e2!=a2 and e2!=b2 and e2!=c2 and e2!=d2:
        datae.remove(e2)
        break

while True:
    e3=random.choice(datae)
    if e3==a3 or e3==b3 or e3==c3 or e3==d3:
        continue
    elif e3!=a3 and e3!=b3 and e3!=c3 and e3!=d3:
        datae.remove(e3)
        break

while True:
    e4=random.choice(datae)
    if e4==a4 or e4==b4 or e4==c4 or e4==d4:
        continue
    elif e4!=a4 and e4!=b4 and e4!=c4 and e4!=d4:
        datae.remove(e4)
        break

while True:
    e5=random.choice(datae)
    if e5==a5 or e5==b5 or e5==c5 or e5==d5:
        continue
    elif e5!=a5 and e5!=b5 and e5!=c5 and e5!=d5:
        datae.remove(e5)
        break

while True:
    e6=random.choice(datae)
    if e6==a6 or e6==b6 or e6==c6 or e6==d6:
        continue
    elif e6!=a6 and e6!=b6 and e6!=c6 and e6!=d6:
        datae.remove(e6)
        break

while True:
    e7=random.choice(datae)
    if e7==a7 or e7==b7 or e7==c7 or e7==d7:
        continue
    elif e7!=a7 and e7!=b7 and e7!=c7 and e7!=d7:
        datae.remove(e7)
        break

while True:
    e8=random.choice(datae)
    if e8==a8 or e8==b8 or e8==c8 or e8==d8:
        continue
    elif e8!=a8 and e8!=b8 and e8!=c8 and e8!=d8:
        datae.remove(e8)
        break

while True:
    e9=random.choice(datae)
    if e9==a9 or e9==b9 or e9==c9 or e9==d9:
        continue
    elif e9!=a9 and e9!=b9 and e9!=c9 and e9!=d9:
        datae.remove(e9)
        break


dataf=[1,2,3,4,5,6,7,8,9]
# F
while True:
    f1=random.choice(dataf)
    if f1==a1 or f1==b1 or f1==c1 or f1==d1 or f1==e1:
        continue
    elif f1!=a1 and f1!=b1 and f1!=c1 and f1!=d1 and f1!=e1:
        dataf.remove(f1)
        break

while True:
    f2=random.choice(dataf)
    if f2==a2 or f2==b2 or f2==c2 or f2==d2 or f2==e2:
        continue
    elif f2!=a2 and f2!=b2 and f2!=c2 and f2!=d2 and f2!=e2:
        dataf.remove(f2)
        break

while True:
    f3=random.choice(dataf)
    if f3==a3 or f3==b3 or f3==c3 or f3==d3 or f3==e3:
        continue
    elif f3!=a3 and f3!=b3 and f3!=c3 and f3!=d3 and f3!=e3:
        dataf.remove(f3)
        break

while True:
    f4=random.choice(dataf)
    if f4==a4 or f4==b4 or f4==c4 or f4==d4 or f4==e4:
        continue
    elif f4!=a4 and f4!=b4 and f4!=c4 and f4!=d4 and f4!=e4:
        dataf.remove(f4)
        break

while True:
    f5=random.choice(dataf)
    if f5==a5 or f5==b5 or f5==c5 or f5==d5 or f5==e5:
        continue
    elif f5!=a5 and f5!=b5 and f5!=c5 and f5!=d5 and f5!=e5:
        dataf.remove(f5)
        break

while True:
    f6=random.choice(dataf)
    if f6==a6 or f6==b6 or f6==c6 or f6==d6 or f6==e6:
        continue
    elif f6!=a6 and f6!=b6 and f6!=c6 and f6!=d6 and f6!=e6:
        dataf.remove(f6)
        break

while True:
    f7=random.choice(dataf)
    if f7==a7 or f7==b7 or f7==c7 or f7==d7 or f7==e7:
        continue
    elif f7!=a7 and f7!=b7 and f7!=c7 and f7!=d7 and f7!=e7:
        dataf.remove(f7)
        break

while True:
    f8=random.choice(dataf)
    if f8==a8 or f8==b8 or f8==c8 or f8==d8 or f8==e8:
        continue
    elif f8!=a8 and f8!=b8 and f8!=c8 and f8!=d8 and f8!=e8:
        dataf.remove(f8)
        break

while True:
    f9=random.choice(dataf)
    if f9==a9 or f9==b9 or f9==c9 or f9==d9 or f9==e9:
        continue
    elif f9!=a9 and f9!=b9 and f9!=c9 and f9!=d9 and f9!=e9:
        dataf.remove(f9)
        break


datag=[1,2,3,4,5,6,7,8,9]
# G
while True:
    g1=random.choice(datag)
    if g1==a1 or g1==b1 or g1==c1 or g1==d1 or g1==e1 or g1==f1:
        continue
    elif g1!=a1 and g1!=b1 and g1!=c1 and g1!=d1 and g1!=e1 and g1!=f1:
        datag.remove(g1)
        break

while True:
    g2=random.choice(datag)
    if g2==a2 or g2==b2 or g2==c2 or g2==d2 or g2==e2 or g2==f2:
        continue
    elif g2!=a2 and g2!=b2 and g2!=c2 and g2!=d2 and g2!=e2 and g2!=f2:
        datag.remove(g2)
        break

while True:
    g3=random.choice(datag)
    if g3==a3 or g3==b3 or g3==c3 or g3==d3 or g3==e3 or g3==f3:
        continue
    elif g3!=a3 and g3!=b3 and g3!=c3 and g3!=d3 and g3!=e3 and g3!=f3:
        datag.remove(g3)
        break

while True:
    g4=random.choice(datag)
    if g4==a4 or g4==b4 or g4==c4 or g4==d4 or g4==e4 or g4==f4:
        continue
    elif g4!=a4 and g4!=b4 and g4!=c4 and g4!=d4 and g4!=e4 and g4!=f4:
        datag.remove(g4)
        break

while True:
    g5=random.choice(datag)
    if g5==a5 or g5==b5 or g5==c5 or g5==d5 or g5==e5 or g5==f5:
        continue
    elif g5!=a5 and g5!=b5 and g5!=c5 and g5!=d5 and g5!=e5 and g5!=f5:
        datag.remove(g5)
        break

while True:
    g6=random.choice(datag)
    if g6==a6 or g6==b6 or g6==c6 or g6==d6 or g6==e6 or g6==f6:
        continue
    elif g6!=a6 and g6!=b6 and g6!=c6 and g6!=d6 and g6!=e6 and g6!=f6:
        datag.remove(g6)
        break

while True:
    g7=random.choice(datag)
    if g7==a7 or g7==b7 or g7==c7 or g7==d7 or g7==e7 or g7==f7:
        continue
    elif g7!=a7 and g7!=b7 and g7!=c7 and g7!=d7 and g7!=e7 and g7!=f7:
        datag.remove(g7)
        break

while True:
    g8=random.choice(datag)
    if g8==a8 or g8==b8 or g8==c8 or g8==d8 or g8==e8 or g8==f8:
        continue
    elif g8!=a8 and g8!=b8 and g8!=c8 and g8!=d8 and g8!=e8 and g8!=f8:
        datag.remove(g8)
        break

while True:
    g9=random.choice(datag)
    if g9==a9 or g9==b9 or g9==c9 or g9==d9 or g9==e9 or g9==f9:
        continue
    elif g9!=a9 and g9!=b9 and g9!=c9 and g9!=d9 and g9!=e9 and g9!=f9:
        datag.remove(g9)
        break


datah=[1,2,3,4,5,6,7,8,9]
# H
while True:
    h1=random.choice(datah)
    if h1==a1 or h1==b1 or h1==c1 or h1==d1 or h1==e1 or h1==f1 or h1==g1:
        continue
    elif h1!=a1 and h1!=b1 and h1!=c1 and h1!=d1 and h1!=e1 and h1!=f1 and h1!=g1:
        datah.remove(h1)
        break

while True:
    h2=random.choice(datah)
    if h2==a2 or h2==b2 or h2==c2 or h2==d2 or h2==e2 or h2==f2 or h2==g2:
        continue
    elif h2!=a2 and h2!=b2 and h2!=c2 and h2!=d2 and h2!=e2 and h2!=f2 and h2!=g2:
        datah.remove(h2)
        break

while True:
    h3=random.choice(datah)
    if h3==a3 or h3==b3 or h3==c3 or h3==d3 or h3==e3 or h3==f3 or h3==g3:
        continue
    elif h3!=a3 and h3!=b3 and h3!=c3 and h3!=d3 and h3!=e3 and h3!=f3 and h3!=g3:
        datah.remove(h3)
        break

while True:
    h4=random.choice(datah)
    if h4==a4 or h4==b4 or h4==c4 or h4==d4 or h4==e4 or h4==f4 or h4==g4:
        continue
    elif h4!=a4 and h4!=b4 and h4!=c4 and h4!=d4 and h4!=e4 and h4!=f4 and h4!=g4:
        datah.remove(h4)
        break

while True:
    h5=random.choice(datah)
    if h5==a5 or h5==b5 or h5==c5 or h5==d5 or h5==e5 or h5==f5 or h5==g5:
        continue
    elif h5!=a5 and h5!=b5 and h5!=c5 and h5!=d5 and h5!=e5 and h5!=f5 and h5!=g5:
        datah.remove(h5)
        break

while True:
    h6=random.choice(datah)
    if h6==a6 or h6==b6 or h6==c6 or h6==d6 or h6==e6 or h6==f6 or h6==g6:
        continue
    elif h6!=a6 and h6!=b6 and h6!=c6 and h6!=d6 and h6!=e6 and h6!=f6 and h6!=g6:
        datah.remove(h6)
        break

while True:
    h7=random.choice(datah)
    if h7==a7 or h7==b7 or h7==c7 or h7==d7 or h7==e7 or h7==f7 or h7==g7:
        continue
    elif h7!=a7 and h7!=b7 and h7!=c7 and h7!=d7 and h7!=e7 and h7!=f7 and h7!=g7:
        datah.remove(h7)
        break

while True:
    h8=random.choice(datah)
    if h8==a8 or h8==b8 or h8==c8 or h8==d8 or h8==e8 or h8==f8 or h8==g8:
        continue
    elif h8!=a8 and h8!=b8 and h8!=c8 and h8!=d8 and h8!=e8 and h8!=f8 and h8!=g8:
        datah.remove(h8)
        break

while True:
    h9=random.choice(datah)
    if h9==a9 or h9==b9 or h9==c9 or h9==d9 or h9==e9 or h9==f9 or h9==g9:
        continue
    elif h9!=a9 and h9!=b9 and h9!=c9 and h9!=d9 and h9!=e9 and h9!=f9 and h9!=g9:
        datah.remove(h9)
        break


datai=[1,2,3,4,5,6,7,8,9]
# I
while True:
    i1=random.choice(datai)
    if i1==a1 or i1==b1 or i1==c1 or i1==d1 or i1==e1 or i1==f1 or i1==g1 or i1==h1:
        continue
    elif i1!=a1 and i1!=b1 and i1!=c1 and i1!=d1 and i1!=e1 and i1!=f1 and i1!=g1 and i1!=h1:
        datai.remove(i1)
        break

while True:
    i2=random.choice(datai)
    if i2==a2 or i2==b2 or i2==c2 or i2==d2 or i2==e2 or i2==f2 or i2==g2 or i2==h2:
        continue
    elif i2!=a2 and i2!=b2 and i2!=c2 and i2!=d2 and i2!=e2 and i2!=f2 and i2!=g2 and i2!=h2:
        datai.remove(i2)
        break

while True:
    i3=random.choice(datai)
    if i3==a3 or i3==b3 or i3==c3 or i3==d3 or i3==e3 or i3==f3 or i3==g3 or i3==h3:
        continue
    elif i3!=a3 and i3!=b3 and i3!=c3 and i3!=d3 and i3!=e3 and i3!=f3 and i3!=g3 and i3!=h3:
        datai.remove(i3)
        break

while True:
    i4=random.choice(datai)
    if i4==a4 or i4==b4 or i4==c4 or i4==d4 or i4==e4 or i4==f4 or i4==g4 or i4==h4:
        continue
    elif i4!=a4 and i4!=b4 and i4!=c4 and i4!=d4 and i4!=e4 and i4!=f4 and i4!=g4 and i4!=h4:
        datai.remove(i4)
        break

while True:
    i5=random.choice(datai)
    if i5==a5 or i5==b5 or i5==c5 or i5==d5 or i5==e5 or i5==f5 or i5==g5 or i5==h5:
        continue
    elif i5!=a5 and i5!=b5 and i5!=c5 and i5!=d5 and i5!=e5 and i5!=f5 and i5!=g5 and i5!=h5:
        datai.remove(i5)
        break

while True:
    i6=random.choice(datai)
    if i6==a6 or i6==b6 or i6==c6 or i6==d6 or i6==e6 or i6==f6 or i6==g6 or i6==h6:
        continue
    elif i6!=a6 and i6!=b6 and i6!=c6 and i6!=d6 and i6!=e6 and i6!=f6 and i6!=g6 and i6!=h6:
        datai.remove(i6)
        break

while True:
    i7=random.choice(datai)
    if i7==a7 or i7==b7 or i7==c7 or i7==d7 or i7==e7 or i7==f7 or i7==g7 or i7==h7:
        continue
    elif i7!=a7 and i7!=b7 and i7!=c7 and i7!=d7 and i7!=e7 and i7!=f7 and i7!=g7 and i7!=h7:
        datai.remove(i7)
        break

while True:
    i8=random.choice(datai)
    if i8==a8 or i8==b8 or i8==c8 or i8==d8 or i8==e8 or i8==f8 or i8==g8 or i8==h8:
        continue
    elif i8!=a8 and i8!=b8 and i8!=c8 and i8!=d8 and i8!=e8 and i8!=f8 and i8!=g8 and i8!=h8:
        datai.remove(i8)
        break

while True:
    i9=random.choice(datai)
    if i9==a9 or i9==b9 or i9==c9 or i9==d9 or i9==e9 or i9==f9 or i9==g9 or i9==h9:
        continue
    elif i9!=a9 and i9!=b9 and i9!=c9 and i9!=d9 and i9!=e9 and i9!=f9 and i9!=g9 and i9!=h9:
        datai.remove(i9)
        break













board=f'''
| {a1} | {b1} | {c1} | {d1} | {e1} | {f1} | {g1} | {h1} | {i1} |
-------------------------------------

| {a2} | {b2} | {c2} | {d2} | {e2} | {f2} | {g2} | {h2} | {i2} |
-------------------------------------
| {a3} | {b3} | {c3} | {d3} | {e3} | {f3} | {g3} | {h3} | {i3} |
-------------------------------------
| {a4} | {b4} | {c4} | {d4} | {e4} | {f4} | {g4} | {h4} | {i4} |
-------------------------------------
| {a5} | {b5} | {c5} | {d5} | {e5} | {f5} | {g5} | {h5} | {i5} |
-------------------------------------
| {a6} | {b6} | {c6} | {d6} | {e6} | {f6} | {g6} | {h6} | {i6} |
-------------------------------------
| {a7} | {b7} | {c7} | {d7} | {e7} | {f7} | {g7} | {h7} | {i7} |
-------------------------------------
| {a8} | {b8} | {c8} | {d8} | {e8} | {f8} | {g8} | {h8} | {i8} |
-------------------------------------
| {a9} | {b9} | {c9} | {d9} | {e9} | {f9} | {g9} | {h9} | {i9} |


'''
print(board)



