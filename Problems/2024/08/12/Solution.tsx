class heapq {
    arr: number[];

    constructor() {
        this.arr = [null];
    }

    push(val: number): void {
        this.arr.push(val);
        let i = this.arr.length - 1;
        while (i > 1 && this.arr[i] < this.arr[Math.floor(i / 2)]) {
            const tmp = this.arr[Math.floor(i / 2)];
            this.arr[Math.floor(i / 2)] = this.arr[i];
            this.arr[i] = tmp;
            i = Math.floor(i / 2);
        }
    }

    pop(): number {
        const ret = this.arr[1];
        this.arr[1] = this.arr.pop();
        let i = 1;
        while (i * 2 < this.arr.length) {
            const tmp = this.arr[i];
            if (i * 2 + 1 < this.arr.length && this.arr[i * 2] > this.arr[i * 2 + 1] && this.arr[i] > this.arr[i * 2 + 1]) {
                this.arr[i] = this.arr[i * 2 + 1];
                i = i * 2 + 1;
                this.arr[i] = tmp;
            } else if (this.arr[i] > this.arr[i * 2]) {
                this.arr[i] = this.arr[i * 2];
                i = i * 2;
                this.arr[i] = tmp;
            } else {
                break;
            }
        }
        return ret;
    }

    size(): number {
        return this.arr.length-1;
    }

    peak(): number {
        return this.arr[1];
    }
}

class KthLargest {

    q: heapq;
    k: number;

    constructor(k: number, nums: number[]) {
        this.q = new heapq();
        for (const num of nums) {
            this.q.push(num);
        }
        while (this.q.size() > k) {
            this.q.pop();
        }
        this.k = k;
    }

    add(val: number): number {
        this.q.push(val);
        if (this.q.size() > this.k) {
            this.q.pop();
        }
        return this.q.peak();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
