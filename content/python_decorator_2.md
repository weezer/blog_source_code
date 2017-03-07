Title: Python Decorator in details
Date: 2017-03-03 15:42
Category: tech
Tags: tricks, python,
Slug: python-decorator-2
Authors: Weezer Su
Summary: ease to understand python decorator.
先来个返回值的例子
```python
def p1(name):
    print name

p3 = p1

p1("weezer p1")
p3("weezer p3")
print p3
p3 = p1("weezer")
print p3

#output
weezer p1
weezer p3
<function p1 at 0x10349a668>
weezer
None
```

先看一个函数的内部函 
其实就是把内部方法抛出
```python 
def p2(name):
    def p1(name):
        return "p1: " + name
    def p2argument(name):
        return "p2 inside: " + p1(name)
    return p2argument(name)


print p2("hello")
```
把他换个写法
```python
def p1(name):
    return "p1: " + name

def p2(func):
    def p2argument(name):
        return "p2 inside: " + func(name)
    return p2argument

print p2(p1)("weezer")
```

所以装饰器其实就是把内部函数抛出同时你使用内部函数更改了目标的返回值。
```python
def p1(name):
    return "p1" + name

def p2(func):
    def p2i(name):
        return "p2i" + func(name)
    return p2i

p3 = p2(p1)
print p3("123")
#output p2ip1123
```
#the below one is same as the above one.
```python
def p2(func):
    def p2i(name):
        return "p2i" + func(name)
    return p2i

@p2
def p1(name):
    return "p1" + name

print p1("123")
```
关于 ```from functools import wraps```
```python
def p1():
    pass

print p1.__name__
#p1
```
加入decorator
```python
def p2(func):
    return p2

@p2
def p1():
    pass

print p1().__name__
#p2
```
加入wraps
```python
from functools import wraps

def p2(func):
    @wraps(func)
    def p2i():
        pass
    return p2i

@p2
def p1():
    pass

print p1.__name__
#p1
```
