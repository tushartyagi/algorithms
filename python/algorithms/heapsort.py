from random import randint
import pdb

q = [1,4,10,14,7,9,3,2,8,16]

def heapsort(xs):
    length = len(xs) - 1
    heapsize = length

    build_heap(xs)

    for i in range(length, 1, -1):
        #pdb.set_trace()
        swap(xs, 0, i)  # value at index 0 is always the maximum
        heapsize -= 1
        heapify(heapsize, xs, 0)

    return xs


def build_heap(xs):
    heapsize = len(xs) - 1
    mid = heapsize // 2 

    # building heap
    for i in range(mid, -1, -1):
        heapify(heapsize, xs, i) 


def swap(xs, i, j):
    xs[i], xs[j] = xs[j], xs[i]

    
def heapify(heapsize, xs, i):
    
    def left_child(i):
        return 2*i + 1

    def right_child(i):
        return 2*i + 2

    l = left_child(i)
    r = right_child(i)
    largest = i

    if l <= heapsize and xs[l] > xs [largest]:
        largest = l
    elif r <= heapsize and xs[r] > xs[largest]:
        largest = r

    if largest != i:
        swap(xs, i, largest)
        heapify(heapsize, xs, largest)

