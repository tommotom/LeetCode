function passThePillow(n: number, time: number): number {
    let i = 0, d = 1;
    for (let _ = 0; _ < time; _++) {
        i += d;
        if (i === 0 || i === n - 1) {
            d *= -1;
        }
    }
    return i+1;
};
