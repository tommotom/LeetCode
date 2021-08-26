class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#": return True

        preorder_arr = preorder.split(",")
        if preorder_arr[0] == "#": return False

        stack = [[preorder_arr[0], False, False]]
        for node in preorder_arr[1:]:
            if not stack: return False
            if node != "#":
                stack.append([node, False, False])
            else:
                while stack:
                    if not stack[-1][1]:
                        stack[-1][1] = True
                        break
                    stack.pop()
        return stack == []
