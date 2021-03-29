class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.i = 0

    def traverse(self, minNum, maxNum, arr):
        if self.i == len(arr) or arr[self.i] < minNum or arr[self.i] > maxNum:
            return None

        tmp = arr[self.i]
        self.i += 1
        left = self.traverse(minNum, tmp, arr)
        right = self.traverse(tmp, maxNum, arr)

        return Node(tmp, left, right)

    def convertPostOrder(self, node, answer):
        if not node:
            return

        self.convertPostOrder(node.left, answer)
        self.convertPostOrder(node.right, answer)
        answer.append(node.val)


if __name__ == "__main__":
    vals = map(lambda x: int(x), raw_input().split())
    sol = Solution()
    node = sol.traverse(-float("inf"), float("inf"), vals)
    answer = []
    sol.convertPostOrder(node, answer)
    print(answer)
