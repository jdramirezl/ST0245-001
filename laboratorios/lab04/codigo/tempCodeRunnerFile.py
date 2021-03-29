vals = line.split()
    sol = Solution()
    node = sol.traverse(-float("inf"), float("inf"), vals)
    answer = []
    sol.convertPostOrder(node, answer)
    print(answer)