class MyNode implements Comparable<MyNode> {

  public final int label;

  public final int delay;

  public MyNode(int label, int delay) {
    this.label = label;
    this.delay = delay;
  }

  @Override
  public int compareTo(MyNode other) {
    return Integer.compare(this.delay, other.delay);
  }
}

class Solution {
  public int networkDelayTime(int[][] times, int n, int k) {
    Map<Integer, List<Integer[]>> graph = new HashMap<>();
    for (int i = 0; i < times.length; i++) {
      int key = times[i][0];
      Integer[] costTo = {times[i][1], times[i][2]};
      if (graph.containsKey(key)) {
        graph.get(key).add(costTo);
      } else {
        List<Integer[]> list = new ArrayList<>();
        list.add(costTo);
        graph.put(key, list);
      }
    }

    int ans = 0;
    PriorityQueue<MyNode> q = new PriorityQueue<>();
    Set<Integer> visited = new HashSet<>();
    q.add(new MyNode(k, 0));
    while (q.size() > 0 && visited.size() < n) {
      MyNode u = q.poll();

      ans = u.delay;
      visited.add(u.label);

      if (!graph.containsKey(u.label)) {
        continue;
      }

      List<Integer[]> nextLabels = graph.get(u.label);
      for (int i = 0; i < nextLabels.size(); i++) {
        Integer[] costTo = nextLabels.get(i);
        if (visited.contains(costTo[0])) {
          continue;
        }
        q.add(new MyNode(costTo[0], costTo[1] + u.delay));
      }
    }

    return visited.size() == n ? ans : -1;
  }
}
