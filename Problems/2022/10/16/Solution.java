class Solution {

    Map<Integer, Integer>[][] memo;
    int[] jobs;
    int d;

    public int minDifficulty(int[] jobDifficulty, int d) {
        if (jobDifficulty.length < d) {return -1;}
        jobs = jobDifficulty;
        this.d = d;
        memo = new Map[jobs.length][d+1];
        return helper(0, jobs[0], 1);
    }

    private int helper(int i, int dif, int day) {
        if (day > d) {return 100000;}
        if (i == jobs.length-1) {
            if (day == d) {
                return dif;
            }
            return 100000;
        }
        if (jobs.length - i - 1 < d - day) {
            return 100000;
        }
        if (memo[i][day] == null) {
            memo[i][day] = new HashMap<>();
        } else if (memo[i][day].containsKey(dif)) {
            return memo[i][day].get(dif);
        }
        int ret = Math.min(helper(i+1, Math.max(dif, jobs[i+1]), day), helper(i+1, jobs[i+1], day+1)+dif);
        memo[i][day].put(dif, ret);
        return ret;
    }
}
