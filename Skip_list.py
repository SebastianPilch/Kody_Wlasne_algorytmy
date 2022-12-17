class Element:
    def __init__(self, key=None, value=None, levels=1):
        self.tab_ = [None for i in range(levels)]
        self.key_ = key
        self.value_ = value
        self.levels_ = len(self.tab_)

class SkipList:
    def __init__(self, max_level):
        self.head_ = Element(None, None, max_level)
        self.maxlevels_ = max_level

    def __str__(self):
        to_str = '{'
        for i in range(self.maxlevels_):
            to_str += 'level' + str(i) + '['
            next_elem: Element = self.head_.tab_[i]
            for j in range(next_elem.levels_):
                while next_elem.tab_[j] is not None:
                   to_str += ' ' + str(next_elem.value_) + ' '
                   next_elem = next_elem.tab_[j]
                else:
                    to_str += ']\n'
        return to_str + '}'

    def insert(self, new: Element):
        if self.head_.value_ is None:
            for i in range(self.maxlevels_):
                if new.levels_ < self.maxlevels_:
                    self.head_.tab_[i] = new
        else:
            level = new.levels_
            elem = self.head_.tab_
            prev = [None for i in range(level)]
            while level <= 0:
                prev_elem: Element = elem[level]
                while prev_elem is not None:
                    if prev_elem.key_ < new.key_:
                        new.tab_[level] = prev_elem.tab_[level]
                        prev[level] = new

                    else:
                        prev_elem = prev_elem.tab_[level]
                level -= 1


slst = SkipList(5)
slst.insert(Element(5, 5, 3))
print(slst)