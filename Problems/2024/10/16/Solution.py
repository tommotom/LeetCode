class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        heapq.heappush(q, (-a, 'a'))
        heapq.heappush(q, (-b, 'b'))
        heapq.heappush(q, (-c, 'c'))
        st = []

        while len(q) > 0:
            count, c = heapq.heappop(q)
            if count == 0: continue
            if len(st) > 1 and st[-1] == c and st[-2] == c:
                if len(q) == 0: break
                count2, c2 = heapq.heappop(q)
                if count2 < 0:
                    st.append(c2)
                    heapq.heappush(q, (count2+1, c2))
                heapq.heappush(q, (count, c))
            else:
                st.append(c)
                heapq.heappush(q, (count+1, c))

        return ''.join(st)
