class Solution {

    private final Map<Integer, List<Integer>> children = new HashMap<>();
    private int[] informTime;

    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        this.informTime = informTime;
        for (int i = 0; i < n; i++) {
            if (manager[i] == -1) {continue;}
            if (!children.containsKey(manager[i])) {
                children.put(manager[i], new ArrayList<>());
            }
            children.get(manager[i]).add(i);
        }

        return dfs(headID);
    }

    private int dfs(int i) {
        if (!children.containsKey(i)) {
            return 0;
        }
        return informTime[i] + children.get(i).stream().map(a -> dfs(a)).max(Comparator.naturalOrder()).get();
    }
}
