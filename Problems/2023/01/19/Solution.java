class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> mods = new HashMap<>();
        mods.put(0, 1);
        int sum = 0, ans = 0;
        for (int num : nums) {
            sum += num;
            int mod = sum % k;
            if (mod < 0) {
                mod += k;
            }
            ans += mods.getOrDefault(mod, 0);
            mods.put(mod, mods.getOrDefault(mod, 0)+1);
        }
        return ans;
    }
}
