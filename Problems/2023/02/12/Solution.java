class Solution {
    public long minimumFuelCost(int[][] roads, int seats) {
        int n = roads.length + 1;
        int[] edges = new int[n];
        long[] people = new long[n];
        Arrays.fill(people, 1);
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] road : roads) {
            int u = road[0], v = road[1];
            graph.putIfAbsent(u, new ArrayList<>());
            graph.putIfAbsent(v, new ArrayList<>());
            graph.get(u).add(v);
            graph.get(v).add(u);
            edges[u]++;
            edges[v]++;
        }

        LinkedList<Integer> leaves = new LinkedList<>();
        for (int i = 1; i < n; i++) {
            if (edges[i] == 1) {
                leaves.add(i);
            }
        }

        long fuel = 0;
        while (leaves.size() > 0) {
            int leaf = leaves.poll();
            for (int next : graph.get(leaf)) {
                if (edges[next] == 0) {
                    continue;
                }
                people[next] += people[leaf];
                fuel += (people[leaf]+seats-1) / seats;
                edges[next]--;
                if (next > 0 && edges[next] == 1) {
                    leaves.add(next);
                }
            }
            edges[leaf] = 0;
        }

        return fuel;
    }
}
