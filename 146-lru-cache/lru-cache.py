class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
    
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def insert(self, node):
        p = self.right.prev
        p.next = node
        node.prev = p
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
        
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)