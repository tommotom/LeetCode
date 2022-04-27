class UF {

  private int[] ids;

  public UF(int n) {
    ids = new int[n];
    for (int i = 0; i < n; i++) {
      ids[i] = i;
    }
  }

  public int find(int u) {
    if (u == ids[u]) {
      return u;
    }
    ids[u] = find(ids[u]);
    return ids[u];
  }

  public void union(int u, int v) {
    u = find(u);
    v = find(v);
    ids[v] = u;
  }

  public int[] getIds() {
    return ids;
  }
}

class Solution {
  public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
    UF uf = new UF(s.length());
    for (List<Integer> pair : pairs) {
      uf.union(pair.get(0), pair.get(1));
    }

    int[]ids = uf.getIds();
    Map<Integer, Queue<Character>> map = new HashMap<>();
    for (int i = 0; i < ids.length; i++) {
      int j = uf.find(i);
      map.putIfAbsent(j, new PriorityQueue<>());
      map.get(j).add(s.charAt(i));
    }
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < ids.length; i++) {
      int j = uf.find(i);
      sb.append(map.get(j).poll());
    }
    return sb.toString();
  }
}
