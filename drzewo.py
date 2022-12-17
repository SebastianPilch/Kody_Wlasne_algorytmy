class Element:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.left_ = left
        self.right_ = right
        self.key_ = key
        self.value_ = value


class Tree:
    def __init__(self, root: Element = None):
        self.root_ = root

    def insert(self, new: Element):
        if self.root_ is None:
            self.root_ = new
        else:
            next = self.root_
            while next is not None:
                if new.key_ == next.key_:
                    next.value_ = new.value_
                    break
                else:
                    if new.key_ > next.key_:
                        if next.right_ is not None:
                            next = next.right_
                        else:
                            next.right_ = new
                    else:
                        if next.left_ is not None:
                            next = next.left_
                        else:
                            next.left_ = new

    def search(self, key, curr_node):

        if curr_node is None:
            return None
        else:
            if curr_node.key_ < key:
                return self.search(key, curr_node.right_)
            elif curr_node.key_ > key:
                return self.search(key, curr_node.left_)
            else:
                return curr_node.value_
        # def search(self, data):
        #     if self.root_ is None:
        #         return None
        #     key = self.root_.key_
        #     if key == data:
        #         return key
        #     visited = [key]
        #     next = []
        #     if self.root_.left_ is not None:
        #         next.append(self.root_.left_)
        #     if self.root_.right_ is not None:
        #         next.append(self.root_.right_)
        #     if len(next) < 0:
        #         return None
        #     for Elem in next:
        #         if Elem.key_ not in visited:
        #             if Elem.key_ == data:
        #                 return Elem.value_
        #             else:
        #                 if Elem.left_ is not None:
        #                     next.append(Elem.left_)
        #                 if Elem.right_ is not None:
        #                     next.append(Elem.right_)
        #                 visited.append(Elem.key_)

    def delete(self, data):

        if self.search(data, self.root_) is None:
            print("nie ma zmiennej o takim kluczu")
            return 0

        else:
            elem = self.root_
            prev = self.root_
            side = 0

            while 1:
                if elem.key_ > data:
                    if elem.left_.key_ == data:
                        prev = elem
                        elem = elem.left_
                        side = 1
                        break
                    else:
                        elem = elem.left_

                if elem.key_ < data:
                    if elem.right_.key_ == data:
                        prev = elem
                        elem = elem.right_
                        side = 2
                        break
                    else:
                        elem = elem.right_

                if elem.key_ == data:
                    break

            if elem.left_ is None and elem.right_ is None:
                if prev.left_ is not None:
                    if prev.left_.key_ == data:
                        prev.left_ = None

                if prev.right_ is not None:
                    if prev.right_.key_ == data:
                        prev.right_ = None
                return

            if elem.left_ is None and elem.right_ is not None:
                if side == 2:  # jesli ansz usuwany jest z prawej
                    prev.right_ = elem.right_
                elif side == 1:
                    prev.left_ = elem.right_
                return

            if elem.left_ is not None and elem.right_ is None:

                if side == 2:
                    prev.right_ = elem.left_
                elif side == 1:
                    prev.left_ = elem.left_

            if elem.left_ is not None and elem.right_ is not None:

                if elem.right_.left_ is None:
                    elem.key_ = elem.right_.key_
                    elem.value_ = elem.right_.value_
                    elem.right_ = elem.right_.right_

                elif elem.right_.left_ is not None:

                    pom_node = elem.right_.left_
                    pom_prev_node = elem.right_

                    while pom_node.left_ is not None:
                        pom_node = pom_node.left_
                        pom_prev_node = pom_prev_node.left_

                    elem.key_ = pom_node.key_
                    elem.value_ = pom_node.value_

                    if pom_node.right_ is not None:
                        pom_prev_node.left_ = pom_node.right_
                    elif pom_node.right_ is None:
                        pom_prev_node.left_ = None

    def print_tree(self):
        print("==============")
        self._print_tree(self.root_, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right_, lvl + 5)
            print()
            print(lvl * " ", node.key_, node.value_)
            self._print_tree(node.left_, lvl + 5)

    def height(self, node, i=0):
        if node is None:
            return i
        left = self.height(node.left_, i + 1)
        right = self.height(node.right_, i + 1)
        return left if left > right else right


new_tree = Tree()

keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
elems = [Element(keys[i], values[i]) for i in range(len(keys))]
# elems2 = [Element(keys2[i], values[i]) for i in range(len(keys2))]
for El in elems:
    new_tree.insert(El)

keys.sort()
print('{')
for i in range(len(keys)):
    print('[', keys[i], ':', new_tree.search(keys[i], new_tree.root_), '],')
print('}')

new_tree.print_tree()
print(new_tree.search(24, new_tree.root_))
new_tree.insert(Element(20, 'AA'))
new_tree.insert(Element(6, 'M'))
keys.append(6)
new_tree.delete(62)
keys.remove(62)
new_tree.insert(Element(59, 'N'))
keys.append(59)
new_tree.insert(Element(100, 'P'))
keys.append(100)
new_tree.delete(8)
keys.remove(8)
new_tree.delete(15)
keys.remove(15)
new_tree.insert(Element(55, 'R'))
keys.append(55)
new_tree.delete(50)
keys.remove(50)
new_tree.delete(5)
keys.remove(5)
new_tree.delete(24)
keys.remove(24)
print(new_tree.height(new_tree.root_))
new_tree.print_tree()

keys.sort()
print('{')
for i in range(len(keys)):
    print('[', keys[i], ':', new_tree.search(keys[i], new_tree.root_), '],')
print('}')
