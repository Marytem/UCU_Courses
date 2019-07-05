import abc


class Heap:

    def __init__(self, heap_size=0):
        self.heap = []
        self.length = len(self.heap)
        self.heap_size = heap_size

    def right(self, i):
        return 2*i + 2

    def left(self, i):
        return 2*i + 1

    @abc.abstractmethod
    def compare(self, x, y):
        pass

    def heapify(self, heap, i):
        left = self.left(i)
        right = self.right(i)
        if left <= len(heap) - 1 and self.compare(heap[left], heap[i]):
            highest = left
        else:
            highest = i
        if right <= len(heap) - 1 and self.compare(heap[right], heap[highest]):
            highest = right
        if highest != i:
            heap[i], heap[highest] = heap[highest], heap[i]
            self.heapify(heap, highest)

    def build_heap(self, lst):
        self.heap_size = len(lst)
        for i in range(len(lst)//2, -1, -1):
            self.heapify(lst, i)

    def top(self):
        return self.heap[0]

    def extract_top(self):
        if self.heap_size:
            top = self.heap[0]
            self.heap[0] = self.heap.pop(self.heap_size - 1)
            self.heap_size -= 1
            self.heapify(self.heap, 0)
            return top
        else:
            raise Exception("The heap is empty.")

    def append_el(self, el):
        self.heap.append(el)
        self.heap_size += 1


class MaxHeap(Heap):
    def compare(self, x, y):
        if x > y:
            return True
        else:
            return False


class MinHeap(Heap):
    def compare(self, x, y):
        if x < y:
            return True
        else:
            return False


class Median:

    def __init__(self):
        self.upper = MinHeap()
        self.lower = MaxHeap()

    def add_element(self, el):

        if self.lower.heap and el < self.lower.top():
            self.lower.append_el(el)
            self.lower.build_heap(self.lower.heap)

        else:
            self.upper.append_el(el)
            self.upper.build_heap(self.upper.heap)

        if self.lower.heap_size - self.upper.heap_size == 2:
            difference = self.lower.extract_top()
            self.upper.append_el(difference)
            self.upper.build_heap(self.upper.heap)

        elif self.upper.heap_size - self.lower.heap_size == 2:
            difference = self.upper.extract_top()
            self.lower.append_el(difference)
            self.lower.build_heap(self.lower.heap)

    def get_median(self):
        if self.lower.heap_size == self.upper.heap_size:
            return self.lower.top(), self.upper.top()
        elif self.upper.heap_size > self.lower.heap_size:
            return self.upper.top()
        else:
            return self.lower.top()

    def get_maxheap_elements(self):
        return self.lower.heap

    def get_minheap_elements(self):
        return self.upper.heap
