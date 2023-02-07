class Solution {
    public int totalFruit(int[] fruits) {
        int l = 0, r = 0, ans = 0;
        Map<Integer, Integer> count = new HashMap<>();
        while (l < fruits.length) {
            count.put(fruits[l], count.getOrDefault(fruits[l], 0) + 1);
            while (count.size() > 2) {
                count.put(fruits[r], count.get(fruits[r]) - 1);
                if (count.get(fruits[r]) == 0) {
                    count.remove(fruits[r]);
                }
                r++;
            }
            l++;
            ans = Math.max(ans, l - r);
        }
        return ans;
    }
}
