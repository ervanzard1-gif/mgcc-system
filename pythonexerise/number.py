
import math
a=-11
print(abs(a))


a=12.2
print(math.ceil(a))
print(math.floor(a))

a=2
print(math.exp(a))

a=2
b=3
print(math.pow(a,b))

a=-6
print(math.fabs(a))


a=8
print(math.log2(a))

a=16
print(math.sqrt(a))

a=(65,3,6,9,4,3)
print(max(a))
print(min(a))


a=8.794
print(round(a,2))

a=6.52
pecahan,bulat=math.modf(a)
print(round(pecahan,2))
print(pecahan)
print(bulat)


import random
x=(4,2,6,5,7,9,5,3)
print(random.choice(x))

x=['ayam','bebek','cacing']#bisa juga pake tuple
print(random.choice(x))

x=random.randint(1,100)
print(x)
x=random.randrange(1,100,10)
print(x)


x=['ayam','bebek','cacing']
random.shuffle(x)
print(x)

random.seed(42)
print(random.random())
random.seed()
print(random.random())

print(random.uniform(5,4))