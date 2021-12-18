# N-ARY TREES:
# - preorder (easy recursion)
# - postorder (easy recursion)
# - level-order aka bfs
#
# BINARY TREES:
# ... all the same, and
# - inorder (easy recursion)
#
# GRAPHS:
# - dfs (easy recursion: code below)
# - bfs aka level-order



# DFS:

    # (first set every visited flag to false)
    def dfs(u):
        # (visit goes here)
        u.visited = true
        for v in u.neighbors:
            if not v.visited:
                dfs(v)


# LEVEL-ORDER TRAVERSAL: (or pre-order iterative if 1. stack and 2. push children in reverse order)

    def levelorder(node):
        q = [node]
        while q:
            node = q.pop(0)
            # (visit goes here)
            q.extend(node.children)

# BFS without "parent" (where you're visiting from) info

    # (first set every visited flag to false)
    def bfs(node):  # This version of BFS does not have "parent" (where you're visiting from) info
        node.visited = true
        q = [node]
        while q:
            node = q.pop(0)
            # (visit goes here)
            for v in node.neighbors:
                if not v.visited:
                    v.visited = true
                    q.append(v)

# BFS with "parent" info

    # (first set every visited flag to false)
    def bfs(node):
        visit(node, None)
        node.visited = true
        q = [node]
        while q:
            node = q.pop(0)
            for v in node.neighbors:
                if not v.visited:
                    visit(v, node)
                    v.visited = true
                    q.append(v)
    def visit(node, via):  # via = the node you're visiting from
        # (implement me)
        pass


# Backtracking (DFS)

    def backtracking_search(state):
        if is_solved(state):
            return get_solution(state)
        for child in child_nodes(state):
            update(state, child)
            solved = backtracking_search(state)
            if solution:
                return solution
            undo_update(state, child)


# Practice problems:
# https://medium.com/techie-delight/top-25-depth-first-search-dfs-practice-problems-a620f0ab9faf
# https://medium.com/techie-delight/top-20-breadth-first-search-bfs-practice-problems-ac2812283ab1
