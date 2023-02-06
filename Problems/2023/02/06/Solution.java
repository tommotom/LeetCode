class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = nums[i];
            ys[i] = nums[i+n];
        }
        for (int i = 0; i < n; i++) {
            nums[2*i] = xs[i];
            nums[2*i+1] = ys[i];
        }
        return nums;
    }
}
