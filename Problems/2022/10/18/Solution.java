class Solution {
    public String countAndSay(int n) {
        if (n == 1) {return "1";}
        String prev = countAndSay(n-1);
        StringBuilder sb = new StringBuilder();
        char p = prev.charAt(0);
        int count = 0;
        for (char c : prev.toCharArray()) {
            if (c == p) {
                count++;
            } else {
                sb.append(count);
                sb.append(p);
                p = c;
                count = 1;
            }
        }
        sb.append(count);
        sb.append(p);
        return sb.toString();
    }
}
