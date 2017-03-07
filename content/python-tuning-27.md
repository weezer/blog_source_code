Title: Python Tuning 
Date: 2017-03-04 12:17
Category:tech 
Tags: tricks, python
Slug:python-tuning-27.md 
Authors: Weezer Su
Summary: Python Tuning 

1.使用 Map ，Reduce 和 Filter 代替 for 循环

2.校验 a in b， 字典 或 set 比 列表 或 元组 更好

3.当数据量大的时候，尽可能使用不可变数据类型，他们更快 元组 > 列表

4.在一个列表中插入数据的复杂度为 O(n)

5.如果你需要操作列表的两端，使用 deque

6.list和set查找某一个元素的时间复杂度分别是O(n)和O(1)。

7.使用dict或set查找元素
python dict和set都是使用hash表来实现(类似c++11标准库中unordered_map)，查找元素的时间复杂度是O(1)
```python
import copy
a = range(100000)
%timeit -n 10 copy.copy(a) # 运行10次 copy.copy(a)
%timeit -n 10 copy.deepcopy(a)
10 loops, best of 3: 1.55 ms per loop
10 loops, best of 3: 151 ms per loop
```
8.合理使用copy与deepcopy
```python
import copy
a = range(100000)
%timeit -n 10 copy.copy(a) # 运行10次 copy.copy(a)
%timeit -n 10 copy.deepcopy(a)
10 loops, best of 3: 1.55 ms per loop
10 loops, best of 3: 151 ms per loop
```

9.合理使用生成器（generator）和yield.
```python
%timeit -n 100 a = (i for i in range(100000))
%timeit -n 100 b = [i for i in range(100000)]
100 loops, best of 3: 1.54 ms per loop
100 loops, best of 3: 4.56 ms per loop
```
使用()得到的是一个generator对象，所需要的内存空间与列表的大小无关，所以效率会高一些。在具体应用上，比如set(i for i in range(100000))会比set([i for i in range(100000)])快。
但是对于需要循环遍历的情况：
```python
%timeit -n 10 for x in (i for i in range(100000)): pass
%timeit -n 10 for x in [i for i in range(100000)]: pass
10 loops, best of 3: 6.51 ms per loop
10 loops, best of 3: 5.54 ms per loop
```
后者的效率反而更高，但是如果循环里有break,用generator的好处是显而易见的。yield也是用于创建generator：
```python
def yield_func(ls):
    for i in ls:
        yield i+1

def not_yield_func(ls):
    return [i+1 for i in ls]

ls = range(1000000)
%timeit -n 10 for i in yield_func(ls):pass
%timeit -n 10 for i in not_yield_func(ls):pass
10 loops, best of 3: 63.8 ms per loop
10 loops, best of 3: 62.9 ms per loop
```
10.优化循环
循环之外能做的事不要放在循环内，比如下面的优化可以快一倍
```python
a = range(10000)
size_a = len(a)
%timeit -n 1000 for i in a: k = len(a)
%timeit -n 1000 for i in a: k = size_a
1000 loops, best of 3: 569 µs per loop
1000 loops, best of 3: 256 µs per loop
```
11.优化包含多个判断表达式的顺序
对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面。如：
```python
a = range(2000)  
%timeit -n 100 [i for i in a if 10 < i < 20 or 1000 < i < 2000]
%timeit -n 100 [i for i in a if 1000 < i < 2000 or 100 < i < 20]     
%timeit -n 100 [i for i in a if i % 2 == 0 and i > 1900]
%timeit -n 100 [i for i in a if i > 1900 and i % 2 == 0]
100 loops, best of 3: 287 µs per loop
100 loops, best of 3: 214 µs per loop
100 loops, best of 3: 128 µs per loop
100 loops, best of 3: 56.1 µs per loop
```
12.使用join合并迭代器中的字符串
join对于累加的方式，有大约5倍的提升。

