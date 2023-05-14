class Solution {

    private int[] nums;
    private Map<Integer, Integer>[] memo;

    public int maxScore(int[] nums) {
        this.nums = nums;
        this.memo = new Map[nums.length];
        return helper(nums.length / 2, 0);
    }

    private int helper(int i, int used) {
        if (i == 0) {return 0;}
        if (memo[i] == null) {memo[i] = new HashMap<>();}
        if (memo[i].containsKey(used)) {return memo[i].get(used);}
        int score = 0;
        for (int j = 0; j < nums.length-1; j++) {
            for (int k = j+1; k < nums.length; k++) {
                if ((used & (1 << j)) > 0 || (used & (1 << k)) > 0) {
                    continue;
                }
                int tmp = used | (1 << j) | (1 << k);
                score = Math.max(score, i * gcd(nums[j], nums[k]) + helper(i-1, tmp));
            }
        }
        memo[i].put(used, score);
        return score;
    }

    private int gcd(int x, int y) {
        if (y == 0) {
            return x;
        }
        if (y > x) {
            return gcd(y, x);
        }
        return gcd(y, x % y);
    }
}
