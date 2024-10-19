function findKthBit(n: number, k: number): string {
    const gen = n => {
        if (n === 1) {
            return ["0"];
        }
        const arr = gen(n-1);
        const len = arr.length;
        arr.push("1");
        for (let i = len-1; i >= 0; i--) {
            arr.push(arr[i] === "0" ? "1" : "0");
        }
        return arr;
    }
    return gen(n)[k-1];
};
