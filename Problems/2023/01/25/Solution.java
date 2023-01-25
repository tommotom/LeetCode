class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        Set<Integer> visited1 = new HashSet<>();
        visited1.add(node1);
        Set<Integer> visited2 = new HashSet<>();
        visited2.add(node2);
        while (!visited1.contains(node2) && !visited2.contains(node1)) {
            if (node1 != -1) {
                node1 = edges[node1];
                if (visited1.contains(node1)) {
                    node1 = -1;
                } else {
                    visited1.add(node1);
                }
            }
            if (node2 != -1) {
                node2 = edges[node2];
                if (visited2.contains(node2)) {
                    node2 = -1;
                } else {
                    visited2.add(node2);
                }
            }
            if (node1 == -1 && node2 == -1) {
                return -1;
            }
        }

        if (visited1.contains(node2) && visited2.contains(node1)) {
            return Math.min(node1, node2);
        }
        return visited1.contains(node2)
                ? node2
                : node1;
    }
}
