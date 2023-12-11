function findSpecialInteger(arr: number[]): number {
    let i = 0;
    while (i < arr.length) {
        let j = i + 1;
        while (j < arr.length && arr[i] === arr[j]) {
            j++;
        }
        if (j - i > arr.length / 4) {
            return arr[i];
        }
        i = j;
    }
};
