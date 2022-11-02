class Solution {
    public int minMutation(String start, String end, String[] bank) {
        LinkedList<String> str = new LinkedList<>();
        LinkedList<Integer> mut = new LinkedList<>();
        str.add(start);
        mut.add(0);
        Set<String> visited = new HashSet<>();
        while (str.size() > 0) {
            String s = str.poll();
            int m = mut.poll();
            if (s.equals(end)) {
                return m;
            }

            visited.add(s);
            for (String b : bank) {
                if (visited.contains(b)) {
                    continue;
                }
                if (dist(s, b) == 1) {
                    str.add(b);
                    mut.add(m+1);
                }
            }
        }
        return -1;
    }

    private int dist(String a, String b) {
        int ret = 0;
        for (int i = 0; i < 8; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                ret++;
            }
        }
        return ret;
    }
}
