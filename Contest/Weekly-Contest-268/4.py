class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def nextArr(arr, k):
            i = len(arr) - 1
            while i >= 0:
                arr[i] += 1
                if arr[i] == k:
                    arr[i] = 0
                    i -= 1
                    continue
                break
            return arr if i >= 0 else None

        def isKMirrorNum(numk):
            num10 = str(int(numk, k))
            return num10 == num10[::-1]

        ans = count = 0
        length = 1
        while count < n:
            if length == 1:
                for num in range(1, k):
                    ans += num
                    count += 1
                    if count == n:
                        return ans
                length += 1
                continue

            half_arr = [1] + [0] * (length//2 - 1)
            centers = range(0, k) if length % 2 == 1 else [""]
            while half_arr:
                half = "".join(map(str, half_arr))
                for center in centers:
                    numk = half + str(center) + half[::-1]
                    if isKMirrorNum(numk):
                        ans += int(numk, k)
                        count += 1
                        if count == n:
                            return ans
                half_arr = nextArr(half_arr, k)
            length += 1
        return ans
