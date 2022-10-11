class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length < 3) {return false;}

        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num <= min1) {min1 = num;}
            else if (num <= min2) {min2 = num;}
            else {return true;}
        }
        return false;
    }
}
