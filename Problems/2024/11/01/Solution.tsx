function makeFancyString(s: string): string {
    const arr = [];
    for (const c of s.split('')) {
        if (arr.length > 1 && arr[arr.length-2] === arr[arr.length-1] && arr[arr.length-1] === c) {
            continue;
        }
        arr.push(c);
    }
    return arr.join('');
};
