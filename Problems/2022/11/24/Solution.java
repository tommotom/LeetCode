class Solution {

    private char[][] board;
    private int m;
    private int n;
    private String word;
    private int[][] dirs = new int[][] {{1,0},{-1,0},{0,1},{0,-1}};

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.m = board.length;
        this.n = board[0].length;
        this.word = word;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (helper(0, i, j, new HashSet<>())) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean helper(int index, int r, int c, Set<Integer> visited) {
        if (index == word.length()) {
            return true;
        }
        if (r < 0 || r == m || c < 0 || c == n) {
            return false;
        }
        if (board[r][c] != word.charAt(index)) {
            return false;
        }
        int key = r * 10 + c;
        if (visited.contains(key)) {
            return false;
        }
        visited.add(key);
        for (int[] dir : dirs) {
            if (helper(index+1, r+dir[0], c+dir[1], visited)) {
                return true;
            }
        }
        visited.remove(key);
        return false;
    }
}
