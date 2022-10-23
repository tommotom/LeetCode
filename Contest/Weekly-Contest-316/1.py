class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[1] >= event2[0] if event1[0] <= event2[0] else event2[1] >= event1[0]
