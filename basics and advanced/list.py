>>> my_list=[]
>>> my_list
[]
>>> my_list,id(my_list),type(my_list)
([], 140283518144904, <class 'list'>)
>>> my_list=[1,2,3,[1,2,3],(1,2,3),[1:'one', 2:'two', 3:'three'}]
  File "<stdin>", line 1
    my_list=[1,2,3,[1,2,3],(1,2,3),[1:'one', 2:'two', 3:'three'}]
                                     ^
SyntaxError: invalid syntax
>>> my_list=[1,2,3,[1,2,3],(1,2,3),[1: 'one', 2:'two', 3:'three'}]
  File "<stdin>", line 1
    my_list=[1,2,3,[1,2,3],(1,2,3),[1: 'one', 2:'two', 3:'three'}]
                                     ^
SyntaxError: invalid syntax
>>> my_list=[1,2,3,[1,2,3],(1,2,3),{1:'one', 2:'two', 3:'three'}]
>>> my_list
[1, 2, 3, [1, 2, 3], (1, 2, 3), {1: 'one', 2: 'two', 3: 'three'}]
>>> my_list[4]
(1, 2, 3)
>>> my_list[8]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> my_list[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> my_list[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> my_list[5]
{1: 'one', 2: 'two', 3: 'three'}
>>> my_list[4]
(1, 2, 3)
>>> my_list[4][3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> my_list[4][2]
3
>>> my_list[4][1]
2
>>> my_list[4][0]
1
>>> my_list[4][-1]
3
>>> my_list[4][-3]
1
>>> my_list[-1]
{1: 'one', 2: 'two', 3: 'three'}
>>> my_list[-1][2]
'two'
>>> my_list[-1][-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: -1
>>> my_list[-1][3]
'three'
>>> my_list[::1]
[1, 2, 3, [1, 2, 3], (1, 2, 3), {1: 'one', 2: 'two', 3: 'three'}]
>>> my_list[::-1]
[{1: 'one', 2: 'two', 3: 'three'}, (1, 2, 3), [1, 2, 3], 3, 2, 1]
>>> my_list[::-1][1]
(1, 2, 3)
>>> my_list[::-1][-1]
1
>>> my_list[::-1][-2]
2
>>> my_list[::-1][-4]
[1, 2, 3]
>>> my_list[::-1][-5]
(1, 2, 3)
>>> 1 in my_list
True
>>> 1 not in my_list
False
>>> max(my_list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: list() > int()
>>> max(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> l=[1,2,3,4,5,6,7]
>>> max(l)
7
>>> min(l)
1
>>> del my_list[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> del my_list[5]
>>> my_list
[1, 2, 3, [1, 2, 3], (1, 2, 3)]
>>> my_list[4]
(1, 2, 3)
>>> del my_list[4]
>>> my_list
[1, 2, 3, [1, 2, 3]]
>>> my_list.count(1)
1
>>> my_list.count(3)
1
>>> my_list.count(4)
0
>>> my_list.count(5)
0
>>> my_list.insert(3,1)
>>> my_list
[1, 2, 3, 1, [1, 2, 3]]
>>> my_list.insert(4,1)
>>> my_list
[1, 2, 3, 1, 1, [1, 2, 3]]
>>> my_list.insert(4,4)
>>> my_list
[1, 2, 3, 1, 4, 1, [1, 2, 3]]
>>> my_list.insert(4,9)
>>> my_list
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3]]
>>> l
[1, 2, 3, 4, 5, 6, 7]
>>> my_list.extend[l]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> my_list.extend(l)
>>> my_list
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list.count(1)
4
>>> my_list.count(6)
1
>>> my_list.count(9)
1
>>> l.sort
<built-in method sort of list object at 0x7f964b11dac8>
>>> l.sort()
>>> l.append(6)
>>> l.append(7)
>>> l.append(9)
>>> l
[1, 2, 3, 4, 5, 6, 7, 6, 7, 9]
>>> my_list[0:]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[::]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[:6]
[1, 2, 3, 1, 9, 4]
>>> my_list[7:]
[[1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[:]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[14:]
[7]
>>> my_list[154:]
[]
>>> my_list[0:5]
[1, 2, 3, 1, 9]
>>> my_list[0:8]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3]]
>>> my_list[0:13]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5]
>>> my_list[4:10]
[9, 4, 1, [1, 2, 3], 1, 2]
>>> my_list[-1]
7
>>> my_list[::-1]
[7, 6, 5, 4, 3, 2, 1, [1, 2, 3], 1, 4, 9, 1, 3, 2, 1]
>>> my_list[::1]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[:9:1]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1]
>>> my_list[:9]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1]
>>> my_list[:1]
[1]
>>> my_list[:-13]
[1, 2]
>>> my_list
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[-13]
3
>>> my_list[13]
6
>>> my_list[:13]
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5]
>>> my_list[:10:-1]
[7, 6, 5, 4]
>>> my_list
[1, 2, 3, 1, 9, 4, 1, [1, 2, 3], 1, 2, 3, 4, 5, 6, 7]
>>> my_list[:9:-1]
[7, 6, 5, 4, 3]
>>> my_list[:6:-1]
[7, 6, 5, 4, 3, 2, 1, [1, 2, 3]]
>>> my_list.reverse()
>>> my_list
[7, 6, 5, 4, 3, 2, 1, [1, 2, 3], 1, 4, 9, 1, 3, 2, 1]
>>> my_list.pop()
1
>>> my_list.pop()
2
>>> my_list.pop()
3
>>> my_list.pop()
1
>>> my_list
[7, 6, 5, 4, 3, 2, 1, [1, 2, 3], 1, 4, 9]
>>> my_list.reverse()
>>> my_list.reverse()
>>> my_list
[7, 6, 5, 4, 3, 2, 1, [1, 2, 3], 1, 4, 9]
>>> 
>>> my_list.pop()
9
>>> my_list.insert(0,1)
>>> my_list
[1, 7, 6, 5, 4, 3, 2, 1, [1, 2, 3], 1, 4]
>>> my_list([1,2,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> my_list[1,2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> a=my_list([1,2,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> list[1,2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> list([1,2,3])
[1, 2, 3]
>>> a=list([1,2,3])
>>> b=list([1,2,3])
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]

