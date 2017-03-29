Title: Elevator Maintenance
Date: 2017-03-28 21:24:42
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-Elevator-Maintenance
Authors: Weezer Su
Summary: Elevator Maintenance
Compare 2 strings```"abc" < "abd"```

```python
def version_sort(list):
    version_list = []
    for i in list:
        version_list.append(i.split("."))
    for i in range(1, len(version_list)):
        for j in range(i):
            if elem_compare(version_list[i], version_list[j]):
                version_list[i], version_list[j] = version_list[j], version_list[i]
    result = []
    for i in version_list:
        result.append(".".join(i))
    return result


def elem_compare(a, b):
    for i in range(min(len(a), len(b))):
        if int(a[i]) < int(b[i]):
            return True
        if int(a[i]) > int(b[i]):
            return False
    return (True, False)[len(a) > len(b)]


print version_sort( ["1.11", "1.2"])

```

```
