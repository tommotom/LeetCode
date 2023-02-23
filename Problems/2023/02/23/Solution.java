class PJ {
    final int profit;
    final int capital;
    PJ(final int profit, final int capital) {
        this.profit = profit;
        this.capital = capital;
    }
}

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<PJ> canWork = new PriorityQueue<>((a, b) -> b.profit - a.profit);
        PriorityQueue<PJ> q = new PriorityQueue<>((a, b) -> a.capital - b.capital);
        for (int i = 0; i < profits.length; i++) {
            PJ pj = new PJ(profits[i], capital[i]);
            if (capital[i] <= w) {
                canWork.add(pj);
            } else {
                q.add(pj);
            }
        }

        for (int i = 0; i < k; i++) {
            if (canWork.size() == 0) {
                break;
            }
            PJ pj = canWork.poll();
            w += pj.profit;
            while (q.size() > 0 && q.peek().capital <= w) {
                canWork.add(q.poll());
            }
        }
        return w;
    }
}
