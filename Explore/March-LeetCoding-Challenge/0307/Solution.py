class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashMap = [[-1] * 1000 for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket, idx = self._index(key)
        bucket[idx] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket, idx = self._index(key)
        return bucket[idx]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket, idx = self._index(key)
        bucket[idx] = -1

    def _hash(self, key):
        return key//1000, key%1000

    def _index(self, key):
        bucketKey, idx = self._hash(key)
        return self.hashMap[bucketKey], idx

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
