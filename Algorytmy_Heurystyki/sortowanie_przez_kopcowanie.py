import random
import time

class Element:

    def __init__(self, priority, data):
        self.priority_ = priority
        self.value_ = data

    def __gt__(self, other):
        if self.priority_ > other.priority_:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.priority_ < other.priority_:
            return True
        else:
            return False

    def __str__(self):
        return str(self.priority_) + ':' + str(self.value_)

    def __repr__(self):
        return str(self.priority_) + ':' + str(self.value_)


class Heap:
    def __init__(self, Tab_to_sort: list[Element] = None):
        if Tab_to_sort is not None:
            self.queue_ = Tab_to_sort
            self.size_ = len(Tab_to_sort)
            last_parent = self.size_//2 - 1
            for i in range(self.size_//2):
                self.heapify(last_parent-i)
        else:
            self.queue_ = []
            self.size_ = 0

    def left(self, index):
        new_index = 2 * index + 1
        if new_index > self.size_ - 1:
            return None
        else:
            return new_index

    def right(self, index):
        new_index = 2 * index + 2
        if new_index > self.size_ - 1:
            return None
        else:
            return new_index

    def parent(self, index):
        new_index = int((index - 1) / 2) if index % 2 == 1 else int((index - 2) / 2)
        if new_index < 0:
            return 0
        else:
            return new_index

    def is_empty(self):
        return True if self.size_ == 0 else False

    def peek(self):
        return self.queue_[0].value_

    def enqueue(self, data: Element):
        self.queue_.append(data)
        self.size_ += 1
        parent_index = self.parent(self.size_ - 1)
        parent: Element = self.queue_[parent_index]
        new_index = self.size_ - 1
        new: Element = self.queue_[new_index]
        while new_index != 0 and parent.priority_ < new.priority_:
            self.queue_[parent_index], self.queue_[new_index] = self.queue_[new_index], self.queue_[parent_index]
            new = self.queue_[parent_index]
            new_index = parent_index
            parent_index = self.parent(new_index)
            parent = self.queue_[parent_index]

    def dequeue(self):
        removed_index = 0
        if self.is_empty():
            print('brak indeksu o podanym priorytecie')
            return None
        removed_elem: Element = self.queue_[removed_index]
        data_to_return = removed_elem
        self.queue_[self.size_ - 1], self.queue_[removed_index] = self.queue_[removed_index], self.queue_[
            self.size_ - 1]
        self.size_ -= 1
        if self.is_empty():
            return data_to_return
        self.heapify()
        return data_to_return

    def heapify(self, removed_index=0):
        new_elem: Element = self.queue_[removed_index]
        child = None
        child_index = None

        left_index = self.left(removed_index)
        right_index = self.right(removed_index)
        if left_index is not None:
            left_elem: Element = self.queue_[left_index]
        else:
            left_elem = None
        if right_index is not None:
            right_elem: Element = self.queue_[right_index]
        else:
            right_elem = None

        if left_elem is None:
            if right_elem is None:
                return
            if right_elem.priority_ > new_elem.priority_:
                child = right_elem
                child_index = right_index
            else:
                return
        if right_elem is None:
            if left_elem.priority_ > new_elem.priority_:
                child = left_elem
                child_index = left_index
            else:
                return
        if (left_elem.priority_ < new_elem.priority_) and (right_elem.priority_ < new_elem.priority_):
            return
        if left_elem is not None and right_elem is not None:
            if left_elem.priority_ > right_elem.priority_:
                child = left_elem
                child_index = left_index
            else:
                child = right_elem
                child_index = right_index

        while child.priority_ > new_elem.priority_:

            self.queue_[removed_index], self.queue_[child_index] = self.queue_[child_index], self.queue_[removed_index]
            removed_index = child_index
            new_elem: Element = self.queue_[child_index]
            left_index = self.left(child_index)
            right_index = self.right(child_index)

            if left_index is not None:
                left_elem: Element = self.queue_[left_index]
            else:
                left_elem = None
            if right_index is not None:
                right_elem: Element = self.queue_[right_index]
            else:
                right_elem = None

            if left_elem is None:
                if right_elem is None:
                    return
                if right_elem.priority_ > new_elem.priority_:
                    child = right_elem
                    child_index = right_index
                else:
                    return
            if right_elem is None:
                if left_elem.priority_ > new_elem.priority_:
                    child = left_elem
                    child_index = left_index
                else:
                    return
            if (left_elem.priority_ < new_elem.priority_) and (right_elem.priority_ < new_elem.priority_):
                return
            if (left_elem is not None) and (right_elem is not None):
                if left_elem.priority_ > right_elem.priority_:
                    child = left_elem
                    child_index = left_index
                else:
                    child = right_elem
                    child_index = right_index

    def print_tab(self):
        if self.is_empty():
            print('{}')
        else:
            print('{', end=' ')
            for i in range(self.size_ - 1):
                print(self.queue_[i], end=', ')
            if self.queue_[self.size_ - 1]: print(self.queue_[self.size_ - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx is not None and idx < self.size_:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.queue_[idx] if self.queue_[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

tab =[(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
elements = [Element(tab[i][0],tab[i][1]) for i in range(len(tab))]

heap2 = Heap(elements)
heap2.print_tree(0, 0)
for i in range(heap2.size_):
    heap2.dequeue()
heap2.size_ = len(elements)
heap2.print_tab()

ran_tab = []
for i in range(10000):
     r = (int(random.random() * 100))
     ran_tab.append(Element(r,r))

t_start = time.perf_counter()
heap3 = Heap(ran_tab)
for i in range(heap3.size_):
    heap3.dequeue()
heap3.size_ = 10000
heap3.print_tab()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# sortowanie jest stabilne w tablicy z danymi w formie liter przy tym samym priotytecie kolejność jest zawsze ta sama