class Solution {

    Map<Integer, Integer> f = new HashMap<>();
    int island = 0;

    public int removeStones(int[][] stones) {
        for (int[] stone : stones) {
            union(stone[0], ~stone[1]);
        }
        return stones.length - island;
    }

    private int find(int x) {
        if (f.putIfAbsent(x, x) == null) {
            island++;
        }
        if (x != f.get(x)) {
            f.put(x, find(f.get(x)));
        }
        return f.get(x);
    }

    private void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            f.put(x, y);
            island--;
        }
    }
}
