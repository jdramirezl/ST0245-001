from random import randrange
from Graph import Graph
import time

def lcs(word1, word2, longest, shortest):
    time.sleep(0.001)
    if longest == 0 or shortest == 0:
        return 0
    if word1[longest-1] == word2[shortest-1]:
        return 1 + lcs(word1, word2, longest-1, shortest-1)
    else:
        return max(lcs(word1, word2, longest, shortest-1), lcs(word1, word2, longest-1, shortest))


if __name__ == '__main__':
    args = [(x, str(randrange(x-100, x)), str(randrange(x-100, x))) for x in range(10000, 300000, 10000)]
    Graph(lcs, args, "Longest Common Subsequence")
