from abc import abstractmethod


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class HashTable:

    def __init__(self, hash_type, values):
        self.hash_type = hash_type
        self.values = values
        if self.hash_type == 1:
            self.hash_table = DivisionChained(values)
        if self.hash_type == 2:
            self.hash_table = MultiplicationChained(values)
        if self.hash_type == 3:
            self.hash_table = LinearOpenAddr(values)
        if self.hash_type == 4:
            self.hash_table = QuadrOpenAddr(values)
        if self.hash_type == 5:
            self.hash_table = DoubleOpenAddr(values)

    def get_collisions_amount(self):
        return len(self.hash_table.values) + len([el for el in self.hash_table.table if el is None])\
               - self.hash_table.tab_length

    def find_sum(self, s):
        for value in self.hash_table.values:
            if self.hash_table.get_val(s - value):
                return value, s - value
        return None


class HashTab:

    def __init__(self, values):
        self.collisions = 0
        self.values = values
        self.tab_length = len(values)*3
        self.set_tab_length()
        self.table = [None for _ in range(self.tab_length)]
        self.build_tab()

    @abstractmethod
    def build_tab(self):
        pass

    @abstractmethod
    def set_tab_length(self):
        pass


class ChainedTab(HashTab):

    def build_tab(self):
        for value in self.values:
            current_node = Node(value)
            if self.table[self.hash(value)] is None:
                self.table[self.hash(value)] = current_node
            else:
                self.collisions += 1
                current_chain = self.table[self.hash(value)]
                while current_chain.next:
                    current_chain = current_chain.next
                current_chain.next = current_node

    def get_val(self, value):
        current_chain = self.table[self.hash(value)]
        if current_chain:
            while current_chain.next and current_chain.value != value:
                current_chain = current_chain.next
            if current_chain.value == value:
                return current_chain.value
        return None


    @abstractmethod
    def hash(self, value):
        return 0


class DivisionChained(ChainedTab):

    def set_tab_length(self):
        good_pr = [1, 3, 7, 13, 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241]
        min_pos_dif = lambda x: min([x - pr for pr in good_pr if x - pr > 0])
        self.tab_length = len(self.values) * 3 - min_pos_dif(len(self.values) * 3)

    def hash(self, value):
        return value % self.tab_length


class MultiplicationChained(ChainedTab):

    def set_tab_length(self):
        powers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
        min_pos_dif = lambda x: min([x - pow for pow in powers if x - pow > 0])
        self.tab_length = len(self.values) * 3 - min_pos_dif(len(self.values) * 3)

    def hash(self, value):
        return int((value * 0.61803399 % 1) * self.tab_length)


test = HashTable(3, [1, 2, 3])
print(test.find_sum(6))

class OpenAddr(HashTab):

    def build_tab(self):
        for value in self.values:
            i = 0
            while i != self.tab_length:
                j = hash(value, i)
                if self.table[j] is None:
                    self.table = value
                else:
                    i += 1
            raise Exception("HashTable is full")

    def get_val(self, value):
        i = 0
        while i != self.tab_length:
            j = hash(value, i)
            if self.table[j] == value:
                return value
            else:
                i += 1
        return None

    def set_tab_length(self):
        self.tab_length = len(self.values) * 3

    @abstractmethod
    def hash(self, value, i):
        pass


class LinearOpenAddr(OpenAddr):

    def hash(self, value, i):
        return (value % self.tab_length + i) % self.tab_length


class QuadrOpenAddr(OpenAddr):

    def hash(self, value, i):
        return (value % self.tab_length + 5*i + 2*i**2) % self.tab_length

class DoubleOpenAddr(OpenAddr):

    def h1(self, value):
        return value % self.tab_length

    def h2(self, value):
        return value % (self.tab_length-1)

    def hash(self, value, i):
        return (self.h1(value) + i * self.h2(value))% self.tab_length

