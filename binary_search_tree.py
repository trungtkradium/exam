class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            cur = self.root
            while True:
                if value < cur.value:
                    if cur.left == None:
                        cur.left = newNode
                        return
                    cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = newNode
                        return
                    cur = cur.right
                    
    def findAncestors(self, k):
        result = []
        if self.root == None:
            return result
        cur = self.root
        while cur is not None:
            if cur.value == k:
                return result
            result.append(cur.value)
            if k < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        if cur == None:
            return []
        return result