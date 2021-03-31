
from collections import defaultdict
import sys


class Solution:

    def traverse(self, nodes, adj):
        for node in nodes:
            if not node in self.visited:
                self.visited.add(node)
                self.traverse(adj[node], adj)

    def numberOfRoutes(self, adj):
        self.visited = set()
        total = 0
        for key in adj.keys():
            if not key in self.visited:
                self.visited.add(key)
                self.traverse(adj[key], adj)
                total += 1
        return total


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
    print(Solution().numberOfRoutes(adj))
