class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]     
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
            
    # Without OrderedDict
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.cache = {}
    #     self.order = []

    # def get(self, key: int) -> int:
    #     if key in self.cache:
    #         self.order.remove(key) #Moving the ordering
    #         self.order.append(key)
    #         return self.cache[key]
    #     return -1
        
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.order.remove(key)
    #     self.cache[key] = value
    #     self.order.append(key)
    #     if len(self.cache) > self.capacity:
    #         to_delete = self.order[0]
    #         del self.cache[to_delete]
    #         self.order.pop(0)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)