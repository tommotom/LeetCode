class Solution {
  public int divide(int dividend, int divisor) {
    long sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
    long lDividend = Math.abs((long) dividend);
    long lDivisor = Math.abs((long) divisor);
    long quotient = 0, temp = 0;
    for (int i = 31; i >= 0; i--) {
      if (temp + (lDivisor << i) <= lDividend) {
        temp += lDivisor << i;
        quotient |= 1L << i;
      }
    }
    if (sign * quotient > Integer.MAX_VALUE) return Integer.MAX_VALUE;
    return (int) (sign * quotient);
  }
}
