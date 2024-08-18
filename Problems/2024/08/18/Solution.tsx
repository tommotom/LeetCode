class heapq {
    arr: number[];

    constructor() {
        this.arr = [null];
    }

    push(val: number): void {
        this.arr.push(val);
        let i = this.arr.length-1;
        while (i > 1) {
            const j = Math.floor(i / 2);
            if (this.arr[j] > this.arr[i]) {
                this.swap(i, j);
            }
            i = j;
        }
    }

    poll(): number {
        const ret = this.arr[1];
        this.arr[1] = this.arr.pop();
        let i = 1;
        while (i < this.arr.length) {
            const j = i * 2;
            if (j >= this.arr.length) {
                break;
            }
            if (j+1 === this.arr.length) {
                if (this.arr[i] <= this.arr[j]) {
                    break;
                }
                this.swap(i, j);
                i = j;
            } else if (this.arr[j] < this.arr[j+1]) {
                if (this.arr[i] <= this.arr[j]) {
                    break;
                }
                this.swap(i, j);
                i = j;
            } else {
                if (this.arr[i] <= this.arr[j+1]) {
                    break;
                }
                this.swap(i, j+1);
                i = j+1;
            }
        }
        return ret;
    }

    swap(i: number, j: number): void {
        const tmp = this.arr[i]
        this.arr[i] = this.arr[j]
        this.arr[j] = tmp;
    }
}

function nthUglyNumber(n: number): number {
    const q = new heapq();
    const seen = new Set();
    q.push(1);
    for (let i = 0; i < n; i++) {
        const num = q.poll();
        if (!seen.has(num * 2)) {
            q.push(num * 2);
            seen.add(num * 2);
        }
        if (!seen.has(num * 3)) {
            q.push(num * 3);
            seen.add(num * 3);
        }
        if (!seen.has(num * 5)) {
            q.push(num * 5);
            seen.add(num * 5);
        }
    }
    return q.poll();
};
