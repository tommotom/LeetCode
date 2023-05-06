class Solution {

    private static final int MOD = 1000000007;

    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        long ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int l = i, r = nums.length;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (nums[i] + nums[m] > target) {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            l--;
            if (l < i) {
                continue;
            }
            ans += modPow(2, l-i);
            ans %= MOD;
        }
        return (int) ans;
    }

    public static long modPow(long a, int n) {
        long ret = 1L, tmp = a;
        while (n > 0) {
            if (n % 2 == 1) {
                ret *= tmp;
                ret %= MOD;
            }
            tmp *= tmp;
            tmp %= MOD;
            n >>= 1;
        }
        return ret;
    }
}
