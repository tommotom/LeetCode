class Solution {

    private final Map<Integer, Integer> memo = new HashMap<>();

    public int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        }
        if (!memo.containsKey(n)) {
            int ret = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1);
            memo.put(n, ret);
        }
        return memo.get(n);
    }
}
