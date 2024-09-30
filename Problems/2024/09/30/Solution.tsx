class CustomStack {

    st: number[];
    inc: number[];
    top: number;

    constructor(maxSize: number) {
        this.st = Array(maxSize).fill(0);
        this.inc = Array(maxSize).fill(0);
        this.top = -1;
    }

    push(x: number): void {
        if (this.top + 1 === this.st.length) {
            return;
        }
        this.top++;
        this.st[this.top] = x;
    }

    pop(): number {
        if (this.top < 0) {
            return -1;
        }
        const ret = this.st[this.top] + this.inc[this.top];
        if (this.top > 0) {
            this.inc[this.top-1] += this.inc[this.top];
        }
        this.inc[this.top] = 0;
        this.top--;
        return ret;
    }

    increment(k: number, val: number): void {
        if (this.top >= 0) {
            const i = Math.min(k-1, this.top);
            this.inc[i] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
