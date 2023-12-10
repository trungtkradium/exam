class Node:
    def __init__(self, value: int):
        self.value = value
        self.node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

    def insert(self, value:int):
        newNode = Node(value)

        if str(value) in self.map:
            self.map[str(value)] = self.map[str(value)] + 1
        else:
            self.map[str(value)] = 1

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.node = newNode
            self.tail = newNode
    
    def remove(self, node: Node):
        if self.head == None or node == None:
            return
        cur = self.head
        if cur == node:
            self.head = cur.node
            if self.tail == cur:
                self.tail = None
            node.node = None
            return
        
        while cur.node is not None:
            if cur.node == node:
                cur.node = node.node
                if cur.node == self.tail:
                    self.tail = node.node
                node.node = None
                break
            cur = cur.node
    
    def remove_duplicates(self):
        if self.head == None:
            return
        cur = self.head
        while cur is not None:
            valueString = str(cur.value)
            if str(cur.value) in self.map:
                if self.map[valueString] != 1:
                    nextNode = cur.node
                    self.remove(cur)
                    cur = nextNode
                    self.map[valueString] = self.map[valueString] - 1
                    continue
            cur = cur.node

    def traverse(self):
        if self.head == None:
            return []
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.value)
            cur = cur.node