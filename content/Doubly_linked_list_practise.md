Title: Doubly-linked list 
Date: 2017-02-07 16:23
Category: leetcode
Tags: code, python, leetcode
Slug: Doubly_linked_list_practise 
Authors: Weezer Su
Summary: Just a ease doubly linked list


```python
class Node(object):
    def __init__(self, prev=None, next=None, value=None):
        self.prev = prev
        self.next = next
        self.value = value


class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node()
        self.end = Node()
        self.current = None

    def is_empty(self):
        if self.head.next is None:
            return True

    def append(self, input_value):
        new_node = Node(value=input_value)
        if self.is_empty():
            self.head.next =new_node
            new_node.prev = self.head
            new_node.next = self.end
            self.end.prev = new_node
        else:
            self.current = self.end.prev
            self.current.next = new_node
            new_node.prev = self.current
            new_node.next = self.end

    def remove(self, input_value):
        if self.is_empty():
            return False

        self.current = self.head.next

        while input_value != self.current.value and self.current.value is not None:
            self.current = self.current.next

        if self.current.value is None:
            return False

        self.current.next.prev = self.current.prev
        self.current.prev.next = self.current.next

    def show(self):
        self.current = self.head.next
        while self.current.value is not None:
            print str(self.current.value) + " "
            self.current = self.current.next


if __name__ == "__main__":
    dl_test = DoubleLinkedList()
    dl_test.append(1)
    dl_test.append(2)
    dl_test.remove(1)
    dl_test.show()
```

