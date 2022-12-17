#skończone
def string_ord(key: str):
    sum = 0
    for i in range(len(key)):
        sum += ord(key[i])
    return sum
class Element:
    def __init__(self, key=None, value=None):
        self.key_ = key
        self.value_ = value


class HashList:
    def __init__(self, size: int, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size_ = size
        self.c1_ = c1
        self.c2_ = c2

    def __str__(self):
        lst_keys = []
        lst_values = []
        for i in range(self.size_):
            if isinstance(self.tab[i], Element):
                elem: Element = self.tab[i]
                lst_keys.append(str(elem.key_))
                lst_values.append(str(elem.value_))
            else:
                lst_keys.append(None)
                lst_values.append(None)
        to_str = '{'
        for i in range(self.size_):
            if lst_keys[i] is not None:
                to_str += ' [' + str(lst_keys[i]) + ' : ' + str(lst_values[i]) + '] '
            else:
                to_str += ' ' + str(None) + ' '
        return to_str + '}'

    def hash_fct(self, key):
        if isinstance(key, str):
            return int(string_ord(key) % self.size_)
        else:
            return int(int(key) % self.size_)

    def collision(self, data, i):
        if isinstance(data, str):
            index = int(string_ord(data) + self.c1_ * i + self.c2_ * i ** 2) % self.size_
            if index == i:
                for j in range(self.size_):
                    if self.tab[index] is not None:
                        index = (index + 1) % self.size_
                    else:
                        break
                return index
            else:
                return index
        else:
            index = int(int(data) + self.c1_ * i + self.c2_ * i ** 2) % self.size_
            if index == i:
                for j in range(self.size_):
                    if self.tab[index] is not None:
                        index = (index + 1) % self.size_
                    else:
                        break
                return index
            else:
                return index

    def search(self, key):
        for i in range(self.size_):
            if isinstance(self.tab[i], Element):
                elem: Element = self.tab[i]
                if elem.key_ == key:
                    return elem.value_
            else:
                return None

    def insert(self, data: Element):
        for i in range(self.size_):
            if isinstance(self.tab[i], Element):
                elem: Element = self.tab[i]
                if elem.key_ == data.key_:
                    self.tab[i] = data
                    return
        index = self.hash_fct(data.key_)
        overflow = True
        for i in range(self.size_):
            if self.tab[index] is None:
                self.tab[index] = data
                overflow = False
                break
            else:
                index = self.collision(data.key_, index)
        if overflow:
            raise OverflowError

    def remove(self, key):
        remove_flag = True
        for i in range(self.size_):
            if isinstance(self.tab[i], Element):
                elem: Element = self.tab[i]
                if elem.key_ == key:
                    self.tab[i] = None
                    remove_flag = False
                    break
        if remove_flag:
            raise ValueError


hlst = HashList(13)

keys = [ 31 if i == 7 else 18 if i == 6 else i + 1 for i in range(15)]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
elems = [Element(keys[i], values[i]) for i in range(15)]
try:
    for i in range(15):
        hlst.insert(elems[i])
except:
    print('Brak miejsca')
print(hlst)
print(hlst.search(5))
print(hlst.search(14))
hlst.insert(Element(5, 'Nadpisana'))
print(hlst.search(5))
hlst.remove(5)
print(hlst)
print(hlst.search(31))
try:
    hlst.remove(5)
except:
    print('Brak danej')
hlst.insert(Element('W','test'))
print(hlst)

hlst2 = HashList(13)

keys = [i * 13 for i in range(15)]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
elems2 = [Element(keys[i], values[i]) for i in range(15)]
try:
    for i in range(15):
        hlst2.insert(elems2[i])
except:
    print('Brak miejsca')
print(hlst2)
hlst3 = HashList(13, 0, 1)
try:
    for i in range(15):
        hlst3.insert(elems2[i])
except:
    print('Brak miejsca')
print(hlst3)