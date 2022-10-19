class Count implements Comparable<Count> {
    String word;
    Integer count;

    public Count(String word, int count) {
        this.word = word;
        this.count = count;
    }

    public int compareTo(Count a) {
        if (this.count == a.count) {
            return a.word.compareTo(this.word);
        }
        return Integer.compare(this.count, a.count);
    }

    public String toString() {
        return word + " " + count;
    }
}

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counter = new HashMap<>();
        for (String word : words) {
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }

        PriorityQueue<Count> q = new PriorityQueue<>();
        for (String key : counter.keySet()) {
            q.add(new Count(key, counter.get(key)));
            if (q.size() == k+1) {
                q.poll();
            }
        }

        List<String> ans = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            ans.add(q.poll().word);
        }

        Collections.reverse(ans);

        return ans;
    }
}
