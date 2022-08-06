class Solution {

    HashMap<Integer, Integer>[] memo;

    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int test = minutesToTest / minutesToDie;
        memo = new HashMap[test+1];
        int pig = 0;
        while (true) {
            if (canCheck(pig, test) >= buckets) {
                return pig;
            }
            pig++;
        }
    }

    private int canCheck(int pig, int test) {
        if (pig == 0) {return 1;}
        if (test == 1) {return (int) Math.pow(2, pig);}
        if (memo[test] != null && memo[test].containsKey(pig)) {return memo[test].get(pig);}
        int ret = 0;
        int dead = 0;
        while (dead <= pig) {
            ret += canCheck(pig-dead, test-1) * (factorial(pig) / factorial(dead) / factorial(pig-dead));
            dead++;
        }
        if (memo[test] == null) {
            memo[test] = new HashMap<>();
        }
        memo[test].put(pig, ret);
        return ret;
    }

    private int factorial(int n) {
        if (n == 0) {return 1;}
        return n * factorial(n-1);
    }
}
