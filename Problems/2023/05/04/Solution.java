class Solution {
    public String predictPartyVictory(String senate) {
        char[] arr = senate.toCharArray();
        int n = senate.length();
        LinkedList<Integer> r = new LinkedList<>(), d = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if ('R' == arr[i]) {
                r.add(i);
            } else {
                d.add(i);
            }
        }
        while (!r.isEmpty() && !d.isEmpty()) {
            if (r.peek() < d.peek()) {
                d.poll();
                r.add(r.poll() + n);
            } else {
                r.poll();
                d.add(d.poll() + n);
            }
        }
        return !r.isEmpty() ? "Radiant" : "Dire";
    }
}
