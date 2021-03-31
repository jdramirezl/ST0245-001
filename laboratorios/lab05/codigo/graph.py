
from collections import defaultdict
import sys


class Solution:

    def traverse(self, nodes, adj, color):

        canBeColored = True
        for node in nodes:
            if not node in self.visited:
                self.nodeColors[node] = color
                self.visited.add(node)
                canBeColored = canBeColored and self.traverse(
                    adj[node], adj, - color)
            elif self.nodeColors[node] == color:
                return False
        return canBeColored

    def color(self, adj):
        self.nodeColors = defaultdict(0)
        self.visited = set()
        self.nodeColors[0] = 1
        self.visited.add(0)
        return self.traverse(adj[0], adj, 1)


if __name__ == '__main__':
    nodes = int(input())
    adj = defaultdict(list)
    for i in range(nodes):
        connections = int(input())
        while connections:
            con = int(input())
            if con >= i:
                sys.exit(1)
            adj[i].append(con)
            connections -= 1
    print(Solution().color(adj))
