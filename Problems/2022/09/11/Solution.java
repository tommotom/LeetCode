class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int[][] engineers = new int[n][2];
        for (int i = 0; i < n; i++) {
            engineers[i][0] = efficiency[i];
            engineers[i][1] = speed[i];
        }
        Arrays.sort(engineers, (a, b) -> b[0] - a[0]);

        PriorityQueue<Integer> q = new PriorityQueue<>();
        long sum = 0;
        long ans = 0;
        for (int[] engineer : engineers) {
            sum += engineer[1];
            q.add(engineer[1]);
            if (q.size()  > k) {
                sum -= q.poll();
            }
            ans = Math.max(ans, sum * engineer[0]);
        }
        return (int)(ans % 1000000007);
    }
}
