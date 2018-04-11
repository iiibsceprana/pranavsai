satya@satya-pc:~$ python3
Python 3.5.2 (default, Jul  5 2016, 12:43:10) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> var1=1
>>> var2=10
>>> var1+var2
11
>>> del var1
>>> del var2
>>> cmpl=3+4j
>>> cmpl,id(cmpl),type(cmpl)
((3+4j), 139934244735344, <class 'complex'>)
>>> flt=45.567
>>> flt,id(flt),type(flt)
(45.567, 139934245585136, <class 'float'>)
>>> intg=55
>>> intg,id(intg),type(intg)
(55, 10913440, <class 'int'>)
>>> oct=OxAF
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'OxAF' is not defined
>>> oct=OxAF
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'OxAF' is not defined
>>> oct=oXAF
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'oXAF' is not defined
>>> oct=OxAF
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'OxAF' is not defined
>>> oct=0xAF
>>> oct=0o77
>>> oct,id(oct),type(oct)
(63, 10913696, <class 'int'>)
>>> hexa_decimal=0xAF
>>> hexa_decimal,id(hexa_decimal),type(hexa_decimal)
(175, 10917280, <class 'int'>)
>>> lng=5422222222222222222222222222222222222222222222222222
>>> lng,id(lng),type(lng)
(5422222222222222222222222222222222222222222222222222, 139934208108128, <class 'int'>)
>>> var=-5
>>> var
-5
>>> abs(var)
5
>>> var=-0
>>> math.ciel(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> import math
>>> math.ciel(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'ciel'
>>> math.ceil(var)
0
>>> math.floor(var)
0
>>> var=56.89
>>> math.ceil(var)
57
>>> math.floor(var)
56
>>> math.expl(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'expl'
>>> math.expl(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'expl'
>>> math.fabs(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> math.fabs(1)
1.0
>>> math.exp(1)
2.718281828459045
>>> math.log(10)
2.302585092994046
>>> math.log10(10)
1.0
>>> math.log(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> math.log(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> math.log10(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> var=1
>>> var=2
>>> var=3
>>> max(1,2,3)
3
>>> min(1,2,3)
1
>>> math.modf(2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: modf() takes exactly one argument (2 given)
>>> math.modf(3)
(0.0, 3.0)
>>> math.pow(2,64)
1.8446744073709552e+19
>>> var=456.768
>>> round(var)
457
>>> round(var,2)
456.77
>>> round(var,3)
456.768
>>> sqrt(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> math.sqrt(2)
1.4142135623730951
>>> math.sqrt(7)
2.6457513110645907
>>> var=100
>>> var=[1,22,24,43,5,6,7]
>>> import random 
>>> import seaborn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'seaborn'
>>> random.choice(var)
22
>>> random.choice(var)
5
>>> random.choice(var)
6
>>> random.choice(var)
24
>>> random.choice(var)
24
>>> random.choice(var)
5
>>> random.random()
0.9873561886215504
>>> random.randrange(0,10,2)
2
>>> random.randrange(0,10,2)
8
>>> random.randrange(0,10,2)
8
>>> random.randrange(0,10,2)
8
>>> random.seed(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/random.py", line 122, in seed
    super().seed(a)
TypeError: unhashable type: 'list'
>>> random.seed(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: seed() takes from 1 to 3 positional arguments but 4 were given
>>> c=random.seed(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/random.py", line 122, in seed
    super().seed(a)
TypeError: unhashable type: 'list'
>>> c=random.seed(1)
>>> c=random.seed(3)
>>> random.shuffle(var)
>>> var
[1, 24, 43, 7, 6, 5, 22]
>>> random.uniform(2,3)
2.625720304108054
>>> random.uniform(3,4)
3.065528859239813
>>> acosx(90)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'acosx' is not defined
>>> math.acos(0)
1.5707963267948966
>>> math.asin(0)
0.0
>>> math.atan(0)
0.0
>>> math.tan(45)
1.6197751905438615
>>> math.atan2(0,45)
0.0
>>> math.hypot(0,45)
45.0
>>> degrees(45)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'degrees' is not defined
>>> math.degrees(45)
2578.3100780887044
>>> math.radians(45)
0.7853981633974483
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045

