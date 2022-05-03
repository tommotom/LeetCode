class Solution {
  public int findUnsortedSubarray(int[] nums) {
    Stack<Integer> st = new Stack<>();
    st.push(0);
    int max = nums[0];

    Integer first = null, last = null;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < max) {
        while (!st.empty() && nums[st.peek()] > nums[i]) {
          st.pop();
        }

        int tmp = st.empty() ? 0 : st.peek() + 1;
        if (first == null) {
          first = tmp;
        } else {
          first = Math.min(first, tmp);
        }

        last = i;
      }
      max = Math.max(max, nums[i]);
      st.push(i);
    }
    return first == null ? 0 : last - first + 1;
  }
}
