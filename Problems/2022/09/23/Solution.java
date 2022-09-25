class Solution {
    public int concatenatedBinary(int n) {
        int mod = 1000000007;
        long ans = 0;
        int d = 1;
        for (int i = 1; i <= n; i++) {
            if (1<<d <= i) {
                d++;
            }
            ans <<= d;
            ans += i;
            ans %= mod;
        }
        return (int) ans;
    }
}
