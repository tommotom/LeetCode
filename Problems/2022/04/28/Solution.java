class Path implements Comparable<Path> {

  public int x;
  public int y;
  public int effort;

  public Path(int x, int y, int effort) {
    this.x = x;
    this.y = y;
    this.effort = effort;
  }

  public int compareTo(Path p) {
    return Integer.compare(this.effort, p.effort);
  }

}

class Solution {
  public int minimumEffortPath(int[][] heights) {
    int rows = heights.length;
    int cols = heights[0].length;

    Set<Integer> visited = new HashSet<>();
    Queue<Path> q = new PriorityQueue<>();
    q.add(new Path(0, 0, 0));
    while (true) {
      Path cur = q.poll();
      int x = cur.x;
      int y = cur.y;

      if (x == rows-1 && y == cols-1) {
        return cur.effort;
      }

      visited.add(hash(x, y));

      if (x > 0 && !visited.contains(hash(x-1, y))) {
        q.add(new Path(x-1, y, Math.max(cur.effort, Math.abs(heights[x][y] - heights[x-1][y]))));
      }
      if (y > 0 && !visited.contains(hash(x, y-1))) {
        q.add(new Path(x, y-1, Math.max(cur.effort, Math.abs(heights[x][y] - heights[x][y-1]))));
      }
      if (x+1 < rows && !visited.contains(hash(x+1, y))) {
        q.add(new Path(x+1, y, Math.max(cur.effort, Math.abs(heights[x][y] - heights[x+1][y]))));
      }
      if (y+1 < cols && !visited.contains(hash(x, y+1))) {
        q.add(new Path(x, y+1, Math.max(cur.effort, Math.abs(heights[x][y] - heights[x][y+1]))));
      }
    }
  }

  private int hash(int x, int y) {
    return 100 * x + y;
  }
}
