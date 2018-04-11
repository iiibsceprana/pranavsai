satya@satya-pc:~$ python3
Python 3.5.2 (default, Jul  5 2016, 12:43:10) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a=()
>>> b=0,
>>> a,id(a),type(a)
((), 140356632469576, <class 'tuple'>)
>>> b,id(b),type(b)
((0,), 140356631406296, <class 'tuple'>)
>>> b=1,
>>> b,id(b),type(b)
((1,), 140356631406352, <class 'tuple'>)
>>> c=1,2,3
>>> c,id(c),type(c)
((1, 2, 3), 140356631649736, <class 'tuple'>)
>>> c.insert(2,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'insert'
>>> c.remove(2,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'
>>> c.append(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> max(C)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'C' is not defined
>>> c
(1, 2, 3)
>>> max(C)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'C' is not defined
>>> max(C)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'C' is not defined
>>> max(c)
3
>>> min(c)
1
>>> c.count(1)
1
>>> len(c)
3
>>> del c(2)
  File "<stdin>", line 1
SyntaxError: can't delete function call
>>> del c(2,)
  File "<stdin>", line 1
SyntaxError: can't delete function call
>>> del c
>>> c=1,2,3
>>> c*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> c*5
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> a=b+c
>>> a
(1, 1, 2, 3)
>>> a[0]
1
>>> a[2]
2
>>> a[3
... 
... ]
3
>>> a[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> a[-3]
1
>>> a[-4]
1
>>> a[-5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> a[::-1]
(3, 2, 1, 1)
>>> a
(1, 1, 2, 3)
>>> 4 in a
False
>>> 3 in a
True
>>> 1 in a
True
>>> a[:]
(1, 1, 2, 3)
>>> a[:-1]
(1, 1, 2)
>>> a.reverse[:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'reverse'
>>> 
>>> a=1.2,3
>>> a=1,2,3
>>> a[::-1]
(3, 2, 1)
>>> a[::-2]
(3, 1)
>>> a[::-1]
(3, 2, 1)
>>> a[::-3]
(3,)
>>> 3 in a
True
>>> 5 in a
False
>>> a[1:]
(2, 3)
>>> a[-1:
... ]
(3,)
>>> a[2:]
(3,)
>>> a[-2:]
(2, 3)
>>> a[0:]
(1, 2, 3)
>>> a[0:-1]
(1, 2)
>>> a[0:1]
(1,)
>>> a[0:3]
(1, 2, 3)
>>> a[0:4]
(1, 2, 3)
>>> a[0:5]
(1, 2, 3)
>>> a[5:1]
()
>>> a[4:1]
()
>>> a[::-1]
(3, 2, 1)
>>> d=a[::-1]
>>> d
(3, 2, 1)
>>> a
(1, 2, 3)
>>> str="sairam"
>>> tuple(str)
('s', 'a', 'i', 'r', 'a', 'm')
>>> 

