order = [1,4,6,10,0,0,0,7,0,8,0,0,2,5,0,0,3,9,0,0,0]

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:

    def __init__(self, preorder_list):

        self.preorder_list = preorder_list
        self.sorted_ord = sorted([el for el in self.preorder_list if el != 0])
        if preorder_list:
            self.main = Node(preorder_list.pop(0))
        else:
            self.main = None
        self.leaves = []
        self.build(self.main, self.preorder_list[:])
        self.change_keys(self.sorted_ord, self.main)
        for l in self.leaves:
            print(l.data)

    def build(self, main, lst):
        if lst[0] != 0:
            main.left = Node(lst.pop(0), parent=main)
            self.build(main.left, lst)
        else:
            lst.pop(0)

        if lst[0] != 0:
            main.right = Node(lst.pop(0), parent=main)
            self.build(main.right, lst)
        else:
            lst.pop(0)
            if not main.left:
                self.leaves.append(main)

    def change_keys(self, lst, x):
        if x is not None:
            self.change_keys(lst, self.left(x))
            x.data = lst.pop(0)
            self.change_keys(lst, self.right(x))

    def find_sum(self, s):
        pass

    def root(self):
        if self.main:
            return self.main
        return None

    def parent(self, x):
        if x.parent:
            return x.parent
        return None

    def left(self, x):
        if x.left:
            return x.left
        return None

    def right(self, x):
        if x.right:
            return x.right
        return None

    def key(self, x):
        return x.data

tr = BinarySearchTree(order)
