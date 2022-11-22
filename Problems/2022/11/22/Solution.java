class Solution {
    public int numSquares(int n) {
        int[] nums = new int[n+1];
        Deque<Integer> q = new ArrayDeque<>();
        q.add(n);
        while (q.size() > 0) {
            int cur = q.poll();
            for (int i = (int) Math.sqrt(cur); i > 0; i--) {
                int next = cur - i * i;
                if (next == 0) {return nums[cur] + 1;}
                if (nums[next] > 0) {continue;}
                nums[next] = nums[cur] + 1;
                q.add(next);
            }
        }
        return -1;
    }
}
