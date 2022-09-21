class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int sum = Arrays.stream(nums).filter(num->num%2==0).sum();
        int[] ans = new int[queries.length];
        int j = 0;
        for (int[] query : queries) {
            int i = query[1];
            if (nums[i] % 2 == 0) {
                sum -= nums[i];
            }
            nums[i] += query[0];
            if (nums[i] % 2 == 0) {
                sum += nums[i];
            }
            ans[j] = sum;
            j++;
        }
        return ans;
    }
}
