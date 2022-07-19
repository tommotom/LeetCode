class Solution {
  public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> ans = new ArrayList<>();
    ans.add(Arrays.asList(new Integer[]{1}));
    while (--numRows > 0) {
      List<Integer> row = new ArrayList<>();
      row.add(1);
      List<Integer> prev = ans.get(ans.size()-1);
      for (int i = 1; i < prev.size(); i++) {
        row.add(prev.get(i-1) + prev.get(i));
      }
      row.add(1);
      ans.add(row);
    }
    return ans;
  }
}
