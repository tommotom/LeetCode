class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        PriorityQueue<Pair<Integer, Integer>> q = new PriorityQueue<>((a, b) -> a.getValue() == b.getValue() ? b.getKey() - a.getKey() : b.getValue() - a.getValue());
        for (int i = 0; i < n; i++) {
            q.add(new Pair(nums1[i], nums2[i]));
        }

        PriorityQueue<Integer> maxs = new PriorityQueue<>((a, b) -> a - b);
        long sum = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < k; i++) {
            Pair<Integer, Integer> p = q.poll();
            maxs.add(p.getKey());
            sum += p.getKey();
            min = p.getValue();
        }

        long ans = sum * min;
        while (q.size() > 0) {
            Pair<Integer, Integer> p = q.poll();
            min = p.getValue();
            if (p.getKey() > maxs.peek()) {
                sum -= maxs.poll();
                sum += p.getKey();
                maxs.add(p.getKey());
            }
            ans = Math.max(ans, sum * min);
        }
        return ans;
    }
}
