class Solution {
    public int[] findOriginalArray(int[] changed) {
        int n = changed.length;
        if (n % 2 == 1) {return new int[]{};}

        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : changed) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        int[] ans = new int[n/2];
        int i = 0;
        for (int key : counter.keySet().stream().sorted().toList()) {
            if (counter.get(key) == 0) {continue;}
            if (!counter.containsKey(key*2)) {return new int[]{};}
            if (counter.get(key*2) < counter.get(key)) {return new int[]{};}
            counter.put(key*2, counter.get(key*2)-counter.get(key));
            for (int j = 0; j < counter.get(key); j++) {
                ans[i] = key;
                i++;
            }
        }
        return ans;
    }
}
