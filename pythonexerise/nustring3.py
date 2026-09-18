data='ervanza'
print('%s' % (data))

data=126
print('%c'%data)

data=124
print('%s' % (data))
print('%s' % ('ayam'))

data=-23
print('%05d' % (data))
print('%5i' % (data))
print('%u' % (data))

data=10
print(('%o') % (data))

print('%x' % (data))
print('%X' % (data))

data=78
print(bin(data)[2:])
print(chr(data))

data=3.1483508
print('%f' % (data))

data=1000
print('%e' % (data))

data=0.001
print('%E' % (data))

data=100
print('%g' % (data))
data=100.00
print('%g' % (data))
data=100.001000
print('%g' % (data))
data=100000000
print('%g' % (data))

data=0.0001
print('%G' % (data))
data=0.0000001
print('%G' % (data))

print(complex(6))
print(complex(6, 8))

data={1,2,3,4,5,4,3,2}
print(data)

print(type(data))

x={1,2,3,4,5}
y={4,5,6,7,8}
print(x|y)
print(x&y)
print(x-y)
print(y-x)
