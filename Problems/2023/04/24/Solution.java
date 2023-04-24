class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) {
            q.add(s);
        }

        while (q.size() > 1) {
            int s1 = q.poll(), s2 = q.poll();
            if (s1 == s2) {continue;}
            q.add(s1 - s2);
        }

        return q.isEmpty() ? 0 : q.poll();
    }
}
