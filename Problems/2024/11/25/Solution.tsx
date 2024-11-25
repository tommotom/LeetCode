function slidingPuzzle(board: number[][]): number {
    const toString = board => {
        return board.map(row => row.join('')).join('');
    }
    const seen = new Set();
    seen.add(toString(board));

    const q = [{cur: board, step: 0}];

    const isExchangable = (cur, r1, c1, r2, c2) => {
        return cur[r1][c1] === 0 || cur[r2][c2] === 0;
    }

    const exchange = (cur, r1, c1, r2, c2, step) => {
        const tmp = cur[r1][c1];
        cur[r1][c1] = cur[r2][c2];
        cur[r2][c2] = tmp;
        const next = toString(cur);
        if (!seen.has(next)) {
            seen.add(next);
            q.push({cur: [[...cur[0]], [...cur[1]]], step: step+1});
        }
        cur[r2][c2] = cur[r1][c1];
        cur[r1][c1] = tmp;
    }

    const adj = [[0,0,1,0], [0,1,1,1], [0,2,1,2], [0,0,0,1], [0,1,0,2], [1,0,1,1], [1,1,1,2]];

    while (q.length > 0) {
        const {cur, step} = q.shift();
        if (toString(cur) === '123450') {
            return step;
        }
        for (const [r1, c1, r2, c2] of adj) {
            if (isExchangable(cur, r1, c1, r2, c2)) {
                exchange(cur, r1, c1, r2, c2, step);
            }
        }
    }
    return -1;
};
