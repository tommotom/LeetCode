class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        long ans = 0;
        int n = nums.length;
        Map<Integer, Integer>[] counter = new Map[n];
        for (int i = 0; i < n; i++) {
            counter[i] = new HashMap<>(i);
            for (int j = 0; j < i; j++) {
                long delta = (long)nums[i] - (long)nums[j];
                if (delta < Integer.MIN_VALUE || delta > Integer.MAX_VALUE) {
                    continue;
                }
                int diff = (int) delta;
                int origin = counter[j].getOrDefault(diff, 0);
                int sum = counter[i].getOrDefault(diff, 0);
                ans += origin;
                counter[i].put(diff, origin+sum+1);
            }
        }
        return (int) ans;
    }
}
