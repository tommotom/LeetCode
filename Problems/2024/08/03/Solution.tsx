function canBeEqual(target: number[], arr: number[]): boolean {
    target.sort();
    arr.sort();
    return target.filter((num, i) => num !== arr[i]).length === 0;
};
