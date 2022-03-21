class Solution {
  public List<Integer> partitionLabels(String s) {
    Map<String, Integer> counter1 = new HashMap<>();
    for (String ch: s.split("")) {
      counter1.put(ch, counter1.getOrDefault(ch, 0) + 1);
    }

    List<Integer> ans = new ArrayList<>();
    Map<String, Integer> counter2 = new HashMap<>();
    for (String ch: s.split("")) {
      counter1.put(ch, counter1.get(ch)-1);
      counter2.put(ch, counter2.getOrDefault(ch, 0) + 1);
      if (isValidPartition(counter1, counter2)) {
        ans.add(counter2.values().stream().mapToInt(Integer::intValue).sum());
        counter2 = new HashMap<>();
      }
    }
    if (counter2.size() > 0) {
      ans.add(counter2.values().stream().mapToInt(Integer::intValue).sum());
    }
    return ans;
  }

  private boolean isValidPartition(Map<String, Integer> c1, Map<String, Integer> c2) {
    for (String key: c2.keySet()) {
      if (c1.getOrDefault(key, 0) > 0) {
        return false;
      }
    }
    return true;
  }
}
