function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const numToI = new Map();
    for (let i = 0; i < arr2.length; i++) {
        numToI.set(arr2[i], i);
    }

    const comparator = (a, b) => {
        if (numToI.has(a) && numToI.has(b)) {
            return numToI.get(a) - numToI.get(b);
        } else if (!numToI.has(a) && numToI.has(b)) {
            return Number.MAX_SAFE_INTEGER;
        } else if (numToI.has(a) && !numToI.has(b)) {
            return Number.MIN_SAFE_INTEGER;
        } else {
            return a - b;
        }
    }

    return arr1.sort((a, b) => comparator(a, b));
};
