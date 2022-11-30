class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : arr){
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        Set<Integer> occurrence = new HashSet<>();
        for (int key : counter.keySet()) {
            if (!occurrence.add(counter.get(key))) {
                return false;
            }
        }
        return true;
    }
}
