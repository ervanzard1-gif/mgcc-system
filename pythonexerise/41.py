teman2={
    'A': 'Andi',
    'B': 'Budi',
    'C': 'Cici',
    'D': 'Dodi',
    'E': 'Euis',
    'F': 'Fajar',
}

friend=teman2
print(f'teman2={teman2}\n')
print(f'friend={friend}')

teman2['A']='Andika'
print(f'\nteman2={teman2}\n')
print(f'\nfriend={friend}\n')

print('\n\n\n\n\n\n\n\n\n')


friend=teman2.copy()
print(f'teman2={teman2}\n')
print(f'friend={friend}')

teman2['A']='Akmal'
print(f'\nteman2={teman2}\n')
print(f'\nfriend={friend}\n')



data=teman2.pop('A')
print(f'teman={data}')
print(f'teman2={teman2}')

data=teman2.popitem()
print(f'teman={data}')
print(f'teman2={teman2}')


#Penggunaan `dict[key]` akan memicu **`KeyError`** dan menghentikan program jika kunci tidak ditemukan. Sebaliknya, metode **`get()`** lebih aman karena tidak menyebabkan *error*, melainkan mengembalikan nilai **`None`** (atau nilai *default* pilihanmu) saat kuncinya tidak ada.

