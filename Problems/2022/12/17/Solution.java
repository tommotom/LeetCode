class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (isNum(tokens[i])) {
                st.push(Integer.parseInt(tokens[i]));
                continue;
            }

            int a = st.pop(), b = st.pop();
            switch(tokens[i]) {
                case "+":
                    b += a;
                    break;
                case "-":
                    b -= a;
                    break;
                case "*":
                    b *= a;
                    break;
                case "/":
                    b /= a;
                    break;
            }
            st.push(b);
        }

        return st.pop();
    }

    private boolean isNum(String token) {
        return token.length() > 1 && token.charAt(0) == '-'
                ? token.substring(1, token.length()).chars().allMatch(Character::isDigit)
                : token.chars().allMatch(Character::isDigit);
    }
}
