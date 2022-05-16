class Solution {
  public int shortestPathBinaryMatrix(int[][] grid) {
    int row = grid.length, col = grid[0].length;

    if (grid[0][0] == 1 || grid[row-1][col-1] == 1) {
      return -1;
    }

    int[][] dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    Queue<int[]> q = new ArrayDeque<>();
    q.add(new int[] {0, 0});
    int ans = 0;
    while (!q.isEmpty()) {
      ans++;
      int size = q.size();

      for (int k = 0; k < size; k++) {
        int[] cur = q.poll();
        if (cur[0] == row - 1 && cur[1] == col - 1) {
          return ans;
        }
        for (int l = 0; l < 8; l++) {
          int nextRow = cur[0] + dirs[l][0];
          int nextCol = cur[1] + dirs[l][1];

          if (nextRow < 0 || nextCol < 0 || nextRow >= row || nextCol >= col || grid[nextRow][nextCol] == 1) {
            continue;
          }

          grid[nextRow][nextCol] = 1;
          q.add(new int[] {nextRow, nextCol});
        }
      }
    }
    return -1;
  }
}
