class Solution {
    public double average(int[] salary) {
        int min = Integer.MAX_VALUE, max = 0;
        double sum = 0;
        for (int s : salary) {
            min = Math.min(min, s);
            max = Math.max(max, s);
            sum += s;
        }
        return (sum - max - min) / (salary.length - 2);
    }
}
