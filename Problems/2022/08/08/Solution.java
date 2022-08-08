class Solution {

    private List<Integer> list = new ArrayList<>();

    public int lengthOfLIS(int[] nums) {
        list.add(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            if (num > list.get(list.size()-1)){
                list.add(num);
            } else {
                list.set(binSearch(num), num);
            }
        }
        return list.size();
    }

    private int binSearch(int num) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m) < num) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
