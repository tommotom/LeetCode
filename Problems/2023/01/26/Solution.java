class State implements Comparable<State>{

    final int city;
    final int price;
    final int stop;

    State(int price, int city, int stop) {
        this.price = price;
        this.city = city;
        this.stop = stop;
    }

    @Override
    public int compareTo(State a) {
        return Integer.compare(this.price, a.price);
    }
}

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
        for (int[] flight : flights) {
            int from = flight[0], to = flight[1], price = flight[2];
            graph.putIfAbsent(from, new HashMap<>());
            graph.get(from).put(to, price);
        }

        Map<Integer, State> visited = new HashMap<>();
        PriorityQueue<State> q = new PriorityQueue<>();
        q.add(new State(0, src, 0));

        while (q.size() > 0) {
            State cur = q.poll();
            if (cur.city == dst) {
                return cur.price;
            }
            if (cur.stop > k || !graph.containsKey(cur.city)) {
                continue;
            }
            if (visited.containsKey(cur.city)) {
                State last = visited.get(cur.city);
                if (last.price <= cur.price && last.stop <= cur.stop) {
                    continue;
                }
            }
            visited.putIfAbsent(cur.city, cur);

            Map<Integer, Integer> nexts = graph.get(cur.city);
            for (int to : nexts.keySet()) {
                q.add(new State(cur.price + nexts.get(to), to, cur.stop + 1));
            }
        }

        return -1;
    }
}
