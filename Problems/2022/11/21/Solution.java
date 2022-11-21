class Solution {

    private int m;
    private int n;

    public int nearestExit(char[][] maze, int[] entrance) {
        m = maze.length;
        n = maze[0].length;
        int[][] dir = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};

        Deque<int[]> q = new ArrayDeque<>();
        q.add(entrance);

        Set<Integer> visited = new HashSet<>();
        int step = 0;
        while (q.size() > 0) {
            Deque<int[]> newQ = new ArrayDeque<>();
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cur = q.poll();
                visited.add(hash(cur));
                for (int[] d : dir) {
                    int[] next = new int[] {cur[0]+d[0], cur[1]+d[1]};
                    if (isOut(next)) {
                        if (cur != entrance) {
                            return step;
                        }
                    } else if (maze[next[0]][next[1]] == '+') {
                        continue;
                    } else if (!visited.contains(hash(next))) {
                        visited.add(hash(next));
                        newQ.add(next);
                    }
                }
            }
            q = newQ;
            step++;
        }
        return -1;
    }

    private boolean isOut(int[] next) {
        return next[0] < 0 || next[0] == m || next[1] < 0 || next[1] == n;
    }

    private int hash(int[] pos) {
        return 100 * pos[0] + pos[1];
    }
}
