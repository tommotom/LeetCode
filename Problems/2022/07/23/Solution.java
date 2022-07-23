class Solution {
  public List<Integer> countSmaller(int[] nums) {
    ArrayList<Integer> list = new ArrayList<>();
    List<Integer> ans = new LinkedList();
    for (int i = nums.length-1; i >= 0; i--) {
      int num = nums[i];
      int j = bisect(num, list);
      ans.add(j);
      list.add(j, num);
    }
    Collections.reverse(ans);
    return ans;
  }

  private int bisect(int num, List<Integer> list) {
    int l = 0, r = list.size();
    while (l < r) {
      int m = l + (r - l) / 2;
      int n = list.get(m);
      if (n < num) {
        l = m+1;
      } else {
        r = m;
      }
    }
    return l;
  }
}
