class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        Arrays.sort(arr);

        int n = arr.length;
        long[] dp = new long[n];
        Arrays.fill(dp, 1);

        Map<Integer, Integer> valToI = new HashMap<>();
        for (int i = 0; i < n; i++) {
            valToI.put(arr[i], i);
        }

        int mod = 1000000007;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0) {
                    int right = arr[i] / arr[j];
                    if (valToI.containsKey(right)) {
                        dp[i] = (dp[i] + dp[j] * dp[valToI.get(right)]) % mod;
                    }
                }
            }
        }

        long ans = 0;
        for (long count : dp) {
            ans += count;
        }
        return (int) (ans % mod);
    }
}
