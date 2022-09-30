class Building implements Comparable<Building> {
    int l;
    int r;
    int h;

    public Building(int l, int r, int h) {
        this.l = l;
        this.r = r;
        this.h = h;
    }

    @Override
    public int compareTo(Building another) {
        if (this.h == another.h) {
            return Integer.compare(this.r, another.r);
        }
        return Integer.compare(another.h, this.h);
    }
}

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        PriorityQueue<Building> q = new PriorityQueue<>();
        LinkedList<List<Integer>> ans = new LinkedList<>();
        int i = 0, j = buildings[0][0];
        while (i < buildings.length || q.size() > 0) {
            if (i < buildings.length && q.size() > 0) {
                j = Math.min(buildings[i][0], q.peek().r);
            } else if (i < buildings.length) {
                j = buildings[i][0];
            } else {
                j = q.peek().r;
            }

            while (i < buildings.length && buildings[i][0] <= j) {
                q.add(new Building(buildings[i][0], buildings[i][1], buildings[i][2]));
                i++;
            }

            while (q.size() > 0 && q.peek().r <= j) {
                q.poll();
            }

            if (ans.size() > 0 && q.size() > 0 && ans.getLast().get(1) == q.peek().h) {
                continue;
            }
            ans.add(Arrays.asList(j, q.isEmpty() ? 0 : q.peek().h));
        }
        return ans;
    }
}
