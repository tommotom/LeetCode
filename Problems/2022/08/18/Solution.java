import java.util.Collections;

class Solution {
    public int minSetSize(int[] arr) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : arr) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        List<Integer> counts = new ArrayList<>();
        for (int key : counter.keySet()) {
            counts.add(counter.get(key));
        }
        Collections.sort(counts, Collections.reverseOrder());

        int target = (arr.length + 1) / 2;
        int removed = 0;
        int i = 0;
        while (removed < target) {
            removed += counts.get(i);
            i++;
        }
        return i;
    }
}
