function removeDuplicateLetters(s: string): string {
    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }

    const ans = [];
    for (const c of s) {
        counter.set(c, counter.get(c) - 1);
        if (ans.includes(c)) {
            continue;
        }
        while (ans.length > 0) {
            const last = ans[ans.length-1];
            if (last > c && counter.get(last) > 0) {
                ans.pop();
            } else {
                break;
            }
        }
        ans.push(c);
    }

    return ans.join('');
};
