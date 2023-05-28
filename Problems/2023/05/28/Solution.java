class Solution {

    private int[] cuts;
    private final Map<Pair<Integer, Integer>, Integer> memo = new HashMap<>();

    public int minCost(int n, int[] cuts) {
        Arrays.sort(cuts);
        this.cuts = new int[cuts.length+2];
        this.cuts[this.cuts.length-1] = n;
        System.arraycopy(cuts, 0, this.cuts, 1, cuts.length);
        return helper(0, this.cuts.length-1);
    }

    private int helper(int i, int j) {
        if (i+1 == j) {return 0;}
        Pair<Integer, Integer> key = new Pair(i, j);
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        int ans = Integer.MAX_VALUE;
        int l = cuts[j] - cuts[i];
        for (int k = i+1; k < j; k++) {
            ans = Math.min(ans, l + helper(i, k) + helper(k, j));
        }
        memo.put(key, ans);
        return ans;
    }
}
