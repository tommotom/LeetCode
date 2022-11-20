class Solution {

    private final Map<Integer, Integer> brackets = new HashMap<>();

    public int calculate(String s) {
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(i);
            } else if (s.charAt(i) == ')') {
                brackets.put(st.pop(), i);
            }
        }

        return calculate(s, 0, s.length());
    }

    private int calculate(String s, int start, int end) {
        int ret = 0, sign = 1, i = start;
        while (i < end) {
            char c  = s.charAt(i);
            if (Character.isDigit(c)) {
                int j = i+1;
                while (j < end && Character.isDigit(s.charAt(j))) {
                    j += 1;
                }
                ret += sign * Integer.parseInt(s.substring(i, j));
                i = j;
                continue;
            }
            if (c == '(') {
                ret += sign * calculate(s, i+1, brackets.get(i));
                i = brackets.get(i) + 1;
                continue;
            }
            if (c == '+') {
                sign = 1;
            } else if (c == '-') {
                sign = -1;
            }

            i++;
        }
        return ret;
    }
}
