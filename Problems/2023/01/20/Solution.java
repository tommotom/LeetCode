class Solution {

    private final Set<List<Integer>> ans = new HashSet<>();
    private int[] nums;

    public List<List<Integer>> findSubsequences(int[] nums) {
        this.nums = nums;
        helper(0, new Stack<>());
        return new ArrayList<>(ans);
    }

    private void helper(int i, Stack<Integer> st) {
        if (i == nums.length) {
            return;
        }
        if (st.empty() || st.peek() <= nums[i]) {
            st.push(nums[i]);
            if (st.size() > 1) {
                ans.add(new ArrayList<>(st));
            }
            helper(i+1, st);
            st.pop();
        }
        helper(i+1, st);
    }
}
