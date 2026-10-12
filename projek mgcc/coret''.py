#2048(sampe 16 aja dulu)
import random
a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'
j='j'
k='k'
l='l'
m='m'
n='n'
o='o'
p='p'

cell_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
first_index, second_index = random.sample(range(len(cell_names)), 2)
for idx in (first_index, second_index):
    globals()[cell_names[idx]] = '\x1b[32m2\x1b[0m'

board=f'''
 {a} | {b} | {c} | {d}
---------------
 {e} | {f} | {g} | {h}
---------------
 {i} | {j} | {k} | {l}
---------------
 {m} | {n} | {o} | {p}
'''
print(board)
