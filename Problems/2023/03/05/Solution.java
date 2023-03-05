class Solution {
    public int minJumps(int[] arr) {
        Map<Integer, LinkedList<Integer>> numToI = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int num = arr[i];
            numToI.putIfAbsent(num, new LinkedList<>());
            numToI.get(num).add(i);
        }

        int[] arrivedAt = new int[arr.length];
        Arrays.fill(arrivedAt, Integer.MAX_VALUE);
        arrivedAt[0] = 0;
        LinkedList<Integer> q = new LinkedList<>();
        q.add(0);
        while (true) {
            int cur = q.poll();
            if (cur == arr.length-1) {
                return arrivedAt[cur];
            }
            if (cur > 0 && arr[cur-1] != arr[cur] && arrivedAt[cur-1] == Integer.MAX_VALUE) {
                arrivedAt[cur-1] = arrivedAt[cur] + 1;
                q.add(cur-1);
            }
            if (cur+1 < arr.length && arr[cur] != arr[cur+1] && arrivedAt[cur+1] == Integer.MAX_VALUE) {
                arrivedAt[cur+1] = arrivedAt[cur] + 1;
                q.add(cur+1);
            }
            while (numToI.get(arr[cur]).size() > 0) {
                int next = numToI.get(arr[cur]).poll();
                if (cur == next) {continue;}
                if (arrivedAt[next] <= arrivedAt[cur] + 1) {continue;}
                arrivedAt[next] = arrivedAt[cur] + 1;
                q.add(next);
            }
        }
    }
}
