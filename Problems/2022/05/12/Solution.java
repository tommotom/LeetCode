class Solution {

  private HashMap<Integer, Integer> counter = new HashMap<>();
  private List<List<Integer>> ans = new ArrayList<>();
  private int n;

  public List<List<Integer>> permuteUnique(int[] nums) {
    n = nums.length;
    for (int num : nums) {
      counter.put(num, counter.getOrDefault(num, 0)+1);
    }

    helper(new Stack<Integer>(), new ArrayList<Integer>(counter.keySet()));

    return ans;
  }

  private void helper(Stack<Integer> st, List<Integer> keys) {
    if (st.size() == n) {
      ans.add(new ArrayList(st));
      return;
    }
    for (int i = 0; i < keys.size(); i++) {
      Integer key = keys.get(i);
      if (counter.get(key) == 0) {
        continue;
      }
      counter.put(key, counter.get(key)-1);
      st.push(key);
      helper(st, keys);
      st.pop();
      counter.put(key, counter.get(key)+1);
    }
  }
}
