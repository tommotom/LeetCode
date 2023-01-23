class Solution {
    public int findJudge(int n, int[][] trust) {
        Map<Integer, Integer> trusts = new HashMap<>();
        Map<Integer, Integer> trusted = new HashMap<>();
        for (int[] t : trust) {
            trusts.put(t[0], trusts.getOrDefault(t[0], 0) + 1);
            trusted.put(t[1], trusted.getOrDefault(t[1], 0) + 1);
        }
        for (int i = 1; i <= n; i++) {
            if (!trusts.containsKey(i) && trusted.getOrDefault(i, 0) == n-1) {
                return i;
            }
        }
        return -1;
    }
}
