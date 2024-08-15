function lemonadeChange(bills: number[]): boolean {
    const counter = new Map();
    const changes = [10, 5];
    counter.set(5, 0);
    counter.set(10, 0);
    counter.set(20, 0);
    for (let b of bills) {
        counter.set(b, counter.get(b) + 1);
        b -= 5;
        let i = 0
        while (b > 0 && i < changes.length) {
            if (changes[i] <= b) {
                const c = Math.min(counter.get(changes[i]), Math.floor(b / changes[i]));
                b -= c * changes[i];
                counter.set(changes[i], counter.get(changes[i]) - c);
            }
            i++;
        }
        if (b > 0) {
            return false;
        }
    }
    return true;
};
