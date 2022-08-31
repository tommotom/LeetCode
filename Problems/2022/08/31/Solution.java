class Solution {
    private int m;
    private int n;
    private int[][] dirs = new int[][]{{1,0}, {-1,0}, {0,1}, {0,-1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m = heights.length;
        n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        pacificDFS(heights, pacific, 0, 0);
        atlanticDFS(heights, atlantic, m-1, n-1);

        List<List<Integer>> ans = new ArrayList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    ans.add(List.of(new Integer[]{r, c}));
                }
            }
        }
        return ans;
    }

    private void pacificDFS(int[][] heights, boolean[][] isReachable, int r, int c) {
        if (r >= m || c >= n) {return;}
        if (r == 0 || c == 0) {
            isReachable[r][c] = true;
            pacificDFS(heights, isReachable, r+1, c);
            pacificDFS(heights, isReachable, r, c+1);
        }
        if (!isReachable[r][c]) {return;}
        for (int[] dir : dirs) {
            int nextR = r + dir[0], nextC = c + dir[1];
            if (nextR < 0 || nextR >= m || nextC < 0 || nextC >= n) {continue;}
            if (!isReachable[nextR][nextC] && heights[r][c] <= heights[nextR][nextC]) {
                isReachable[nextR][nextC] = true;
                pacificDFS(heights, isReachable, nextR, nextC);
            }
        }
    }

    private void atlanticDFS(int[][] heights, boolean[][] isReachable, int r, int c) {
        if (r < 0 || c < 0) {return;}
        if (r == m-1 || c == n-1) {
            isReachable[r][c] = true;
            atlanticDFS(heights, isReachable, r-1, c);
            atlanticDFS(heights, isReachable, r, c-1);
        }
        if (!isReachable[r][c]) {return;}
        for (int[] dir : dirs) {
            int nextR = r + dir[0], nextC = c + dir[1];
            if (nextR < 0 || nextR >= m || nextC < 0 || nextC >= n) {continue;}
            if (!isReachable[nextR][nextC] && heights[r][c] <= heights[nextR][nextC]) {
                isReachable[nextR][nextC] = true;
                atlanticDFS(heights, isReachable, nextR, nextC);
            }
        }
    }
}
