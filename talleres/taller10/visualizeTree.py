
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node, level):
    if not node:
        return None

    left = traverse(node.left, level + 1)
    right = traverse(node.right, level + 1)
    tabs = "".join(["\t" for _ in range(level)])
    if not left and not right:
        return f"{tabs}{node.val};"
    if left and not right:
        return f"{tabs}{node.val} -> {left}"
    if right and not left:
        return f"{tabs}{node.val} -> {right}"
    return f"{tabs}{node.val}" + "{" + f"\n{tabs}\t{left}\n{tabs}\t{right}\n" + f"{tabs}" + "}"


def createGraph():
    n = Node(val=1, left=Node(val=2, left=Node(val=5), right=Node(val=6)),
             right=Node(val=4, right=Node(val=10)))
    print(traverse(n, 0))


createGraph()
