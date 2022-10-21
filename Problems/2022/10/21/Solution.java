class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> seenAt = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (seenAt.containsKey(num) && i - seenAt.get(num) <= k) {
                return true;
            }
            seenAt.put(num, i);
        }
        return false;
    }
}
