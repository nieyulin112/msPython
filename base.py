# 数组的方法
arr = [1, 2, 3]
print('length', len(arr))
t = (1, 2, 4, 5)
print('length', len(t), t[0:3], arr[1:3])
# list 和 tuple, 可以进行切片操作, list可以进行修改, tuple是不可以修改
arr.append(4)
# 复制一个数组或者元组
print('arr', arr, t, t[:], arr[:])
# 迭代循环
for val in 'variable':
    print('val', val)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)

for k, v in d.items():
    print(k, ':', v)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance('123', Iterable))
# 获取数组的下标
for i, vs in enumerate(['A', 'B', 'C']):
    print(i, ':', vs)

# 列表生成器
s = list(range(1, 10))
print('s:', s)

l = []
for x in range(1, 5):
    l.append(x * x)
print('l:', l)


# tuple
g = (x * x for x in range(10))
for n in g:
    print('n:', n)
