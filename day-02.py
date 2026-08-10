# Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
num = [45,45,78]
num
[45, 45, 78]
num
[45, 45, 78]
num[0]
45
num[0:2]
[45, 45]
num[4:0]
[]
num[1:2]
[45]
num[2:2]
[]
num[1:3]
[45, 78]
num[1:3]
[45, 78]
num[4]
#Traceback (most recent call last):
#  File "<pyshell#10>", line 1, in <module>
    num[4]
#IndexError: list index out of range
num[2.]
#Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
    num[2.]
#TypeError: list indices must be integers or slices, not float
num[2]
#78
num[-2]
#45
name = ['ravi','negi']
name
['ravi', 'negi']
name[0]
'ravi'
name[-1]
'negi'
alpha_numeric = [name, 45, 98, 45]
alpha_numeric
[['ravi', 'negi'], 45, 98, 45]
alpha_numeric[0]
['ravi', 'negi']
len(alpha_numeric)
4
name.count()
#Traceback (most recent call last):
#  File "<pyshell#22>", line 1, in <module>
    name.count()
#TypeError: list.count() takes exactly one argument (0 given)
num.count()
#Traceback (most recent call last):
#  File "<pyshell#23>", line 1, in <module>
    num.count()
#TypeError: list.count() takes exactly one argument (0 given)
num.count(14)
#0
num.count(98)
#0
num.count(45)
#2
num.insert(99)
#Traceback (most recent call last):
#  File "<pyshell#27>", line 1, in <module>
    num.insert(99)
#TypeError: insert expected 2 arguments, got 1
num.insert(2,99)
num
#[45, 45, 99, 78]
#[45, 45, 99, 78]
#[45, 45, 99, 78]
tup = 45, 78, 78 ,78
tup
#(45, 78, 78, 78)
type(tup)
#<class 'tuple'>
#<class 'tuple'>
#SyntaxError: invalid syntax
tup2 = (45,45,787,74,4)
tup2
(45, 45, 787, 74, 4)
max(tup2)
787
tup.index()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    tup.index()
TypeError: index expected at least 1 argument, got 0
>>> tup(74).index()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    tup(74).index()
TypeError: 'tuple' object is not callable
>>> tup[4]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    tup[4]
IndexError: tuple index out of range
>>> tup2.count(74)
1
>>> tup2.index(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tup2.index(1)
ValueError: tuple.index(x): x not in tuple
>>> tup2.index(74)
3
>>> tup2.index(74)
3
>>> tup = 45, 'ravi'
>>> tup
(45, 'ravi')
>>> '45' in tup
False
>>> 45 in tup
True
