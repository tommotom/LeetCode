class Solution {
    public boolean isPossible(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0)+1);
        }

        Map<Integer, Integer> canPut = new HashMap<>();
        for (int num : nums) {
            if (counter.get(num) == 0) {
                continue;
            }

            if (canPut.getOrDefault(num, 0) > 0) {
                counter.put(num, counter.get(num)-1);
                canPut.put(num, canPut.get(num)-1);

                canPut.put(num+1, canPut.getOrDefault(num+1, 0)+1);
            } else if (counter.get(num) > 0 && counter.getOrDefault(num+1, 0) > 0 && counter.getOrDefault(num+2, 0) > 0) {
                counter.put(num, counter.get(num)-1);
                counter.put(num+1, counter.get(num+1)-1);
                counter.put(num+2, counter.get(num+2)-1);

                canPut.put(num+3, canPut.getOrDefault(num+3, 0)+1);
            } else {
                return false;
            }
        }
        return true;
    }
}
