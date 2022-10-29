class Flower implements Comparable<Flower> {

    int plant;
    int grow;

    public Flower(int plant, int grow) {
        this.plant = plant;
        this.grow = grow;
    }

    @Override
    public int compareTo(Flower a) {
        return Integer.compare(a.grow, this.grow);
    }
}

class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        PriorityQueue<Flower> q = new PriorityQueue<>();
        for (int i = 0; i < plantTime.length; i++) {
            q.add(new Flower(plantTime[i], growTime[i]));
        }

        int ans = 0;
        int t = 0;
        while (q.size() > 0) {
            Flower flower = q.poll();
            ans = Math.max(ans, t + flower.plant + flower.grow);
            t += flower.plant;
        }

        return ans;
    }
}
