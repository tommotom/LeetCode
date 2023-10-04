class MyHashMap {

    map = [...Array(1000)].map(_ => []);

    constructor() {

    }

    hash(key: number): number {
        return key % 1000;
    }

    put(key: number, value: number): void {
        this.remove(key);
        const k = this.hash(key);
        this.map[k].push([key, value]);
    }

    get(key: number): number {
        for (const [k, v] of this.map[this.hash(key)]) {
            if (k === key) {
                return v;
            }
        }
        return -1;
    }

    remove(key: number): void {
        const k = this.hash(key);
        for(let i = 0; i < this.map[k].length; i++) {
            if (this.map[k][i][0] === key) {
                this.map[k].splice(i, 1);
                break;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
