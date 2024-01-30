class MyQueue {

    st = [];

    constructor() {
    }

    push(x: number): void {
        this.st.push(x);
    }

    pop(): number {
        const tmp = [];
        while (this.st.length > 1) {
            tmp.push(this.st.pop());
        }
        const ret = this.st.pop();
        while (tmp.length > 0) {
            this.st.push(tmp.pop());
        }
        return ret;
    }

    peek(): number {
        return this.st[0];
    }

    empty(): boolean {
        return this.st.length === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
