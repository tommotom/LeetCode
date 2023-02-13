class Solution {
    public int countOdds(int low, int high) {
        int l = low % 2 == 0 ? 0 : 1;
        int h = high % 2 == 0 ? 0 : 1;
        return l + h + (high - low - l - h) / 2;
    }
}
