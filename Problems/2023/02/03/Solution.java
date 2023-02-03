class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int next = 1, index = 0;
        for (char c : s.toCharArray()) {
            rows[index].append(c);
            if (index == 0) {
                next = 1;
            } else if (index == numRows-1) {
                next = -1;
            }
            index += next;
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            ans.append(rows[i].toString());
        }

        return ans.toString();
    }
}
