class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Set<Integer> players = new HashSet<>();
        Map<Integer, Integer> loses = new HashMap<>();
        for (int[] match : matches) {
            players.add(match[0]);
            players.add(match[1]);
            loses.put(match[1], loses.getOrDefault(match[1], 0) + 1);
        }
        List<Integer>[] ans = new List[2];
        ans[0] = new ArrayList<>();
        ans[1] = new ArrayList<>();
        for (int player : players) {
            if (!loses.containsKey(player)) {
                ans[0].add(player);
            } else if (loses.get(player) == 1) {
                ans[1].add(player);
            }
        }
        Collections.sort(ans[0]);
        Collections.sort(ans[1]);
        return Arrays.asList(ans);
    }
}
