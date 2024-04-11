function removeKdigits(num: string, k: number): string {
    const arr = [];
    for (const c of num.split('')) {
        while (k > 0 && arr[arr.length-1] > c) {
            arr.pop();
            k--;
        }
        arr.push(c);
    }
    while (arr.length > 0 && k > 0) {
        arr.pop();
        k--;
    }
    while (arr.length > 0 && arr[0] === '0') {
        arr.shift();
    }
    return arr.length > 0 ? arr.join('') : '0';
};
