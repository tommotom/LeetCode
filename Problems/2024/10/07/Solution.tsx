function minLength(s: string): number {
    const arr = s.split('');
    let removed = true;
    while (removed) {
        removed = false;
        let i = 0;
        while (i + 1 < arr.length) {
            if ((arr[i] === 'A' && arr[i+1] === 'B') || (arr[i] === 'C' && arr[i+1] === 'D')) {
                arr.splice(i, 1);
                arr.splice(i, 1);
                removed = true;
            } else {
                i++;
            }
        }
    }
    return arr.length;
};
