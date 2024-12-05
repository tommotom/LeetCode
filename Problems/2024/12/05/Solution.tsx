function canChange(start: string, target: string): boolean {
    const compress = str => {
        const arr = [];
        for (let i = 0; i < str.length; i++) {
            if (str.charAt(i) === '_') {
                continue;
            }
            arr.push([str.charAt(i), i]);
        }
        return arr;
    }

    const startArr = compress(start), targetArr = compress(target);

    if (startArr.length !== targetArr.length) {
        return false;
    }

    for (let i = 0; i < startArr.length; i++) {
        if (startArr[i][0] !== targetArr[i][0]) {
            return false;
        }
        if (startArr[i][0] === 'L') {
            if (startArr[i][1] < targetArr[i][1]) {
                return false;
            }
        } else {
            if (startArr[i][1] > targetArr[i][1]) {
                return false;
            }
        }
    }

    return true
};
