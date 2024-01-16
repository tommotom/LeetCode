class RandomizedSet {
    arr = [];
    index = new Map();

    constructor() {
    }

    insert(val: number): boolean {
        if (this.index.has(val)) {
            return false;
        }
        this.arr.push(val);
        this.index.set(val, this.arr.length - 1);
        return true;
    }

    remove(val: number): boolean {
        if (!this.index.has(val)) {
            return false;
        }
        const i = this.index.get(val);
        this.arr[i] = this.arr[this.arr.length-1];
        this.arr.pop();
        this.index.set(this.arr[i], i);
        this.index.delete(val);
        return true;
    }

    getRandom(): number {
        return this.arr[Math.floor(Math.random() * this.arr.length)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
