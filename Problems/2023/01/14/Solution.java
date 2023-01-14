class UF {

    private final char[] ids;

    UF() {
        ids = new char[26];
        for (int i = 0; i < 26; i++) {
            ids[i] = (char)('a' + i);
        }
    }

    char find(char c) {
        int i = c - 'a';
        if (ids[i] == c) {
            return c;
        }
        return find(ids[i]);
    }

    void union(char a, char b) {
        a = find(a);
        b = find(b);

        if (a < b) {
            ids[b-'a'] = a;
        } else {
            ids[a-'a'] = b;
        }
    }
}

class Solution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        UF uf = new UF();
        for (int i = 0; i < s1.length(); i++) {
            uf.union(s1.charAt(i), s2.charAt(i));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < baseStr.length(); i++) {
            sb.append(uf.find(baseStr.charAt(i)));
        }
        return sb.toString();
    }
}
