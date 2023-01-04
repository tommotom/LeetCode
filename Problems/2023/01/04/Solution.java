class Solution {
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int task : tasks) {
            counter.put(task, counter.getOrDefault(task, 0)+1);
        }

        int ans = 0;
        for (int num : counter.keySet()) {
            int count = counter.get(num);
            if (count == 1) {
                return -1;
            }
            ans += count / 3;
            if (count % 3 != 0) {
                ans++;
            }
        }

        return ans;
    }
}
