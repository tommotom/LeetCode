class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int[] diff = new int[n];
        int prev = 0, min = Integer.MAX_VALUE, minI = 0;
        for (int i = 0; i < n; i++) {
            diff[i] = prev + gas[i] - cost[i];
            if (diff[i] < min) {
                minI = i;
                min = diff[i];
            }
            prev = diff[i];
        }

        int i = (minI + 1) % n;
        int g = gas[i];
        for (int j = 0; j < n; j++) {
            if (g < cost[i]) {return -1;}
            g -= cost[i];
            i = (i + 1) % n;
            g += gas[i];
        }

        return (minI + 1) % n;
    }
}