13.不借助中间变量交换两个变量的值
```python
a,b=1,2
a,b=b,a
```
14.使用 if is True 比 if == True 将近快一倍。
15.使用级联比较x < y < z
16.while 1 比 while True 更快, 因为True是一个变量，而不是关键字
17. 使用**而不是pow  
18. 使用 cProfile, cStringIO 和 cPickle等用c实现相同功能（分别对应profile, StringIO, pickle）的包
```python
import cPickle
import pickle
a = range(10000)
%timeit -n 100 x = cPickle.dumps(a)
%timeit -n 100 x = pickle.dumps(a)
100 loops, best of 3: 1.58 ms per loop
100 loops, best of 3: 17 ms per loop
```
19.使用最佳的反序列化方式
```python
import json
import cPickle
a = range(10000)
s1 = str(a)
s2 = cPickle.dumps(a)
s3 = json.dumps(a)
%timeit -n 100 x = eval(s1)
%timeit -n 100 x = cPickle.loads(s2)
%timeit -n 100 x = json.loads(s3)
100 loops, best of 3: 16.8 ms per loop
100 loops, best of 3: 2.02 ms per loop
100 loops, best of 3: 798 µs per loop
```
20.用位运算判断奇偶性
```python
def is_even(x):
    return False if x & 1 else True
```
21.尽量使用局部变量
Python 检索局部变量比检索全局变量快. 这意味着,避免 “global” 关键字.

22.尽量使用 “in”
使用 “in” 关键字. 简洁而快速.

23.使用延迟加载加速
將 import 声明移入函数中,仅在需要的时候导入. 换句话说，如果某些模块不需马上使用,稍后导入他们. 例如，你不必在一开使就导入大量模块而加速程序启动. 该技术不能提高整体性能. 但它可以帮助你更均衡的分配模块的加载时间.

24.使用 xrange() 处理长序列：
这样可为你节省大量的系统内存，因为 xrange() 在序列中每次调用只产生一个整数元素。而相反 range()，它將直接给你一个完整的元素列表，用于循环时会有不必要的开销。 在 Python3 中 xrange 被去掉，而 range 则相当于 python2 的 xrange。

25.了解 itertools 模块：
模块 itertools 对迭代和组合是非常有效的。

26.学习 bisect 模块保持列表排序：
这是一个二分查找实现和快速插入有序序列的工具。该模块能将一个元素插入列表中, 而你不需要再次调用 sort() 来保持容器的排序, 因为在长序列中这会非常昂贵.

27.理解 Python 列表，实际上是一个数组：
Python 中的列表实现并不是以人们通常谈论的计算机科学中的普通单链表实现的。Python 中的列表是一个数组。也就是说，你可以以常量时间 O(1) 检索列表的某个元素，而不需要从头开始搜索。这有什么意义呢？ Python开发人员使用列表对象 insert() 时, 需三思. 例如：list.insert（0，item）

28.在列表的前面插入一个元素效率不高, 因为列表中的所有后续下标不得不改变. 然而，您可以使用list.append()在列表的尾端有效添加元素。 如果你想快速的在两插入或时，可以使用 deque。它是快速的，因为在 Python 中的 deque 用双链表实现。

29.Python 装饰器缓存结果：
@ 符号是 Python 的装饰语法。它不只用于追查，锁或日志。你可以装饰一个 Python 函数，记住调用结果供后续使用。这种技术被称为 memoization 的。例如 functools.lru_cache 就是一个用于缓存数据的装饰器，他会将传入函数的不同的参数产生的结果进行保存，也就是对每一个输入进行缓存，下次调用则直接返回缓存结果。

30.使用 multiprocessing 模块实现真正的并发
因为 GIL 会序列化线程, Python 中的多线程不能在多核机器和集群中加速. 因此 Python 提供了 multiprocessing 模块, 可以派生额外的进程代替线程, 跳出 GIL 的限制. 此外, 你也可以在外部 C 代码中结合该建议, 使得程序更快.

注意, 进程的开销通常比线程昂贵, 因为线程自动共享内存地址空间和文件描述符. 意味着, 创建进程比创建线程会花费更多, 也可能花费更多内存. 这点在计划使用多处理器时要牢记.

31.使用第三方包
有很多为 Python 设计的高性能的第三方库和工具. 下面是一些有用的加速包的简短列表.

 - NumPy: 一个开源的相当于 MatLab 的包
 - SciPy: 另一个数值处理库
 - GPULib: 使用 GPUs 加速代码
 - PyPy: 使用 just-in-time 编译器优化 Python 代码
 - Cython: 將 Python 优码转成 C
 - ShedSkin: 將 Python 代码转成 C++   

