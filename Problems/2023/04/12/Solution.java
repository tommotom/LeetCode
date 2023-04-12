class Solution {
    public String simplifyPath(String path) {
        String[] arr = path.split("/");
        Stack<String> st = new Stack<>();
        for (String p : arr) {
            if (p.equals(".") || p.equals("")) {
                continue;
            }
            if (p.equals("..")) {
                if (st.size() > 0) {
                    st.pop();
                }
            } else {
                st.push(p);
            }
        }

        if (st.size() == 0) {
            return "/";
        }

        StringBuilder ans = new StringBuilder();
        for (String p : st) {
            ans.append("/");
            ans.append(p);
        }
        return ans.toString();
    }
}
