function minimumSteps(s: string): number {
    const n = s.length;
    const arr = s.split('');

    let i = 0;
    while (i < n && arr[i] === '0') {
        i++;
    }

    let j = n-1;
    while (j >= 0 && arr[j] === '1') {
        j--;
    }

    let ans = 0;
    while (i < j && arr[i] === '1' && arr[j] === '0') {
        ans += j - i;
        arr[i] = '0';
        arr[j] = '1';
        while (i < n && arr[i] === '0') {
            i++;
        }
        while (j >= 0 && arr[j] === '1') {
            j--;
        }
    }
    return ans;
};
