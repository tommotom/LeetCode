class Solution {
    public String addBinary(String a, String b) {
        if (a.length() < b.length()) {
            String tmp = a;
            a = b;
            b = tmp;
        }

        StringBuilder ans = new StringBuilder();

        int l = b.length();
        int c = 0;
        for (int i = 0; i < l; i++) {
            int d1 = a.charAt(a.length()-i-1) == '1' ? 1 : 0;
            int d2 = b.charAt(b.length()-i-1) == '1' ? 1 : 0;
            int sum = d1 + d2 + c;
            c = sum / 2;
            ans.append(sum % 2);
        }

        for (int i = l; i < a.length(); i++) {
            int d = a.charAt(a.length()-i-1) == '1' ? 1 : 0;
            int sum = d + c;
            c = sum / 2;
            ans.append(sum % 2);
        }

        if (c > 0) {
            ans.append(1);
        }

        return ans.reverse().toString();
    }
}
