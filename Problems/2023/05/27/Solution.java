class Solution {

    private int[] stoneValue;
    private final Map<Integer, Integer> memo = new HashMap<>();

    public String stoneGameIII(int[] stoneValue) {
        this.stoneValue = stoneValue;
        int result = helper(0);
        if (result > 0) {
            return "Alice";
        } else if (result < 0) {
            return "Bob";
        }
        return "Tie";
    }

    private int helper(int i) {
        if (i >= stoneValue.length) {
            return 0;
        }
        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        int taken = 0, ret = Integer.MIN_VALUE;
        for (int j = 0; j < 3; j++) {
            if (i+j == stoneValue.length) {
                break;
            }
            taken += stoneValue[i+j];
            ret = Math.max(ret, taken - helper(i+j+1));
        }

        memo.put(i, ret);
        return ret;
    }
}
