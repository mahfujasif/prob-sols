class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        pop_v = self.arr[self.length]
        self.arr[self.length] = 0
        return pop_v

    def resize(self) -> None:
        self.capacity *= 2
        n_arr = [0] * self.capacity
        for i in range(self.length):
            n_arr[i] = self.arr[i]
        self.arr = n_arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

