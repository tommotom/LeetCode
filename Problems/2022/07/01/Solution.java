class Solution {
  public int maximumUnits(int[][] boxTypes, int truckSize) {
    Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
    int ans = 0;
    for (int[] boxType : boxTypes) {
      if (truckSize <= 0) {
        break;
      }
      int box = boxType[0];
      int unit = boxType[1];
      ans += Math.min(box, truckSize) * unit;
      truckSize -= box;
    }
    return ans;
  }
}
