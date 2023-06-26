class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> left = new PriorityQueue<>();
        PriorityQueue<Integer> right = new PriorityQueue<>();
        int l = 0, r = costs.length-1;
        for (int i = 0; i < candidates; i++) {
            left.add(costs[l++]);
            if (l > r) { break; }
            right.add(costs[r--]);
            if (l > r) { break; }
        }

        long ans = 0;
        for (int i = 0; i < k; i++) {
            if (left.isEmpty()) {
                ans += right.poll();
                continue;
            } else if (right.isEmpty()) {
                ans += left.poll();
                continue;
            }
            if (left.peek() <= right.peek()) {
                ans += left.poll();
                if (l <= r) {
                    left.add(costs[l++]);
                }
            } else {
                ans += right.poll();
                if (l <= r) {
                    right.add(costs[r--]);
                }
            }
        }
        return ans;
    }
}
