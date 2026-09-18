#casting
data_int=-1
print("data : ",data_int)
print("bertype : ", type(data_int) )

data_float =float(data_int)
data_str =str(data_int)
data_bool =bool(data_int) #akan false jika 0
print("data : ",data_float)
print("data : ",data_str)
print("data : ",data_bool)
print("bertype : ", type(data_float) )
print("bertype : ", type(data_str) )
print("bertype : ", type(data_bool) )



data_float =float(data_int)
data_str =str(data_int)
data_bool =bool(data_int) #akan false jika 0
print("data : ",data_float,"bertype : ", type(data_float) )
print("data : ",data_str, "bertype : ", type(data_str) )
print("data : ",data_bool, "bertype : ", type(data_bool) )


print("=======float=======")
data_float=9.9
print("data : ",data_float)
print("bertype : ", type(data_float) )


data_int =int(data_float)
data_str =str(data_float)
data_bool =bool(data_float) #akan false jika 0
print("data : ",data_int,"bertype : ", type(data_int) )
print("data : ",data_str, "bertype : ", type(data_str) )
print("data : ",data_bool, "bertype : ", type(data_bool) )

print ("======boolean======")
data_bool= True
print("data : ",data_bool)
print("bertype : ", type(data_bool))

data_int =int(data_bool)
data_str =str(data_bool)
data_float =float(data_bool) #akan false jika 0
print("data : ",data_int,"bertype : ", type(data_int) )
print("data : ",data_str, "bertype : ", type(data_str) )
print("data : ",data_float, "bertype : ", type(data_float) )

print ("======string======")
data_str= "10" ;
print("data : ",data_str)
print("bertype : ", type(data_str))

data_int =int(data_str)# harus angka
data_bool =bool(data_str) # false jika string kosong
data_float =float(data_str) # harus angka
print("data : ",data_int,"bertype : ", type(data_int) )
print("data : ",data_bool, "bertype : ", type(data_bool) )
print("data : ",data_float, "bertype : ", type(data_float) )



data_int=2
print('data=',data_int)
print("bertipe", type(data_int))

#casting
data_float=float(data_int)
print('data= = ',data_float)
print('bertipe= ',type(data_float))


data_str=""
print('angka',data_str,'type=',type(data_str))

data_bool=bool(data_str)
print('hasil',data_bool,'type',type(data_bool))



data_int=0
print('data=',data_int, 'type',type(data_int))

data_bool=bool(data_int)
print('hasil=',data_bool,'type',type(data_bool))


data_float=0.1
print(data_float, type(data_float))
data_bool=bool(data_float)
print(data_bool)