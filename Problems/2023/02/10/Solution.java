class Land {

    final int x;
    final int y;
    final int dist;

    Land(int x, int y, int dist) {
        this.x = x;
        this.y = y;
        this.dist = dist;
    }
}

class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        LinkedList<Land> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    visited[i][j] = true;
                    q.add(new Land(i, j, 0));
                }
            }
        }

        if (q.size() == 0 || q.size() == n * n) {
            return -1;
        }

        int ans = 0;
        int[][] dir = new int[][] {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            Land cur = q.poll();
            ans = cur.dist;
            for (int[] d : dir) {
                int x = cur.x + d[0];
                int y = cur.y + d[1];
                if (x < 0 || x == n || y < 0 || y == n || visited[x][y]) {
                    continue;
                }
                visited[x][y] = true;
                q.add(new Land(x, y, cur.dist+1));
            }
        }
        return ans;
    }
}
