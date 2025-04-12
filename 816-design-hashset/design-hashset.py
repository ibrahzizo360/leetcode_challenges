class MyHashSet:

    def __init__(self):
        arr=[]
        self.arr = arr
        

    def add(self, key: int) -> None:
        self.arr.append(key)

        

    def remove(self, key: int) -> None:
        self.arr = [x for x in self.arr if x != key ]
        

    def contains(self, key: int) -> bool:
        return key in self.arr
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)