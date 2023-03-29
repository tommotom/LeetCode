class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        int ans = 0;
        List<Integer> nums = Arrays.stream(satisfaction)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());

        List<Integer> keep = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            keep.add(nums.get(i));
            int tmp = 0;
            for (int j = 0; j < keep.size(); j++) {
                tmp += keep.get(j) * (keep.size() - j);
            }
            if (tmp < ans) {
                return ans;
            }
            ans = tmp;
        }

        return ans;
    }
}
