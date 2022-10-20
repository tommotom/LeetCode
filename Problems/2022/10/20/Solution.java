class Solution {
    public String intToRoman(int num) {
        Object[][] trans = new Object[][] {
                {1000, "M"},
                {900, "CM"},
                {500, "D"},
                {400, "CD"},
                {100, "C"},
                {90, "XC"},
                {50, "L"},
                {40, "XL"},
                {10, "X"},
                {9, "IX"},
                {5, "V"},
                {4, "IV"},
                {1, "I"}
        };

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < trans.length; i++) {
            int n = (int) trans[i][0];
            String s = (String) trans[i][1];

            int count = num / n;
            for (int c = 0; c < count; c++) {
                sb.append(s);
                num -= n;
            }
        }

        return sb.toString();
    }
}
