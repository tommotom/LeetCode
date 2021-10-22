class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        arr = []
        for k, v in sorted(c.items(), key=lambda x: (x[1], x[0]), reverse=True):
            for _ in range(v):
                arr.append(k)
        return "".join(arr)
