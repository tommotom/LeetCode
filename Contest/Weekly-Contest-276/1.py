class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        mod = len(s) % k
        if  mod != 0:
            s = s + fill * (k-mod)
        return [s[i:i+k] for i in range(0, len(s)-k+1, k)]
