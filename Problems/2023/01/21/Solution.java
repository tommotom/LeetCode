class Solution {

    private final List<String> ans = new ArrayList<>();
    private String s;

    public List<String> restoreIpAddresses(String s) {
        this.s = s;
        helper(0, new Stack<>());
        return ans;
    }

    private void helper(int i, Stack<String> st) {
        if (i == s.length()) {
            if (st.size() == 4) {
                ans.add(toIP(st));
            }
            return;
        }
        st.push(s.substring(i, i+1));
        helper(i+1, st);
        st.pop();
        if (s.charAt(i) == '0' || i+1 == s.length()) {
            return;
        }
        st.push(s.substring(i, i+2));
        helper(i+2, st);
        st.pop();

        if (i+2 == s.length()) {
            return;
        }
        int num = Integer.parseInt(s.substring(i, i+3));
        if (num <= 255) {
            st.push(s.substring(i, i+3));
            helper(i+3, st);
            st.pop();
        }
    }

    private String toIP(Stack<String> st) {
        StringBuilder sb = new StringBuilder();
        for (String s : st) {
            sb.append(s);
            sb.append('.');
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}
