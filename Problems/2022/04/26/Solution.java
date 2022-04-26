class UF {

  private int[] ids;

  public UF(int n) {
    ids = new int[n];
    for (int i = 0; i < n; i++) {
      ids[i] = i;
    }
  }

  public int find(int u) {
    while (u != ids[u]) {
      int tmp = u;
      u = ids[u];
      ids[tmp] = u;
    }
    return u;
  }

  public void union(int u, int v) {
    u = find(u);
    v = find(v);
    ids[v] = u;
  }

  public boolean isConnected(int u, int v) {
    return find(u) == find(v);
  }

  public boolean isAllConnected() {
    int u = find(ids[0]);
    for (int i = 1; i < ids.length; i++) {
      if (find(ids[i]) != u) {
        return false;
      }
    }
    return true;
  }
}

class Point {
  public int x;
  public int y;
  public int i;

  public Point(int x, int y, int i) {
    this.x = x;
    this.y = y;
    this.i = i;
  }
}

class Points implements Comparable<Points> {
  public Point a;
  public Point b;

  public Points(Point a, Point b) {
    this.a = a;
    this.b = b;
  }

  public int distance() {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
  }

  public int compareTo(Points p) {
    if (this.distance() < p.distance()) {
      return -1;
    }
    if (this.distance() > p.distance()) {
      return 1;
    }
    return 0;
  }
}

class Solution {

  public int minCostConnectPoints(int[][] points) {
    int n = points.length;
    PriorityQueue<Points> q = new PriorityQueue<>();
    for (int i = 0; i < n-1; i++) {
      Point a = new Point(points[i][0], points[i][1], i);
      for (int j = 0; j < n; j++) {
        Point b = new Point(points[j][0], points[j][1], j);
        Points p = new Points(a, b);
        q.add(p);
      }
    }

    UF uf = new UF(n);
    int cost = 0;
    while (!uf.isAllConnected()) {
      Points p = q.poll();
      if (uf.isConnected(p.a.i, p.b.i)) {
        continue;
      }
      cost += p.distance();
      uf.union(p.a.i, p.b.i);
    }
    return cost;
  }
}
