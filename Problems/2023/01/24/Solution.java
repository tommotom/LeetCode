class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;

        Map<Integer, int[]> numToSquare = new HashMap<>();
        int r = n-1, c = 0, d = 1;
        for (int i = 1; i <= n * n; i++) {
            numToSquare.put(i, new int[]{r, c});
            if (c + d < 0 || c + d == n) {
                d *= -1;
                r -= 1;
            } else {
                c += d;
            }
        }

        Set<Integer> visited = new HashSet<>();
        visited.add(1);
        LinkedList<int[]> q = new LinkedList<>();
        q.add(new int[]{1, 0});
        while (q.size() > 0) {
            int[] arr = q.poll();
            if (arr[0] == n * n) {
                return arr[1];
            }
            for (int dice = 1; dice <= 6; dice++) {
                if (arr[0] + dice > n * n) {
                    break;
                }
                if (visited.contains(arr[0] + dice)) {
                    continue;
                }
                visited.add(arr[0] + dice);
                int[] next = numToSquare.get(arr[0] + dice);
                if (board[next[0]][next[1]] == -1) {
                    q.add(new int[]{arr[0] + dice, arr[1] + 1});
                } else {
                    q.add(new int[]{board[next[0]][next[1]], arr[1] + 1});
                }
            }
        }

        return -1;
    }
}
