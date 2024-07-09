function averageWaitingTime(customers: number[][]): number {
    let time = 0, ans = 0;
    for (const [a, t] of customers) {
        if (time < a) {
            time = a;
        }
        time += t;
        ans += time - a;
    }
    return ans / customers.length;
};
