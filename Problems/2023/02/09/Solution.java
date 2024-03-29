class Solution {
    public long distinctNames(String[] ideas) {
        Set<String>[] sets = new Set[26];
        for (int i = 0; i < 26; i++) {
            sets[i] = new HashSet<>();
        }
        for (String idea : ideas) {
            sets[idea.charAt(0)-'a'].add(idea.substring(1));
        }

        int[][] same = new int[26][26];
        for (int i = 0; i < 25; i++) {
            for (String saffix : sets[i]) {
                for (int j = i+1; j < 26; j++) {
                    if (sets[j].contains(saffix)) {
                        same[i][j]++;
                    }
                }
            }
        }

        long res = 0;
        for (int i = 0; i < 25; i++) {
            for (int j = i+1; j < 26; j++) {
                res += (sets[i].size() - same[i][j]) * (sets[j].size() - same[i][j]) * 2;
            }
        }

        return res;
    }
}
