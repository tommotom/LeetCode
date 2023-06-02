class Solution {

    private final Map<Integer, List<Integer>> canDenote = new HashMap<>();

    public int maximumDetonation(int[][] bombs) {
        for (int i = 0; i < bombs.length; i++) {
            canDenote.put(i, new ArrayList());
            for (int j = 0; j < bombs.length; j++) {
                if (i == j) {continue;}
                if (isIncludes(i, j, bombs)) {
                    canDenote.get(i).add(j);
                }
            }
        }

        int[] counts = new int[bombs.length];
        for (int i = 0; i < bombs.length; i++) {
            counts[i] = dfs(i, new HashSet<>());
        }

        System.out.println(Arrays.toString(counts));

        return Arrays.stream(counts).max().getAsInt();
    }

    private boolean isIncludes(int i, int j, int[][] bombs) {
        return Math.pow(bombs[i][0] - bombs[j][0], 2) + Math.pow(bombs[i][1] - bombs[j][1], 2) <= Math.pow(bombs[i][2], 2);
    }

    private int dfs(int i, Set<Integer> denoted) {
        int ret = 1;
        denoted.add(i);
        for (int j : canDenote.get(i)) {
            if (denoted.contains(j)) {continue;}
            ret += dfs(j, denoted);
        }
        return ret;
    }
}
