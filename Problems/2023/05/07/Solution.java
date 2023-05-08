class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int[] ans = new int[obstacles.length];
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < obstacles.length; i++) {
            int o = obstacles[i];
            int l = 0, r = arr.size();
            while (l < r) {
                int m = l + (r - l) / 2;
                if (arr.get(m) <= o) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            if (l == arr.size()) {
                arr.add(o);
            } else {
                arr.set(l, o);
            }
            ans[i] = l + 1;
        }
        return ans;
    }
}
