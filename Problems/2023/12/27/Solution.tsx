function minCost(colors: string, neededTime: number[]): number {
    let i = 0, ans = 0;
    while (i < neededTime.length) {
        let sum = neededTime[i], max = neededTime[i], j = i+1;
        while (j < neededTime.length && colors.charAt(i) === colors.charAt(j)) {
            sum += neededTime[j];
            max = Math.max(max, neededTime[j++]);
        }
        if (sum > max) {
            ans += sum - max;
        }
        i = j;
    }
    return ans;
};
