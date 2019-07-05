from task_03 import Median

b = Median()
b.add_element(5)
print(b.get_maxheap_elements())
print(b.get_minheap_elements())

b.add_element(4)
print(b.get_maxheap_elements())
print(b.get_minheap_elements())

b.add_element(6)
print(b.get_maxheap_elements())
print(b.get_minheap_elements())

b.add_element(8)
print(b.get_maxheap_elements())
print(b.get_minheap_elements())


import random

ascend = Median()
for i in range(11):
    ascend.add_element(i)
print(ascend.get_median())


descend = Median()
for i in reversed(range(11)):
    descend.add_element(i)
print(descend.get_median())


rand = Median()
for i in reversed(range(23)):
    rand.add_element(random.randrange(100))
print(rand.get_median())
print(rand.get_maxheap_elements())
print(rand.get_minheap_elements())
