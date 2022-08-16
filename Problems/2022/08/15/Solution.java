class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> toInt = new HashMap<>();
        toInt.put('I', 1);
        toInt.put('V', 5);
        toInt.put('X', 10);
        toInt.put('L', 50);
        toInt.put('C', 100);
        toInt.put('D', 500);
        toInt.put('M', 1000);

        int ans = 0;
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (i < s.length() - 1) {
                char n = s.charAt(i+1);
                if (c == 'C' && n == 'M') {
                    ans += 900;
                } else if (c == 'C' && n == 'D') {
                    ans += 400;
                } else if (c == 'X' && n == 'C') {
                    ans += 90;
                } else if (c == 'X' && n == 'L') {
                    ans += 40;
                } else if (c == 'I' && n == 'X') {
                    ans += 9;
                } else if (c == 'I' && n == 'V') {
                    ans += 4;
                } else {
                    ans += toInt.get(c);
                    i--;
                }
                i += 2;
            } else {
                ans += toInt.get(c);
                i += 1;
            }
        }
        return ans;
    }
}
