class Solution {
    public int sumSubarrayMins(int[] arr) {
        int mod = 1000000007;
        long sum = 0;

        Stack<Integer> st = new Stack<>();
        for (int i = 0; i <= arr.length; i++) {
            while (!st.empty() && (i == arr.length || arr[st.peek()] >= arr[i])) {
                int m = st.pop();
                int l = st.empty() ? -1 : st.peek();
                int r = i;

                long count = (m - l) * (r - m) % mod;
                sum += (count * arr[m]) % mod;
                sum %= mod;
            }
            st.push(i);
        }
        return (int) sum;
    }
}
