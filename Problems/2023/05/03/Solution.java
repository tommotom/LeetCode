class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        for (int num1 : nums1) {set1.add(num1);}
        for (int num2 : nums2) {set2.add(num2);}
        Set<Integer> ans1 = new HashSet<>(set1);
        Set<Integer> ans2 = new HashSet<>(set2);
        for (int num1 : set1) {ans2.remove(num1);}
        for (int num2 : set2) {ans1.remove(num2);}
        return List.of(new ArrayList<>(ans1), new ArrayList<>(ans2));
    }
}
