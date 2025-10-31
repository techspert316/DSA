from typing import List


"""
Dynamic Array Implementation:

Dynamic array contains size and capacity

Initialization:
initialize a list with size and capacity

Inserts:
- first check the size of the arr and capacity
- 

"""


class DynamicArray:
    def __init__(self, capacity: int = 10, initial_value=list()):

        self.size: int = 0
        self.capacity: int = capacity
        self.arr: List = [None] * self.capacity

    def _print_arr(self) -> List:
        return self.arr

    def _resize(self, multiplier: int):
        self.capacity = self.capacity * multiplier
        return f"New capacity is {self.capacity}"

    def append(self, value: int):
        if len(self.arr) == self.capacity:
            print(f"Capacity reached, increasing capacity")
            self._resize(2)
        self.arr[self.size] = value
        self.size += 1
        return self.arr

    def update(self, idx: int, value: int):
        self._check_index_bound(idx)
        self.arr[idx] = value

    def get(self, idx: int):
        self._check_index_bound(idx)
        return self.arr[idx]

    def _check_index_bound(self, idx: int):
        if idx > self.size:
            raise Exception("Index out of Bounds")

    def insert_at_index(self, idx: int, value: int):
        print("inserting at index")

        self._check_index_bound(idx)

        if not self.arr[idx]:
            self.arr[idx] = value
            return

        ph = self.arr[idx + 1]
        for i in range(idx, self.size):
            ph = self.arr[i + 1]
            self.arr[i + 1] = self.arr[i]

        self.arr[idx] = value
        self.size += 1

    def delete_at_index(self, idx: int):
        """ """

        self._check_index_bound(idx)
        print(f"Deleting value:{self.arr[idx]} at index {idx}")

        for i in range(idx, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1] = None
        self.size -= 1


arr = DynamicArray(10)

arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(8)
arr.append(9)
arr.append(7)

arr.update(0, 11)
print(arr.size)
print(arr._print_arr())
arr.insert_at_index(3, 17)
print(arr._print_arr())
arr.delete_at_index(0)
print(arr._print_arr())
# print(arr.size)
# arr.delete_at_index(2)
# print(arr.size)
# print(arr._print_arr())
#
