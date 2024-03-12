class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next
    def set_prev(self, new_prev):
        self.prev = new_prev
    def set_data(self, new_data):
        self.data = new_data

class UOLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if (self.head is None) and (self.tail is None):
            return True
        else:
            return False

    def list_size(self):
        count = 0
        start = self.head
        while start is not None:
            count += 1
            start = start.get_next()
        return count

    def add_at_head(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.set_prev(node)
            node.set_next(self.head)
            self.head = node

    def add_at_tail(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node

    def print_with_index(self):
        start = self.head
        idx = 0
        string = ''
        string += f'{idx}: {start.data}'
        start = start.get_next()
        idx += 1
        while start is not None:
            string += ' <--> ' + f'{idx}: {start.data}'
            start = start.get_next()
            idx += 1
        print(string)

    def print(self):
        start = self.head
        string = ''
        string += f'{start.data}'
        start = start.get_next()
        idx = 0
        while start is not None:
            string += ' <--> ' + f'{start.data}'
            start = start.get_next()
            idx += 1
        string += f' --- final index is {idx}'
        print(string)

    def add_list_at_head(self, a_list: list, order = -1): # add in same order, meaning first in list will be head in linked list
        if order not in [0, -1]:
            print('set order to 0 for reverse, or -1 for same order as list.')
        while a_list:
            temp = a_list.pop(order)
            self.add_at_head(temp)

    def add_list_at_tail(self, a_list: list, order = 0): # add in same order, meaning last in list will be tail in linked list
        if order not in [0, -1]:
            print('set order to -1 for reverse, or 0 for same order as list.')
        while a_list:
            temp = a_list.pop(order)
            self.add_at_tail(temp)

    def insert(self, value, index): # insert at specific index, head is 0
        if not isinstance(index, int):
            print('index must be an int')
        elif self.is_empty():
            print('List is empty, use methods add_at_head or add_at_tail before using insert method.')
        elif index < 0:
            print(f'index must be positive, you entered {index}')
        elif index > self.list_size():
            print(f'enter a value in range, you entered {index} where values need to be between 0 and {self.list_size()}')
        elif index == 0:
            self.add_at_head(value)
        elif index == self.list_size():
            self.add_at_tail(value)
        else:
            start = 0
            current = self.head
            while start < index:
                current = current.get_next()
                start += 1
            temp = Node(value)
            prev = current.get_prev()
            temp.next = current
            temp.prev = prev
            prev.next = temp
            current.prev = temp

    def remove(self, value, n = 1): # remove nth instance of value given, default is first
        found = False
        current = self.head
        times = 0
        while current:
            if current.data == value:
                found = True
                times += 1
                if times == n and current == self.head:
                    next = current.get_next()
                    next.prev = None
                    self.head = next
                elif times == n and current == self.tail:
                    temp = current.get_prev()
                    temp.next = None
                elif times == n:
                    prev = current.get_prev()
                    next = current.get_next()
                    prev.next = next
                    next.prev = prev
                elif (current == self.tail) and (times < n):
                    print(f'cannot remove {value} after {n} iterations because {value} is not present {n} times. Will remove {value} at occurrence {times}, the last in list.')
                    self.remove(value, times)
            current = current.get_next()
        if found and (times < n):
            print(f'Cannot remove {value} after {n} iterations because {value} is not present {n} times. Will remove {value} at occurrence {times}, the last occurrence in list.')
            self.remove(value, times)
        if not found:
            print(f'{value} was not in list so nothing removed.')

    def search(self, value) -> bool: # returns True if value in ll
        contains = False
        current = self.head
        while current and not contains:
            if current.data == value:
                return True
            current = current.get_next()
        return contains

    def pop(self, n = -1): # removes item at nth instance.  Default is last item
        pass

    def index(self, value) -> int: # returns index of value
        contains = False
        current = self.head
        start = 0
        while current and not contains:
            if current.data == value:
                return start
            current = current.get_next()
            start += 1
        return None

ll = UOLL()
# ll.add_at_head()
ll.add_at_head(3)
ll.add_list_at_tail([1, 2, 3, 4])
ll.add_list_at_tail([4, 3]*4)
ll.insert(10, 3)
# print(ll.search(4))
# print(ll.index(5))
# ll.add_list_at_tail([10,20,30,40])
# ll.insert(2, 2)
print(ll.list_size())
ll.print()
ll.remove(1, 2)
ll.print()
