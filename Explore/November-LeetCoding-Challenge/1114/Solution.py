from math import ceil
from math import log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest // minutesToDie + 1))
