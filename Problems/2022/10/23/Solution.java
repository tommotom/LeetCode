class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] count = new int[n];
        for (int num : nums) {
            count[num-1]++;
        }

        int duplicate = 0;
        for (int i = 0; i < n; i++) {
            if (count[i] == 2) {
                duplicate = i+1;
                break;
            }
        }

        int missing = 0;
        for (int i = 0; i < n; i++) {
            if (count[i] == 0) {
                missing = i+1;
                break;
            }
        }


        return new int[] {duplicate, missing};
    }
}
