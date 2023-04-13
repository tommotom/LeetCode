class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int n = pushed.length, i = 0;
        Stack<Integer> st = new Stack<>();
        for (int j = 0; j < n; j++) {
            st.push(pushed[j]);
            while (st.size() > 0 && st.peek() == popped[i]) {
                st.pop();
                i++;
            }
        }
        while (i < n) {
            if (st.pop() != popped[i]) {
                return false;
            }
            i++;
        }
        return true;
    }
}
