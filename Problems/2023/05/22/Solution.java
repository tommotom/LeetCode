class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<Pair<Integer, Integer>> q = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());
        for (int key : counter.keySet()) {
            q.add(new Pair(key, counter.get(key)));
            if (q.size() > k) {
                q.poll();
            }
        }

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = q.poll().getKey();
        }
        return ans;
    }
}
