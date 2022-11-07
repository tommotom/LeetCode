class Solution {
    public int maximum69Number (int num) {
        int d = 1;
        while (num / d > 9) {
            d *= 10;
        }

        while (d > 0) {
            if (num / d % 10 == 6) {
                num += 3 * d;
                break;
            }
            d /= 10;
        }

        return num;
    }
}
