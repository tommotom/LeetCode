class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : t.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        int l = -1;
        int r = s.length();
        Map<Character, LinkedList<Integer>> seenAt = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!count.containsKey(c)) {continue;}

            if (!seenAt.containsKey(c)) {
                seenAt.put(c, new LinkedList<>());
            }
            seenAt.get(c).addLast(i);
            if (seenAt.get(c).size() > count.get(c)) {
                seenAt.get(c).pollFirst();
            }

            if (seenAt.size() < count.size()) {continue;}

            boolean isValid = true;
            int left = i;
            for (char key : seenAt.keySet()) {
                left = Math.min(left, seenAt.get(key).getFirst());
                if (seenAt.get(key).size() < count.get(key)) {
                    isValid = false;
                }
            }

            if (isValid && r-l > i+1 - left) {
                l = left;
                r = i+1;
            }
        }

        if (l == -1) {
            return "";
        }
        return s.substring(l, r);
    }
}
