function bestClosingTime(customers: string): number {
    const Ys = (customers.match('/Y') || []).length;
    let penalty = Ys, cur = Ys, ans = 0;
    for (let i = 0; i < customers.length; i++) {
        if (customers.charAt(i) == 'Y') {
            cur--;
        } else {
            cur++;
        }
        if (cur < penalty) {
            penalty = cur;
            ans = i+1;
        }
    }
    return ans;
};
