import java.awt.Point;

class Util {
    public static int ccw(Point a, Point b, Point c) {
        double area = (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
        if      (area < 0) return -1;
        else if (area > 0) return +1;
        else               return  0;
    }
}

class PolarOrder implements Comparator<Point>{

    private final Point p;

    public PolarOrder(Point p) {
        this.p = p;
    }

    @Override
    public int compare(Point a, Point b) {
        int ret = Util.ccw(p, a, b);
        return ret == 0 ? dist(a) - dist(b) : ret;
    }

    private int dist(Point a) {
        int dx = p.x - a.x;
        int dy = p.y - a.y;
        return dx*dx + dy*dy;
    }
}

class Solution {
    public int[][] outerTrees(int[][] trees) {
        if(trees.length <= 3) {
            return trees;
        }

        Point[] points = Arrays.stream(trees).map(x -> new Point(x[0], x[1])).toArray(Point[]::new);

        Arrays.sort(points, (a, b) -> Integer.compare(a.y, b.y));
        Point p = points[0];
        Arrays.sort(points, 1, points.length, new PolarOrder(p));

        int i = points.length - 1;
        while (i >= 0 && Util.ccw(p, points[points.length - 1], points[i]) == 0) {
            i--;
        }
        for (int l = i + 1, h = points.length - 1; l < h; l++, h--) {
            Point temp = points[l];
            points[l] = points[h];
            points[h] = temp;
        }

        Stack<Point> hull = new Stack<>();
        hull.push(points[0]); hull.push(points[1]);
        for (int j = 2; j < points.length; j++) {
            Point top = hull.pop();
            while (!hull.isEmpty() && Util.ccw(hull.peek(), top, points[j]) > 0) {
                top = hull.pop();
            }
            hull.push(top);
            hull.push(points[j]);
        }

        int n = hull.size();
        int[][] ret = new int[n][2];
        for (int j = 0; j < n; j++) {
            Point t = hull.pop();
            ret[j][0] = t.x;
            ret[j][1] = t.y;
        }

        return ret;
    }
}
