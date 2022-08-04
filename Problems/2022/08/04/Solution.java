class Solution {
    public int mirrorReflection(int p, int q) {
        int g = gcd(p, q);
        p /= g;
        q /= g;

        if (p % 2 == 0) {
            return 2;
        }
        if (q % 2 == 0) {
            return 0;
        }
        return 1;
    }

    private int gcd(int p, int q) {
        if (q > p) {
            return gcd(q, p);
        }
        int s = p % q;
        if (s == 0) {
            return q;
        }
        return gcd(q, s);
    }
}
