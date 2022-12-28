class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        for (int pile : piles) {
            q.add(pile);
        }
        for (int i = 0; i < k; i++) {
            int tmp = q.poll();
            tmp -= tmp / 2;
            q.add(tmp);
        }
        return q.stream().mapToInt(a->a).sum();
    }
}
