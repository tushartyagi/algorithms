from random import randint 
import pdb

class MaxHeap:

    def __init__(self, xs):
        self._xs = xs
        self._heapsize = len(xs)
        self._length = len(xs)

        self._build_max_heap()

    @staticmethod
    def left_child(i):
        return 2*i + 1

    @staticmethod
    def right_child(i):
        return 2*i + 2

    @staticmethod
    def parent(i):
        (i - 1) // 2

    def __getitem__(self, i):
        return self._xs[i]

    def __setitem__(self, i, v):
        self._xs[i] = v
    
    def __str__(self, i):
        return str(self.heap())
        
    def heap_size(self):
        return len(self.heap())

    def _build_max_heap(self):
        for i in range(self._length // 2, -1, -1):
            self._max_heapify(i)

    def _max_heapify(self, i):
        #pdb.set_trace()
        l = self.left_child(i)
        r = self.right_child(i)
        largest = i

        if l < self._heapsize and self[l] > self[largest]:
            largest = l
        elif r < self._heapsize and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self._max_heapify(largest)

    def heap(self):
        return self._xs

    def max(self):
        return self[0]

    def pop(self):
        return self._xs.pop(0)
    
    def extract_max(self):
        if self.heap_size() <= 0:
            raise IndexError("The heap is empty")
        top = self.pop()
        self._length = self.heap_size()
        self._heapsize = self.heap_size()
        self._build_max_heap()
        #self._max_heapify(0)
        return top
  
