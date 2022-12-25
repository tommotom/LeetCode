class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int sum = 0, i = 0;
            while (i < nums.length && sum + nums[i] <= queries[q]) {
                sum += nums[i];
                i++;
            }
            ans[q] = i;
        }
        return ans;
    }
}
