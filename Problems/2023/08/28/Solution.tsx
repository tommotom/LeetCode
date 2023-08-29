class MyStack {

    q: number[];

    constructor() {
        this.q = [];
    }

    push(x: number): void {
        this.q.push(x);
    }

    pop(): number {
        return this.q.pop();
    }

    top(): number {
        return this.q[this.q.length-1];
    }

    empty(): boolean {
        return this.q.length === 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
