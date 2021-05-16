class Solution:
    def minSwaps(self, s: str) -> int:
        counter = Counter(s)
        if abs(counter['0'] - counter['1']) > 1: return -1

        a, b = '1', '0'
        dist_a, dist_b = 0, 0
        for c in s:
            if c != a:
                dist_a += 1
            if c != b:
                dist_b += 1
            a, b = b, a
        if dist_a % 2 == 0 and dist_b % 2 == 0:
            return min(dist_a//2, dist_b//2)
        elif dist_a %2 == 0:
            return dist_a//2
        elif dist_b%2 == 0:
            return dist_b//2
