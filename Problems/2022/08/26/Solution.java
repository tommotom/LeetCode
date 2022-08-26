class Solution {
    public boolean reorderedPowerOf2(int n) {
        int[] freq = count(n);
        for (int i = 0; i < 31; i++) {
            if (Arrays.equals(freq, count(1<<i))) {
                return true;
            }
        }
        return false;
    }

    private int[] count(int n) {
        int[] freq = new int[10];
        while (n > 0) {
            freq[n%10]++;
            n /= 10;
        }
        return freq;
    }
}
