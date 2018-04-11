>>> char='a'
>>> char,id(char),type(char)
('a', 139845835075288, <class 'str'>)
>>> str="hello"
>>> str,id(str),type(str)
('hello', 139845799097880, <class 'str'>)
>>> str[0]
'h'
>>> str[1]
'e'
>>> str[2]
'l'
>>> str[3]
'l'
>>> str[4]
'o'
>>> list(str)
['h', 'e', 'l', 'l', 'o']
>>> tuple(str)
('h', 'e', 'l', 'l', 'o')
>>> str
'hello'
>>> str+="sairam"
>>> str
'hellosairam'
>>> str="sai"
>>> str+="sairam"
>>> str+="pranav"
>>> str
'saisairampranav'
>>> del char
>>> del str
>>> print("hello\n sairam")
hello
 sairam
>>> print("hello\nsairam")
hello
sairam
>>> strg+="hello"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'strg' is not defined
>>> str+="hello"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
>>> str
<class 'str'>
>>> strg="hello"
>>> str+="sairam"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
>>> str+="pranav"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
>>> strg
'hello'
>>> str+ ="sairam"
  File "<stdin>", line 1
    str+ ="sairam"
         ^
SyntaxError: invalid syntax
>>> str+="sairam"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +=: 'type' and 'str'
>>> strg[:]
'hello'
>>> strg[1:]
'ello'
>>> strg[3:]
'lo'
>>> strg[5:]
''
>>> strg
'hello'
>>> strg+="sairam"
>>> strg
'hellosairam'
>>> strg[5:]
'sairam'
>>> strg[1:3]
'el'
>>> strg[1:10:2]
'elsia'
>>> strg[1:10:3]
'eoi'
>>> strg[1:10:4]
'esa'
>>> u'strg'
'strg'
>>> b'strg'
b'strg'
>>> strg
'hellosairam'
>>> strg.capitilize()\
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'capitilize'
>>> strg.capitilize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'capitilize'
>>> strg.capitalize()
'Hellosairam'
>>> strg.center(3,"*")
'hellosairam'
>>> strg.center(25,"*")
'*******hellosairam*******'
>>> strg.center(50,"*")
'*******************hellosairam********************'
>>> strg.count('a')
2
>>> strg.count('a',7,10)
1
>>> strg.count('a',6,10)
2
>>> strg.count('a',8,10)
1
>>> strg.count('a',4,10)
2
>>> strg.count('a',1,10)
2
>>> strg.count('a',1,len(strg))
2
>>> strg.count('a',6,len(strg))
2
>>> strg.count('a',8,len(strg))
1
>>> strg.encode(encoding='utf-8',errors="strict")
b'hellosairam'
>>> s=strg.ecode(encoding='utf-8',errors="strict")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'ecode'
>>> s=strg.encode(encoding='utf-8',errors="strict")
>>> s.decode()
'hellosairam'
>>> strg
'hellosairam'
>>> strg.endswith('*',0,len(strg))
False
>>> 
>>> strg.endswith('m',0,len(strg))
True
>>> strg.expandtabs(tabsize=20)
'hellosairam'
>>> strg.expandtabs(tabsize=20)+"hello"
'hellosairamhello'
>>> strg.find("hello",0,len(strg))
0
>>> strg.find("sairam",0,len(strg))
5
>>> strg.idex("sairam",0,len(strg))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'idex'
>>> strg.index("sairam",0,len(strg))
5
>>> strg.index("hello",0,len(strg))
0
>>> strg.isalnum()
True
>>> strg.isalpha()
True
>>> strg.isdigit()
False
>>> "9".isdigit()
True
>>> "9".islower()
False
>>> "9".isupper()
False
>>> strg.isnumeric()
False
>>> strg.istitle()
False
>>> len(strg)
11
>>> strg.join("my friend")\
... 
'mhellosairamyhellosairam hellosairamfhellosairamrhellosairamihellosairamehellosairamnhellosairamd'
>>> ljust(20,'*')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ljust' is not defined
>>> strg.ljust(20,'*')
'hellosairam*********'
>>> strg
'hellosairam'
>>> strg.lower
<built-in method lower of str object at 0x7f3063247830>
>>> strg.lower()
'hellosairam'
>>> strg.upper()
'HELLOSAIRAM'
>>> strg.lstrip()
'hellosairam'
>>> strg.rstrip()
'hellosairam'
>>> strg.strip()
'hellosairam'
>>> strg.maketrans('a','b')
{97: 98}
>>> max(strg)
's'
>>> min(strg)
'a'
>>> strg
'hellosairam'
>>> min("abc")
'a'
>>> strg.replace('s','S',len(strg))
'helloSairam'
>>> strg.replace('s','S')
'helloSairam'
>>> strg.split()
['hellosairam']
>>> strg.split('a',1)
['hellos', 'iram']
>>> strg.split('a',2)
['hellos', 'ir', 'm']
>>> strg.split('sairam',1)
['hello', '']
>>> strg.splitline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'splitline'
>>> strg.splitlines()
['hellosairam']
>>> "hello \n sairam".splitlines()
['hello ', ' sairam']
>>> strg.startswith("*",0,len(strg))
False
>>> strg.startswith("h",0,len(strg))
True
>>> strg.swapcase()
'HELLOSAIRAM'
>>> strg.title()
'Hellosairam'
>>> strg.translate('sai')
'hellosairam'
>>> strg.translate('sai',"ram")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: translate() takes exactly one argument (2 given)
>>> strg.translate("ram")
'hellosairam'
>>> strg.translate("*")
'hellosairam'
>>> strg.zfill()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: zfill() takes exactly 1 argument (0 given)
>>> strg.zfill(20)
'000000000hellosairam'
>>> strg.isdecimal()
False
>>> table=[1,2,3,4,5]
>>> strg.translate(table)
'hellosairam'
>>> table="abc"
>>> strg.translate(table)
'hellosairam'
>>> strg.translate(table,25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: translate() takes exactly one argument (2 given)
>>> strg.translate(table,22)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: translate() takes exactly one argument (2 given)
>>> dict=str.maketrans("abc","def")
>>> strg.translate(dict)
'hellosdirdm'
>>> 

