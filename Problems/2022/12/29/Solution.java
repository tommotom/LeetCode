class Task implements Comparable<Task> {

    final int i;
    final int enqueueTime;
    final int processingTime;

    Task(int[] task, int i) {
        this.i = i;
        this.enqueueTime = task[0];
        this.processingTime = task[1];
    }

    @Override
    public int compareTo(Task a) {
        if (this.processingTime == a.processingTime) {
            return Integer.compare(this.i, a.i);
        }
        return Integer.compare(this.processingTime, a.processingTime);
    }
}

class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        Task[] t = new Task[n];
        for (int i = 0; i < n; i++) {
            t[i] = new Task(tasks[i], i);
        }
        Arrays.sort(t, (p1, p2) -> p1.enqueueTime - p2.enqueueTime);

        PriorityQueue<Task> q = new PriorityQueue<>();
        int[] ans = new int[n];
        int time = 0;
        int i = 0, j = 0;
        while (j < n) {
            if (i < n && q.isEmpty() && time < t[i].enqueueTime) {
                time = t[i].enqueueTime;
            }

            while (i < n && t[i].enqueueTime <= time) {
                q.add(t[i]);
                i++;
            }

            Task process = q.poll();
            ans[j] = process.i;
            System.out.println(time);
            time += process.processingTime;
            j++;
        }

        return ans;
    }
}
