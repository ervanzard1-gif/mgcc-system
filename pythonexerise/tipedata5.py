#angka satuan (data integer) yang gk ada komanya
data_integer=1
print (type(data_integer))
print ("data : ", data_integer, "bertipe : ", type(data_integer))


data_integer=3
print("data : ", data_integer)
print("bertipe : ", type(data_integer))

data_integer=5
print("data : ", data_integer)
print("-bertipe : ", type(data_integer))


#float (angka dengan koma)
data_float=1.5893944898274
print("data : ", data_float)
print("-bertipe : ", type(data_float))

#data string(kumpulan karakter)
dat_string= "halo 3"
print("data : ", dat_string)
print("-bertipe : ", type(dat_string))

#biner true/false (boolean), can use bool or boolean
data_boolean= True
print("data : ", data_boolean)
print("-bertipe : ", type(data_boolean))

"""how about ucup 10?, ini artinya tetap string"""


#bilangan kompleks j itu imajiner
data_complex = complex(5,8)
print("data : ", data_complex)
print("-bertipe : ", type(data_complex))

# bahasa c
from ctypes import c_double, c_char, c_byte,c_int,c_float #ini nanti aja kita bakal bahas
data_c_byte = c_byte(1284241)
print("data : ", data_c_byte)
print("-bertipe : ", type(data_c_byte))

