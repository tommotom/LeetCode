class Node {
    Set<Integer> made, todo;
    public Node(Set<Integer> made, Set<Integer> todo) {
        this.made = made;
        this.todo = todo;
    }
}

class Solution {
    public int[] movesToStamp(String stamp, String target) {
        int m = stamp.length(), n = target.length();
        boolean[] done = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();
        Stack<Integer> ans = new Stack<>();
        List<Node> arr = new ArrayList<>();

        for (int i = 0; i <= n-m; i++) {
            Set<Integer> made = new HashSet<>();
            Set<Integer> todo = new HashSet<>();
            for (int j = 0; j < m; j++) {
                if (stamp.charAt(j) == target.charAt(i+j)) {
                    made.add(i+j);
                } else {
                    todo.add(i+j);
                }
            }
            arr.add(new Node(made, todo));
            if (todo.isEmpty()) {
                ans.push(i);
                for (int j = i; j < i+m; j++) {
                    if (!done[j]) {
                        done[j] = true;
                        queue.add(j);
                    }
                }
            }
        }

        while (!queue.isEmpty()) {
            int i = queue.poll();

            for (int j = Math.max(0, i-m+1); j <= Math.min(n-m, i); j++) {
                if (arr.get(j).todo.contains(i)) {
                    arr.get(j).todo.remove(i);
                    if (arr.get(j).todo.isEmpty()) {
                        ans.push(j);
                        for (int k : arr.get(j).made) {
                            if (!done[k]) {
                                queue.add(k);
                                done[k] = true;
                            }
                        }
                    }
                }
            }
        }

        for (boolean d : done) {
            if (!d) {
                return new int[0];
            }
        }

        int[] ret = new int[ans.size()];
        int t = 0;
        while (!ans.isEmpty()) {
            ret[t++] = ans.pop();
        }

        return ret;
    }
}
