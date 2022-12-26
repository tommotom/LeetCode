class Solution {

    private boolean[] visited;
    private int[] nums;

    public boolean canJump(int[] nums) {
        this.visited = new boolean[nums.length];
        this.nums = nums;
        return helper(0);
    }

    private boolean helper(int i) {
        if (i >= nums.length-1) {
            return true;
        }
        if (visited[i]) {
            return false;
        }
        visited[i] = true;
        for (int j = i + nums[i]; j > i; j--) {
            if (helper(j)) {return true;}
        }
        return false;
    }
}
