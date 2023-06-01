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


def sort_swap(lst: list[Element]):
    for i in range(0,len(lst)-1):
        min = lst[i].priority_
        min_id = i
        for j in range(i + 1, len(lst)):
            if lst[j].priority_ < min:
                min = lst[j].priority_
                min_id = j

        lst[min_id], lst[i] = lst[i], lst[min_id]
    return lst


def sort_shift(lst: list[Element]):
    for i in range(0, len(lst)-1):
        min_id = i
        for j in range(i, len(lst)):
            if lst[j].priority_ < lst[min_id].priority_:
                min_id = j
        min_el = lst[min_id]
        lst.pop(min_id)
        lst.insert(i, min_el)


    return lst

tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
tab_to_sort = []
for i in tab:
    el = Element(i[0], i[1])
    tab_to_sort.append(el)

t_start = time.perf_counter()
print(sort_swap(tab_to_sort))
t_stop = time.perf_counter()
print("Czas sortowania przez zamianę:", "{:.7f}".format(t_stop - t_start))

tab_to_sort = []
for i in tab:
    el = Element(i[0], i[1])
    tab_to_sort.append(el)

t_start = time.perf_counter()
print(sort_shift(tab_to_sort))
t_stop = time.perf_counter()
print("Czas sortowania przez przesunięcie:", "{:.7f}".format(t_stop - t_start))

tab_to_sort = []
for i in range(10000):
    el = (int(random.random() * 1000))
    tab_to_sort.append(Element(el, el))

t_start = time.perf_counter()
tab_to_sort=sort_shift(tab_to_sort)
t_stop = time.perf_counter()
print(tab_to_sort)
print("Czas sortowania przez zamianę:", "{:.7f}".format(t_stop - t_start))


tab_to_sort = []
for i in range(10000):
    el = (int(random.random() * 1000))
    tab_to_sort.append(Element(el, el))
t_start = time.perf_counter()
tab_to_sort = sort_shift(tab_to_sort)
t_stop = time.perf_counter()
print(tab_to_sort)
print("Czas sortowania przez przesunięcie:", "{:.7f}".format(t_stop - t_start))
