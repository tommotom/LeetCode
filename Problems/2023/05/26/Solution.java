class Solution {

    int[] piles;
    Map<Pair<Integer, Integer>, Integer> alice = new HashMap<>();
    Map<Pair<Integer, Integer>, Integer> bob = new HashMap<>();

    public int stoneGameII(int[] piles) {
        this.piles = piles;
        return helper(0, 1, true);
    }

    private int helper(int i, int M, boolean isAlice) {
        if (i == piles.length) {return 0;}

        Pair<Integer, Integer> key = new Pair(i, M);

        if (isAlice && alice.containsKey(key)) {
            return alice.get(key);
        }
        if (!isAlice && bob.containsKey(key)) {
            return bob.get(key);
        }

        int took = 0;
        int ans = isAlice ? 0 : Integer.MAX_VALUE;
        for (int X = 1; X <= 2*M; X++) {
            int j = i + X - 1;
            if (j == piles.length) {break;}
            took += piles[j];

            if (isAlice) {
                ans = Math.max(ans, took + helper(j+1, Math.max(M, X), false));
            } else {
                ans = Math.min(ans, helper(j+1, Math.max(M, X), true));
            }
        }

        if (isAlice) {
            alice.put(key, ans);
        } else {
            bob.put(key, ans);
        }

        return ans;
    }
}
