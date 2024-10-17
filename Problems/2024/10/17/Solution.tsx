function maximumSwap(num: number): number {
    const arr = num.toString().split('');
    let swapped = false;
    for (let i = 0; i < arr.length-1; i++) {
        let max = '', index = -1;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] >= max) {
                max = arr[j];
                index = j;
            }
        }
        if (arr[i] < max) {
            arr[index] = arr[i];
            arr[i] = max;
            break;
        }
    }
    return Number(arr.join(''));
};
