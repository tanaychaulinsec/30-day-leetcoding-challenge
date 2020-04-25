from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()
        

    def get(self, key: int) -> int:
        if self.cache.get(key):
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.cache.move_to_end(key)
        else:
            if len(self.cache)>=self.capacity:
                self.cache.popitem(last=False)
        self.cache[key]=value
            
            
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)