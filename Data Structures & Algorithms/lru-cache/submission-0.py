class Node:
    def __init__(self,key,val):
        self.key,self.val =key,val
        self.prev =self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache ={}
        self.cap =capacity
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    
    def remove(self,node):
        #We have a reference to the node so we just remove it by disconnection
        prev,nxt =node.prev,node.next
        prev.next,nxt.prev =nxt,prev

    def insert(self, node):
        #We have a reference to the top of the queue, we put it before that
        prev, nxt =self.right.prev , self.right
        #The self.right.prev would lead to the left node from the init when we add the first value
        prev.next =nxt.prev =node
        node.next,node.prev =nxt,prev
    def get(self, key: int) -> int:
        if key in self.cache: #This is how we check for existance
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: #If it is already on the cache we remove it and add it again
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) 
        #Create node
        self.insert(self.cache[key])
        #Link it

        if len(self.cache) > self.cap: #If we go over the cap then remove the first one
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # Removes the binding I need to clarify this one.
        
