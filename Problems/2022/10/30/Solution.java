class State {
    int i;
    int j;
    int k;
    int cost;

    public State(int i, int j, int k, int cost) {
        this.i = i;
        this.j = j;
        this.k = k;
        this.cost = cost;
    }

    @Override
    public int hashCode() {
        return i * 10000 + j * 100 + k;
    }
}

class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][] dirs = new int[][] {{1,0},{0,1},{-1,0},{0,-1}};


        LinkedList<State> q = new LinkedList<>();
        q.add(new State(0, 0, k, 0));

        boolean[][][] visited = new boolean[m][n][k+1];

        while (!q.isEmpty()) {
            State s = q.poll();

            if (s.i == m-1 && s.j == n-1) {
                return s.cost;
            }

            for (int[] dir : dirs) {
                int ii = s.i + dir[0];
                int jj = s.j + dir[1];
                if (ii < 0 || jj < 0 || ii == m || jj == n) {
                    continue;
                }
                if (s.k-grid[ii][jj] < 0 || visited[ii][jj][s.k-grid[ii][jj]]) {
                    continue;
                }
                visited[ii][jj][s.k-grid[ii][jj]] = true;
                q.add(new State(ii, jj, s.k-grid[ii][jj], s.cost+1));
            }
        }

        return -1;
    }
}
