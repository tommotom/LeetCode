function buyChoco(prices: number[], money: number): number {
    prices.sort((a, b) => a - b);
    return money >= prices[0] + prices[1] ? money - prices[0] - prices[1] : money;
};
