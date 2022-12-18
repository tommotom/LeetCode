class Temperature implements Comparable<Temperature> {
    int temp;
    int i;

    Temperature(int temp, int i) {
        this.temp = temp;
        this.i = i;
    }

    @Override
    public int compareTo(Temperature a) {
        return Integer.compare(this.temp, a.temp);
    }
}

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int [] ans = new int[temperatures.length];
        PriorityQueue<Temperature> q = new PriorityQueue<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!q.isEmpty() && q.peek().temp < temperatures[i]) {
                int j = q.poll().i;
                ans[j] = i-j;
            }
            q.add(new Temperature(temperatures[i], i));
        }
        return ans;
    }
}
