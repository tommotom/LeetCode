function timeRequiredToBuy(tickets: number[], k: number): number {
    const bought = tickets.shift();
    if (bought === 1 && k === 0) {
        return 1;
    }
    if (bought > 1) {
        tickets.push(bought - 1);
    }
    k = k === 0 ? tickets.length-1 : k - 1;
    return timeRequiredToBuy(tickets, k) + 1;
};
