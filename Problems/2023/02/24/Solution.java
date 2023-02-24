class Solution {
    public int minimumDeviation(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] % 2 == 1) {
                nums[i] *= 2;
            }
            min = Math.min(min, nums[i]);
        }

        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < nums.length; i++) {
            q.add(nums[i]);
        }

        int max = q.poll();
        int score = max - min;
        while (max % 2 == 0) {
            min = Math.min(min, max / 2);
            q.add(max / 2);
            max = q.poll();
            score = Math.min(score, max - min);
        }

        return score;
    }
}
