from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return

        nodes = [None] * 100
        visited = [0] * 100

        head = Node(node.val)
        nodes[node.val-1] = head

        q = deque([node])
        while q:
            target = q.popleft()

            if visited[target.val-1]: continue
            visited[target.val-1] = 1

            if not nodes[target.val-1]: nodes[target.val-1] = Node(target.val)
            clone = nodes[target.val-1]

            for adj in target.neighbors:
                if not nodes[adj.val-1]: nodes[adj.val-1] = Node(adj.val)
                adj_clone = nodes[adj.val-1]
                clone.neighbors.append(adj_clone)
                q.append(adj)

        return head
