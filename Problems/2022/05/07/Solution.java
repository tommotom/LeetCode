class Solution {
  public boolean find132pattern(int[] nums) {
    int n = nums.length;

    int[] mins = Arrays.copyOf(nums, n);
    for (int i = 1; i < n; i++) {
      mins[i] = Math.min(mins[i], mins[i-1]);
    }

    Stack<Integer> st = new Stack<>();
    for (int i = n-1; i >= 0; i--) {
      if (mins[i] < nums[i]) {
        while (!st.empty() && st.peek() <= mins[i]) {
          st.pop();
        }
        if (!st.empty() && st.peek() < nums[i]) {
          return true;
        }
        st.push(nums[i]);
      }
    }
    return false;
  }
}
