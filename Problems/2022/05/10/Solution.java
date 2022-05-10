class Solution {

  private List<List<Integer>> ans = new ArrayList<>();

  public List<List<Integer>> combinationSum3(int k, int n) {
    helper(k, n, 1, new Stack<Integer>());
    return ans;
  }

  private void helper(int k, int n, int num, Stack st) {
    if (k == 0 && n == 0) {
      ans.add(new ArrayList(st));
      return;
    }
    if (num == 10 || n < num || k == 0) {
      return;
    }
    st.push(num);
    helper(k-1, n-num, num+1, st);
    st.pop();
    helper(k, n, num+1, st);
  }
}
