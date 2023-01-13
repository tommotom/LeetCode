class Solution {

    private final Map<Integer, List<Integer>> children = new HashMap<>();
    private String s;
    private int ans = 1;

    public int longestPath(int[] parent, String s) {
        for (int i = 0; i < parent.length; i++) {
            children.putIfAbsent(parent[i], new ArrayList<>());
            children.get(parent[i]).add(i);
        }
        this.s = s;

        helper(0);

        return ans;
    }

    private int helper(int cur) {
        if (!children.containsKey(cur)) {
            return 1;
        }
        int MAX = 1;
        for (int child : children.get(cur)) {
            int len = helper(child) + 1;
            if (s.charAt(cur) == s.charAt(child)) {
                continue;
            }
            ans = Math.max(ans, MAX + len - 1);
            MAX = Math.max(MAX, len);
        }
        return MAX;
    }
}
