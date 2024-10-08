function minSwaps(s: string): number {
    let level = 0, swapped = 0, cleared= 0;
    for (const c of s.split('')) {
        if (c === '[') {
            level++;
        } else if (level === 0){
            level++;
            swapped++;
        } else {
            level--;
        }
    }
    return swapped;
};
