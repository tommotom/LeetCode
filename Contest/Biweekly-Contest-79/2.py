class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(int)
        for m, s in zip(messages, senders):
            counter[s] += len(m.split())
        largest = 0
        ans = None
        for k, v in counter.items():
            if largest < v:
                largest = v
                ans = k
            elif largest == v and ans < k:
                largest = v
                ans = k
        return ans
