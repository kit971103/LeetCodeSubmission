# def counter(func):
#     def proxy(self, *arg):
#         print(self.call_count)
#         self.call_count += 1
#         return func(self, *arg)
#     return proxy

class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.random_list = []
        self.call_count = 0

    # @counter 
    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        else:
            self.container[val] = len(self.random_list)
            self.random_list.append(val)
            return True
    
    # @counter 
    def remove(self, val: int) -> bool:
        if val in self.container:
            index = self.container.pop(val)
            if index+1 == len(self.random_list):
                self.random_list.pop()
            else:
                item = self.random_list.pop()
                self.random_list[index] = item
                self.container[item] = index
            return True
        else:
            return False
    
    # @counter 
    def getRandom(self) -> int:
        return random.choice(self.random_list)
    

    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()