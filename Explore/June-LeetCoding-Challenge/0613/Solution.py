class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = {}
        for i, word in enumerate(words):
            node = root
            for j, c in enumerate(word):
                if not c in node:
                    node[c] = {}
                node = node[c]
                tmp = word[j+1:]
                if tmp == tmp[::-1]:
                    node.setdefault("ids", []).append(i)
            node["isWord"] = i

        ans = []
        for i, word in enumerate(words):
            word = word[::-1]
            node = root
            for j, c in enumerate(word):
                if not c in node: break
                node = node[c]
                if "isWord" in node and i != node["isWord"] and word[j+1:] == word[j+1:][::-1]:
                    ans.append([node["isWord"], i])
            else:
                if "ids" in node:
                    for j in node["ids"]:
                        if i == j or ("isWord" in node and j == node["isWord"]): continue
                        ans.append([j, i])
        if "" in words:
            i = words.index("")
            for j, word in enumerate(words):
                if word == word[::-1] and i != j:
                    ans.append([i, j])
                    ans.append([j, i])
        return ans
