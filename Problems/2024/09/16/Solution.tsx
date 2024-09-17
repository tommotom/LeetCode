function findMinDifference(timePoints: string[]): number {
    const arr = timePoints.map(str => {
        const HH = Number(str.substring(0, 2));
        const MM = Number(str.substring(3, 5));
        return HH * 60 + MM;
    }).sort((a, b) => a - b);
    const diff = (a, b) => {
        return Math.min(b - a, 24 * 60 + a - b);
    }
    let ans = diff(arr[0], arr[arr.length-1]);
    for (let i = 0; i < arr.length-1; i++) {
        ans = Math.min(ans, diff(arr[i], arr[i+1]));
    }
    return ans;
};
