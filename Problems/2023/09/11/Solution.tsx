function groupThePeople(groupSizes: number[]): number[][] {
    const sizeToI = new Map();
    for (let i = 0; i < groupSizes.length; i++) {
        const size = groupSizes[i];
        if (!sizeToI.has(size)) {
            sizeToI.set(size, []);
        }
        sizeToI.get(size).push(i);
    }

    const ans = []
    for (const size of sizeToI.keys()) {
        let arr = [];
        for (const i of sizeToI.get(size)) {
            arr.push(i);
            if (arr.length == size) {
                ans.push(arr);
                arr = [];
            }
        }
    }

    return ans;
};
