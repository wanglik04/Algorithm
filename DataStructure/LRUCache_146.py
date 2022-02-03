# 这题远比想象中的复杂,听说就是相当于让你手动实现一个啥来着不记得了
# 双链表+哈希表,面试如果遇到这种题就自求多福吧
# 节点的结构也有讲究,如果没记错的话应该是要把在哈希表的键一并包含进去
# 然后删除节点的同时还要把对应的key return回去好方便在哈希表中也删掉
class Node:
    def __init__(self,val,key=None,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class Dbst:
    def __init__(self):
        self.first = Node(0)
        self.last = Node(0)
        self.first.next = self.last
        self.last.prev = self.first
    def add(self,node:Node):
        node.prev = self.first
        node.next = self.first.next
        self.first.next.prev = node
        self.first.next = node
        return node
    def delnode(self,node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.key
    def delast(self):
        return self.delnode(self.last.prev)
class LRUCache:
    def __init__(self, capacity: int):
        self.dbst = Dbst()
        self.capacity = capacity
        self.hd = {}

    def put(self, key: int, value: int) -> None:
        if self.hd.get(key):
            self.dbst.delnode(self.hd.get(key))
            self.hd[key] = self.dbst.add(Node(value, key))
            return
        if len(self.hd)==self.capacity:
            del self.hd[self.dbst.delast()]
        self.hd[key] = self.dbst.add(Node(value, key))


    def get(self, key: int) -> int:
        if self.hd.get(key):
            self.put(key,self.hd.get(key).val)
            return self.hd.get(key).val
        return -1




