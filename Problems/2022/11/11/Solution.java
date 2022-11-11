class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 1;
        int num = nums[0];
        for (int j = 0; j < nums.length; j++) {
            if (num != nums[j]) {
                nums[i] = nums[j];
                num = nums[j];
                i++;
            }
        }
        return i;
    }
}
