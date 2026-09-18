#operasi tambah
a=10
b=3
hasil =a+b
print (a,'+',b,'=',hasil)

hasil =a-b
print(a,'-',b,'=',hasil)

hasil= a*b
print(a,'*',b,'=',hasil)

hasil =a/b
print(a,'/',b,'=',hasil) #jadi float enaknya

#eksponen pangkat

hasil =a**b
print(a,'**',b,'=',hasil)

hasil =a%b #modulus
print(a,'%',b,'=',hasil)

hasil=a//b #floor division
print(a,'//',b,'=',hasil)


#prioritas operation

x=3
y=4
z=5
hasil = x**y*(z+x)/y-y%z//x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil=(x+y)*z
print('(',x,'+',y,')*',z,'=',hasil)