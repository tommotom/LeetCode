class Node {
    next = null;
    val = null;
    constructor(val) {
        this.val = val;
    }
}

class Q {
    length = 0;
    head = new Node(null);
    tail = this.head;

    add(obj) {
        this.length++;
        this.tail.next = new Node(obj);
        this.tail = this.tail.next;
    }

    poll() {
        if (this.length === 0) {
            return null;
        }
        this.length--;
        const tmp = this.head;
        this.head = this.head.next;
        tmp.next = null;
        return this.head.val
    }

    size() {
        return this.length;
    }
}

function maximumSafenessFactor(grid: number[][]): number {
    const n = grid.length;
    const dists = Array(n).fill(false).map(() => Array(n).fill(Number.MAX_SAFE_INTEGER));
    const dirs = [[0,1], [0,-1], [1,0], [-1,0]];

    const q = new Q();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                q.add([i, j, 0]);
            }
        }
    }

    while (q.size() > 0) {
        const [i, j, d] = q.poll();
        if (dists[i][j] <= d) {
            continue;
        }
        dists[i][j] = d
        for (const [di, dj] of dirs) {
            if (i+di < 0 || i+di === n || j+dj < 0 || j+dj === n) {
                continue;
            }
            q.add([i+di, j+dj, d + 1]);
        }
    }

    const isValidPath = d => {
        const visited = Array(n).fill(false).map(() => Array(n).fill(false));
        const q = new Q();
        q.add([0, 0])
        while (q.size() > 0) {
            const [i, j] = q.poll();
            if (visited[i][j] || dists[i][j] < d) {
                continue;
            }
            visited[i][j] = true;
            for (const [di, dj] of dirs) {
                if (i+di < 0 || i+di === n || j+dj < 0 || j+dj === n) {
                    continue;
                }
                q.add([i+di, j+dj]);
            }
        }
        return visited[n-1][n-1];
    }

    let l = 0, r = n;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (isValidPath(m)) {
            l = m + 1
        } else {
            r = m;
        }
    }

    return l - 1;
};
