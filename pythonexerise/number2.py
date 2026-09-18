import random
random.seed(42)
print(random.random())

data1=random.randrange(1,100)
print(data1)

data2=random.randrange(1,100)
print(data2)
data=random.uniform(1,5)
print(data)


# abs dan fabs
import math
a=7+5j
print(abs(a))
#print(math.fabs(a)) tidak bisa complex


a=1/2
print(round(math.degrees(math.acos(a))))
a=math.pi/2
print(math.cos(a))
a=math.radians(90)
print(math.cos(a))

a=-10
b=-10
print(math.degrees(math.atan2(a,b)))


a=6
b=8
print(math.hypot(a,b))

print(math.e)
print(math.pi)