"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        org_map = {node.val: node}
        q = deque([node])
        while q:
            o = q.popleft()
            for nei in o.neighbors:
                if nei.val in org_map: continue
                org_map[nei.val] = nei
                q.append(nei)

        clone_map = {node.val: Node(node.val)}
        for n in org_map.values():
            if not n.val in clone_map:
                clone_map[n.val] = Node(n.val)
            for nei in n.neighbors:
                if nei.val not in clone_map:
                    clone_map[nei.val] = Node(nei.val)
                clone_map[n.val].neighbors.append(clone_map[nei.val])

        return clone_map[node.val]
