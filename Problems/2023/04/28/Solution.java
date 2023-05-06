class UF {

    final int[] ids;

    UF(int n) {
        ids = new int[n];
        for (int i = 0; i < n; i++) {
            ids[i] = i;
        }
    }

    int find(int i) {
        if (i != ids[i]) {
            ids[i] = find(ids[i]);
        }
        return ids[i];
    }

    void union(int u, int v) {
        ids[find(u)] = ids[find(v)];
    }
}


class Solution {
    public int numSimilarGroups(String[] strs) {
        final UF uf = new UF(strs.length);
        for (int i = 0; i < strs.length-1; i++) {
            for (int j = i + 1; j < strs.length; j++) {
                if (isSimilar(strs[i], strs[j])) {
                    uf.union(i, j);
                }
            }
        }
        final Set<Integer> groups = new HashSet<>();
        for (int g : uf.ids) {
            groups.add(uf.find(g));
        }
        return groups.size();
    }

    private boolean isSimilar(String a, String b) {
        if (a.equals(b)) {
            return true;
        }
        int[] counter = new int[26];
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                counter[a.charAt(i)-'a']++;
                counter[b.charAt(i)-'a']--;
                diff++;
            }
        }
        if (diff != 2) {
            return false;
        }
        for (int i = 0; i < 26; i++) {
            if (counter[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
