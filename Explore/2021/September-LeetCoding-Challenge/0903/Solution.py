class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 2: return trees


        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def dist(p, q):
            return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

        def compare(p, q):
            nonlocal bm
            diff = orientation(bm, p, q) - orientation(bm, q, p)
            if diff == 0:
                return dist(bm, p) - dist(bm, q)
            else:
                return 1 if diff > 0 else -1;


        trees.sort(key=lambda x: x[1])
        bm = trees[0]
        trees = sorted(trees, key=cmp_to_key(compare))

        i = len(trees) - 1
        while i >= 0 and orientation(bm, trees[-1], trees[i]) == 0:
            i -= 1
        i += 1
        j = len(trees) - 1
        while i < j:
            trees[i], trees[j] = trees[j], trees[i]
            i += 1
            j -= 1

        stack = []
        stack.append(trees[0])
        stack.append(trees[1])

        for tree in trees[2:]:
            top = stack.pop()
            while orientation(stack[-1], top, tree) > 0:
                top = stack.pop()
            stack.append(top)
            stack.append(tree)

        return stack
