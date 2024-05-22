function partition(s: string): string[][] {
    const ans = [];

    const isPalin = arr => {
        let l = 0, r = arr.length - 1;
        while (l < r) {
            if (arr[l++] !== arr[r--]) {
                return false;
            }
        }
        return true;
    }

    const helper = (i, partition, arr) => {
        if (i === s.length) {
            if (arr.length === 0) {
                ans.push([...partition]);
            }
            return;
        }

        arr.push(s.charAt(i));
        if (isPalin(arr)) {
            partition.push(arr.join(""));
            helper(i+1, partition, []);
            partition.pop();
        }
        helper(i+1, partition, arr);
    }

    helper(0, [], []);

    return ans;
};
