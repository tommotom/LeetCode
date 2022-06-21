class Solution {
  public int furthestBuilding(int[] heights, int bricks, int ladders) {
    PriorityQueue<Integer> ladderq = new PriorityQueue<>();
    for (int i = 0; i < heights.length-1; i++) {
      int diff = heights[i+1] - heights[i];
      if (diff <= 0) {
        continue;
      }
      ladderq.add(diff);
      if (ladderq.size() > ladders) {
        bricks -= ladderq.poll();
      }
      if (bricks < 0) {
        return i;
      }
    }
    return heights.length-1;
  }
}
