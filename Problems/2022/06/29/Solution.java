class Solution {
  public int[][] reconstructQueue(int[][] people) {
    Arrays.sort(people, ((a, b)->(a[0]==b[0])?(a[1]-b[1]):(b[0]-a[0])));
    List<int[]> arr = new ArrayList<>();
    for (int[] p : people) {
      arr.add(p[1], p);
    }
    return arr.toArray(new int[people.length][2]);
  }
}
