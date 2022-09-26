class UF {
    private int[] ids = new int[26];
    public UF() {
        for (int i = 0; i < 26; i++) {
            ids[i] = i;
        }
        return;
    }

    public int find(char c) {
        int i = c - 'a';
        while (i != ids[i]) {
            i = ids[i];
        }
        return i;
    }

    public void union(char a, char b) {
        int u = find(a);
        int v = find(b);
        ids[u] = v;
    }
}

class Solution {
    public boolean equationsPossible(String[] equations) {
        UF uf = new UF();

        for (String equation : equations) {
            if (equation.charAt(1) == '!') {
                continue;
            }
            char a = equation.charAt(0);
            char b = equation.charAt(3);
            uf.union(a, b);
        }

        for (String equation : equations) {
            if (equation.charAt(1) == '=') {
                continue;
            }
            char a = equation.charAt(0);
            char b = equation.charAt(3);
            if (uf.find(a) == uf.find(b)) {
                return false;
            }
        }
        return true;
    }
}
