class Solution:
    def robotWithString(self, s: str) -> str:
        i = s.index(min(s))
        ans = [i]

        q = []
        for j in range(i+1, len(s)):
            heapq.heappush(q, (s[j], j))

        st =[]
        for j in range(i):
            st.append(j)

        seen = set([i])
        while len(seen) < len(s):
            while q and (q[0][0] in seen or q[0][1] < i):
                heapq.heappop(q)
            while st and st[-1] in seen:
                st.pop()

            if not st:
                _, j = heapq.heappop(q)
                for k in range(i+1, j):
                    st.append(k)
                i = j
                if j in seen: continue
                ans.append(j)
                seen.add(j)
            elif not q:
                j = st.pop()
                while st and j in seen:
                    j = st.pop()
                if j in seen: continue
                ans.append(j)
                seen.add(j)
            else:
                if q[0][0] < s[st[-1]]:
                    _, j = heapq.heappop(q)
                    for k in range(i+1, j):
                        st.append(k)
                    i = j
                    if j in seen: continue
                    ans.append(j)
                    seen.add(j)
                else:
                    j = st.pop()
                    while st and j in seen:
                        j = st.pop()
                    if j in seen: continue
                    ans.append(j)
                    seen.add(j)

        return "".join([s[i] for i in ans])
