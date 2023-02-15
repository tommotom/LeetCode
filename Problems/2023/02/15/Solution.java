class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        int i = num.length-1;
        int c = 0;
        List<Integer> ans = new ArrayList<>();
        while (i >= 0) {
            num[i] += c + k % 10;
            c = num[i] / 10;
            ans.add(num[i] % 10);
            num[i] %= 10;
            k /= 10;
            i--;
        }
        k += c;
        while (k > 0) {
            ans.add(k % 10);
            k /= 10;
        }
        Collections.reverse(ans);
        return ans;
    }
}
