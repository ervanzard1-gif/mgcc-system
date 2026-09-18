#format string

data="ervanza"
data_str= 'nama saya ='+ data
print(data)

data="FTTM"
data_str=f"fakultas paling ketat = {data}"
print(data_str)

data= True
data_str='hasil'+ str(data)
print(data_str)

data= 'false'
data_str=f'hasil= {data}'
print(data_str)

data=207.3
data_str=f'nilai= {data}'
print(data_str)

data=19
data_str=f'nilai= {data:d}'
print(data_str)

data=20000000
data_str=f'nilai= {data:,}'
print(data_str)


data=2342.412425
data_str=f'nilai= {data:.2f}'
print(data_str)

data=2342.412425
data_str=f'nilai= {data:09.2f}'
print(data_str)

data=2342.412425
data_str=f'nilai= {data:8.2f}'
print(data_str)

angka_minus=-10
angka_plus=10
data_minus=f'nilai= {-angka_minus:d}'
data_plus=f'nilai= {+angka_plus:+d}'
print(data_minus)
print(data_plus)


data=0.067
data_persen=f'nilai= {data:.0%}'
print(data_persen)

data=0.067
data_persen=f'nilai= {data:.3%}'
print(data_persen)


x=2
y=6.3
hasil_str=f'hasil perkalian = {x*y:.1f}'
print(hasil_str)

z=132
databinary=f'binary= {bin(z)}'
dataoctal=f'octal= {oct(z)}'
datahex=f'hex= {hex(z)}'

print(databinary)
print(dataoctal)
print(datahex)

print(hex(id(z)))

#part2
nama="nadine kei inara"
nama2=f'nama= {nama}'
print(nama2)

angka=349.2
angka2=f'angka= {angka}'
print(angka2)

angka=27
angka2=f'angka= {angka:d}'
print(angka2)

hasil=True
hasil2=f'hasil= {hasil}'
print(hasil2)

angka=30000000000000
hasil2=f'harga=Rp.{angka:,}'
print(hasil2)

angka=896200.82974
hasil2=f'angka= {angka:.2f}'
print(hasil2)

angka=0.48792
hasil2=f'diskon= {angka:.1%}'
print(hasil2)

c=348
databinary=f'hasil= {bin(c)}'
dataoctal=f'hasil= {oct(c)}'
datahexid=f'hasil={hex(id(c))}'

print(databinary)
print(dataoctal)
print(datahexid)

data=20000000
print(f'data={data:,}')

data=5729.8257
print(f'data={data:014.2f}')

data=0.0067
print(f'data={data:.3%}')

data=-10
print(f'data={-data:-}')

data=10
print(f'data={data:+}')