class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        for (int i = 0; i < m; i++) {
            sort(mat, i, 0);
        }
        for (int j = 0; j < n; j++) {
            sort(mat, 0, j);
        }
        return mat;
    }

    private void sort(int[][] mat, int row, int col) {
        int m = mat.length, n = mat[0].length;
        List<Integer> arr = new ArrayList<>();

        int i = row, j = col;
        while (i < m && j < n) {
            arr.add(mat[i][j]);
            i++; j++;
        }
        Collections.sort(arr);

        int k = 0;
        i = row; j = col;
        while (i < m && j < n) {
            mat[i][j] = arr.get(k);
            i++; j++; k++;
        }
    }
}
