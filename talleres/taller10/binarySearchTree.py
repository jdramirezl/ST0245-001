
class Node:
    def __init__(self, name=None, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, name, val):
        self.root = Node(name, val)

    def insert(self, name, val):
        tmp = self.root
        while True:
            if tmp.val > val:
                if not tmp.left:
                    tmp.left = Node(name, val)
                    break
                tmp = tmp.left
            elif tmp.val < val:
                if not tmp.right:
                    tmp.right = Node(name, val)
                    break
                tmp = tmp.right
