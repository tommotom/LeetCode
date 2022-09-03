class Solution {

    private List<Integer> ans = new ArrayList<>();

    public int[] numsSameConsecDiff(int n, int k) {
        for (int i = 1; i < 10; i++) {
            helper(n-1, i, k);
        }
        return ans.stream().mapToInt(i->i).toArray();
    }

    public void helper(int n, int num, int k) {
        if (n == 0) {
            ans.add(num);
            return;
        }
        int tmp = num % 10;
        if (tmp + k < 10) {
            helper(n-1, num*10 + tmp+k, k);
        }
        if (k > 0 && tmp - k >= 0) {
            helper(n-1, num*10 + tmp-k, k);
        }
    }
}
