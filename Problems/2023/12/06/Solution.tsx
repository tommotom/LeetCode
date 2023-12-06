function totalMoney(n: number): number {
    let monday = 1, ans = 0;
    while (n > 6) {
        ans += (monday + 3) * 7
        n -= 7;
        monday++;
    }
    while (n > 0) {
        ans += monday++;
        n--;
    }
    return ans;
};
