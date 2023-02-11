class State {
    int pos;
    int d;
    boolean usedRed;

    State(int pos, int d, boolean usedRed) {
        this.pos = pos;
        this.d = d;
        this.usedRed = usedRed;
    }
}

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        Map<Integer, LinkedList<Integer>> redG = new HashMap<>();
        for (int[] edge : redEdges) {
            int u = edge[0], v = edge[1];
            redG.putIfAbsent(u, new LinkedList<>());
            redG.get(u).add(v);
        }
        Map<Integer, LinkedList<Integer>> blueG = new HashMap<>();
        for (int[] edge : blueEdges) {
            int u = edge[0], v = edge[1];
            blueG.putIfAbsent(u, new LinkedList<>());
            blueG.get(u).add(v);
        }

        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        LinkedList<State> q = new LinkedList<>();
        q.add(new State(0, 0, true));
        q.add(new State(0, 0, false));

        while (q.size() > 0) {
            State cur = q.poll();
            if (ans[cur.pos] == -1) {
                ans[cur.pos] = cur.d;
            }
            if (cur.usedRed) {
                while (blueG.getOrDefault(cur.pos, new LinkedList<>()).size() > 0) {
                    int next = blueG.get(cur.pos).poll();
                    q.add(new State(next, cur.d+1, false));
                }
            } else {
                while (redG.getOrDefault(cur.pos, new LinkedList<>()).size() > 0) {
                    int next = redG.get(cur.pos).poll();
                    q.add(new State(next, cur.d+1, true));
                }
            }
        }

        return ans;
    }
}
