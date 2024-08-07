function numberToWords(num: number): string {
    const nums = new Map([[1, 'One'], [2, 'Two'], [3, 'Three'], [4, 'Four'], [5, 'Five'], [6, 'Six'], [7, 'Seven'], [8, 'Eight'], [9, 'Nine'], [10, 'Ten'], [11, 'Eleven'], [12, 'Twelve'], [13, 'Thirteen'], [14, 'Fourteen'], [15, 'Fifteen'], [16, 'Sixteen'], [17, 'Seventeen'], [18, 'Eighteen'], [19, 'Nineteen'], [20, 'Twenty'], [30, 'Thirty'], [40, 'Forty'], [50, 'Fifty'], [60, 'Sixty'], [70, 'Seventy'], [80, 'Eighty'], [90, 'Ninety']]);

    if (num === 0) {
        return 'Zero';
    }

    const twodigit = n => {
        const arr = [];
        if (n > 20) {
            const tmp = Math.floor((n / 10)) * 10;
            arr.push(nums.get(tmp));
            n -= tmp
        }
        if (n > 0) {
            arr.push(nums.get(n));
        }
        return arr.join(' ');
    }

    const convert = n => {
        const arr = [];
        if (n >= 100) {
            arr.push(twodigit(Math.floor(n / 100)));
            arr.push('Hundred');
            n %= 100;
        }
        if (n > 0) {
            arr.push(twodigit(n));
        }
        return arr.join(' ');
    }

    const arr = [];
    const digits = new Map([[0, ""], [1, " Thousand"], [2, " Million"], [3, " Billion"]]);
    let d = 0;
    while (num > 0) {
        if (num % 1000 > 0) {
            arr.unshift(convert(num % 1000) + digits.get(d));
        }
        num = Math.floor(num / 1000);
        d++;
    }

    return arr.join(' ');
};
