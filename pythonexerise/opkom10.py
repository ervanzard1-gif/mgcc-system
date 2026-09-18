#hasil adalah boolean
# <,>,<=,>=,==,!=,is,is not


a=4
b=2

hasil= a>3
print(a,">",3,"=", hasil)

hasil =b<2
print(b,"<",2,"=",hasil)

hasil =b<=2
print(b,"<=",2,"=hasil =b<=2",hasil)

hasil =a>=5
print(a,">=",5,"=",hasil)

hasil =b==2
print(b,"==",2,"=",hasil)

hasil =b!=2
print(b,"!=",2,"=",hasil)

hasil = a is b
print(a,"is",b,"=",hasil)


x=5
y=6
print('nilai x=',x,'id=',hex(id(x)))
print('nilai y=',y,'id=',hex(id(y)))

hasil = x is y
print(x,'is',y,'=',hasil)

hasil = x is not y
print(x,'is not',y,'=',hasil)

