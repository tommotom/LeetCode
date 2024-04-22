function openLock(deadends: string[], target: string): number {
    const genNext = cur => {
        const ret = [];
        const arr = cur.split('');
        for (let i = 0; i < 4; i++) {
            const tmp = arr[i];
            const num = Number(arr[i]);
            arr[i] = (num === 9 ? 0 : num+1).toString();
            ret.push(arr.join(''));
            arr[i] = (num === 0 ? 9 : num-1).toString();
            ret.push(arr.join(''));
            arr[i] = tmp;
        }
        return ret;
    }

    const set = new Set(deadends);
    const visited = new Map();
    const q: [string, number][] = [['0000', 0]];
    while (q.length > 0) {
        const [cur, step] = q.shift();
        if (set.has(cur) || visited.has(cur)) {
            continue;
        }
        if (cur === target) {
            return step;
        }
        visited.set(cur, step);
        for (const next of genNext(cur)) {
            if (set.has(next) || visited.has(next)) {
                continue;
            }
            q.push([next, step+1]);
        }
    }
    return -1;
};
