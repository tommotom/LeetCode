class Solution {
    public boolean checkStraightLine(int[][] A) {
        for (int i = 1; i < A.length; i++) {
            if ((A[0][1] - A[i][1]) * (A[0][0] - A[1][0]) != (A[0][1] - A[1][1]) * (A[0][0] - A[i][0])) {
                return false;
            }
        }
        return true;
    }
}
