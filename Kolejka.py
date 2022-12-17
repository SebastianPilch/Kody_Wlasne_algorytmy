def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:

    def __init__(self, add_index=0, load_index=0, size=5):
        self.tab = [None for i in range(size)]
        self.add_index_ = add_index
        self.load_index_ = load_index

    def __str__(self):
        lst = []

        size = len(self.tab)
        index = self.load_index_
        while index != self.add_index_:
            lst.append(self.tab[index])
            if index < size - 1:
                index += 1
            else:
                index = 0
        return str(lst)

    def print_tab(self):
        return str(self.tab)

    def is_empty(self):
        if self.add_index_ == self.load_index_:
            return True
        else:
            return False

    def peek(self, index):
        if self.is_empty():
            return None
        else:
            return self.tab[self.load_index_ + index]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            load_data = self.tab[self.load_index_]
            if len(self.tab) == self.load_index_ + 1:
                self.load_index_ = 0
            else:
                self.load_index_ += 1

            return load_data

    def enqueue(self, data):
        self.tab[self.add_index_] = data
        if len(self.tab) == self.add_index_ + 1:
            self.add_index_ = 0
        else:
            self.add_index_ += 1
        size = len(self.tab)
        if self.add_index_ == self.load_index_:
            new_tab = [None for i in range(size * 2)]
            for j in range(size):
                if j >= self.load_index_:
                    new_tab[j + size] = self.tab[j]
                else:
                    new_tab[j] = self.tab[j]
            self.load_index_ += size
            self.tab = new_tab


Queue_test = Queue()
print(Queue_test)
print(Queue_test.is_empty())
for i in range(4):
    Queue_test.enqueue(i + 1)
print(Queue_test.dequeue())
print(Queue_test.tab, ' tab ')
print(Queue_test)
print(Queue_test.peek(1))

for i in range(4):
    Queue_test.enqueue(i + 5)
print(Queue_test)
for i in range(len(Queue_test.tab)):
    print(Queue_test.dequeue())
print(Queue_test.tab, ' tab ')
print(Queue_test, ' queue ')
print(Queue_test.is_empty(), '\n')
