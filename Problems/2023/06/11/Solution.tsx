class SnapshotArray {
    arr: number[];
    snapCount: number;
    snapShots: Map<number, Array<[number, number]>>;

    constructor(length: number) {
        this.snapCount = 0;
        this.snapShots = new Map<number, Array<[number, number]>>();
    }

    set(index: number, val: number): void {
        if (this.snapShots.has(index)) {
            this.snapShots.get(index).push([this.snapCount, val]);
        } else {
            this.snapShots.set(index, new Array([this.snapCount, val]));
        }
    }

    snap(): number {
        this.snapCount++;
        return this.snapCount - 1;
    }

    get(index: number, snap_id: number): number {
        if (!this.snapShots.has(index)) {
            return 0;
        }
        const arr: Array<[number, number]> = this.snapShots.get(index);
        let l = 0;
        let r = arr.length;
        while (l < r) {
            let m = Math.floor(l + (r - l) / 2);
            if (arr[m][0] <= snap_id) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l > 0 ? arr[l-1][1] : 0;
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
