class Solution {
    public int compress(char[] chars) {
        char cur = chars[0];
        int count = 1;
        int i = 0;
        for (int j = 1; j < chars.length; j++) {
            if (chars[j] != cur) {
                chars[i] = cur;
                i++;
                if (count == 1) {
                    cur = chars[j];
                    continue;
                }
                Stack<Character> st = new Stack<>();
                while (count > 0) {
                    st.push((char) (count % 10 + '0'));
                    count /= 10;
                }
                while (!st.empty()) {
                    chars[i] = st.pop();
                    i++;
                }
                cur = chars[j];
                count = 0;
            }
            count++;
        }

        chars[i] = cur;
        i++;

        if (count == 1) {
            return i;
        }
        Stack<Character> st = new Stack<>();
        while (count > 0) {
            st.push((char) (count % 10 + '0'));
            count /= 10;
        }
        while (!st.empty()) {
            chars[i] = st.pop();
            i++;
        }

        return i;
    }
}
