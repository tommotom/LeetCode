function sortJumbled(mapping: number[], nums: number[]): number[] {

    const mapNum = num => {
        if (num === 0) {
            return mapping[0];
        }
        let ret = 0, d = 1;
        while (num > 0) {
            ret += d * (mapping[num % 10]);
            d *= 10;
            num = Math.floor(num / 10);
        }
        return ret;
    }

    return nums.map((num, i) => ({num: num, index: i})).sort((a, b) => mapNum(a.num) === mapNum(b.num) ? a.index - b.index : mapNum(a.num) - mapNum(b.num)).map(el => el.num);
};
