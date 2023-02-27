/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;


    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

class Solution {

    int[][] grid;

    public Node construct(int[][] grid) {
        this.grid = grid;
        return helper(0, 0, grid.length);
    }

    private Node helper(int row, int col, int len) {
        boolean isLeaf = true;
        int val = grid[row][col];
        for (int i = row; i < row+len; i++) {
            for (int j = col; j < col+len; j++) {
                if (grid[i][j] != val) {
                    isLeaf = false;
                    break;
                }
            }
            if (!isLeaf) {
                break;
            }
        }

        if (isLeaf) {
            return new Node(val == 1, true);
        } else {
            int l = len / 2;
            Node topLeft = helper(row, col, l);
            Node topRight = helper(row, col+l, l);
            Node bottomLeft = helper(row+l, col, l);
            Node bottomRight = helper(row+l, col+l, l);
            return new Node(grid[row][col] == 1, false, topLeft, topRight, bottomLeft, bottomRight);
        }
    }
}
