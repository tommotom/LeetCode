function largestOddNumber(num: string): string {
    function isOdd(c: string): boolean {
        return c === '1' || c === '3' || c === '5' || c === '7' || c === '9';
    }
    let i = num.length-1;
    while (i >= 0) {
        if (isOdd(num.charAt(i))) {
            break;
        }
        i--;
    }
    return num.substring(0, i+1);
};
