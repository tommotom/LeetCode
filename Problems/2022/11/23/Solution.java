class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9], cols = new int[9], dias = new int[9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                if ((rows[i] & (1<<(c-'1'))) > 0) return false;
                if ((cols[j] & (1<<(c-'1'))) > 0) return false;
                int index = 3 * (i / 3) + j / 3;
                if ((dias[index] & (1<<(c-'1'))) > 0) return false;
                rows[i] |= (1<<(c-'1'));
                cols[j] |= (1<<(c-'1'));
                dias[index] |= (1<<(c-'1'));
            }
        }
        return true;
    }
}
