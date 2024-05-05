function compareVersion(version1: string, version2: string): number {
    const arr1 = version1.split('.'), arr2 = version2.split('.');
    let i1 = 0, i2 = 0;
    while (i1 < arr1.length && i2 < arr2.length) {
        const num1 = Number(arr1[i1++]), num2 = Number(arr2[i2++]);
        if (num1 < num2) {
            return -1;
        } else if (num1 > num2) {
            return 1;
        }
    }
    while (i1 < arr1.length) {
        if (Number(arr1[i1++]) > 0) {
            return 1;
        }
    }
    while (i2 < arr2.length) {
        if (Number(arr2[i2++]) > 0) {
            return -1;
        }
    }
    return 0;
};
