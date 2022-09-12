class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int ans = 0, score = 0, l = 0, r = tokens.length;
        while (l < r) {
            if (tokens[l] <= power) {
                power -= tokens[l];
                score++;
                l++;
                ans = Math.max(ans, score);
            } else if (score > 0) {
                r--;
                score--;
                power += tokens[r];
            } else {
                break;
            }
        }
        return ans;
    }
}
